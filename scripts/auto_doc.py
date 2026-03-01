#!/usr/bin/env python3
"""
auto-doc: Unified Documentation Pipeline CLI

Pre-collects all possible documentation sources for a library, assesses
their quality, and outputs structured JSON for downstream decision-making.

Usage:
    python3 scripts/auto_doc.py probe fastapi
    python3 scripts/auto_doc.py probe fastapi --domain fastapi.tiangolo.com --github fastapi/fastapi
    python3 scripts/auto_doc.py fetch fastapi --source llms-txt --url https://fastapi.tiangolo.com/llms-full.txt
    python3 scripts/auto_doc.py validate --json --max-score 50 --source web-scraped
    python3 scripts/auto_doc.py status --json
"""

import importlib.util
import json
import os
import re
import sqlite3
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

import requests
import typer
import yaml


# ---------------------------------------------------------------------------
# Verbose logging
# ---------------------------------------------------------------------------
_VERBOSE = bool(os.environ.get("AUTO_DOC_VERBOSE"))


_STDERR_FD = None


def _log(msg: str) -> None:
    """Print a debug message to stderr when verbose mode is on.

    Uses os.write to the original stderr fd so that typer's CliRunner
    (which monkey-patches sys.stderr) cannot capture debug output.
    """
    if not _VERBOSE:
        return
    global _STDERR_FD
    if _STDERR_FD is None:
        _STDERR_FD = os.dup(2)  # duplicate the real fd 2 before CliRunner can touch it
    os.write(_STDERR_FD, f"  [debug] {msg}\n".encode())


def _ensure_github_token():
    """Load GitHub token for authenticated API access (5000 req/hr vs 60).

    Priority: GH_TOKEN env var > GITHUB_TOKEN env var > `gh auth token` CLI.
    """
    if os.environ.get("GH_TOKEN"):
        return
    if os.environ.get("GITHUB_TOKEN"):
        os.environ["GH_TOKEN"] = os.environ["GITHUB_TOKEN"]
        return
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            os.environ["GH_TOKEN"] = result.stdout.strip()
    except Exception:
        pass


_ensure_github_token()

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DOCS_DIR = REPO_ROOT / "docs"
INDEX_PATH = REPO_ROOT / "index.yaml"
LLMS_SITES_YAML = SCRIPT_DIR / "llms-sites.yaml"
REPO_CONFIG_YAML = SCRIPT_DIR / "repo_config.yaml"
DOC_INDEX_DB = SCRIPT_DIR / "doc_index.db"
UNIFIED_INDEX_DB = Path.home() / "gitea" / "reverse-dns-indexer" / "results" / "unified-index.db"
DOMAINS_DIR = Path.home() / "gitea" / "auto-doc" / "domains"
STACK_V2_DB = Path.home() / "gitea" / "auto-doc" / "stack-v2" / "results" / "doc_platforms.db"

# ---------------------------------------------------------------------------
# Import helper – existing scripts have hyphens in filenames
# ---------------------------------------------------------------------------

def _import_script(name: str, path: Path):
    """Import a Python module from a file path (works with hyphened filenames)."""
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _get_llms_scraper():
    return _import_script("llms_txt_scraper", SCRIPT_DIR / "llms-txt-scraper.py")


def _get_validator():
    return _import_script("validate_markdown", SCRIPT_DIR / "validate-markdown.py")


def _get_index_updater():
    return _import_script("update_index", SCRIPT_DIR / "update-index.py")


# ---------------------------------------------------------------------------
# Typer app
# ---------------------------------------------------------------------------

app = typer.Typer(
    name="auto-doc",
    help="Unified documentation pipeline CLI for llm-code-docs.",
    no_args_is_help=True,
)

# ---------------------------------------------------------------------------
# Shared utilities
# ---------------------------------------------------------------------------

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "auto-doc/1.0 (llm-code-docs pipeline)",
    "Accept": "text/plain, text/markdown, */*",
})


def _head(url: str, timeout: float = 5.0) -> int:
    """Return HTTP status code from a HEAD request, 0 on error."""
    try:
        r = SESSION.head(url, timeout=timeout, allow_redirects=True)
        return r.status_code
    except Exception:
        return 0


def _get(url: str, timeout: float = 30.0) -> Optional[requests.Response]:
    """GET a URL, returning None on error."""
    try:
        r = SESSION.get(url, timeout=timeout, allow_redirects=True)
        r.raise_for_status()
        return r
    except Exception:
        return None


def _run_cmd(cmd: list[str], timeout: int = 15) -> Optional[str]:
    """Run a subprocess, return stdout or None on failure."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if result.returncode == 0:
            return result.stdout.strip()
        return None
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Discovery: find official site & GitHub repo for a library
# ---------------------------------------------------------------------------

def _discover_pypi(library: str) -> dict:
    """Query PyPI JSON API to find project URLs."""
    info: dict = {"domain": None, "github": None, "pypi_found": False}
    try:
        r = SESSION.get(f"https://pypi.org/pypi/{library}/json", timeout=10)
        if r.status_code != 200:
            return info
    except Exception:
        return info

    data = r.json().get("info", {})
    info["pypi_found"] = True
    _log(f"pypi: found '{library}'")
    project_urls = data.get("project_urls") or {}

    # Find documentation URL
    doc_keys = ["Documentation", "Docs", "Homepage", "Home", "documentation", "docs"]
    for key in doc_keys:
        url = project_urls.get(key)
        if url and "pypi.org" not in url and "github.com" not in url:
            parsed = urlparse(url)
            info["domain"] = parsed.netloc or parsed.hostname
            break

    # Fallback: home_page field
    if not info["domain"] and data.get("home_page"):
        hp = data["home_page"]
        if "github.com" not in hp and "pypi.org" not in hp:
            parsed = urlparse(hp)
            info["domain"] = parsed.netloc or parsed.hostname

    # Find GitHub repo
    gh_keys = ["Source", "Repository", "Source Code", "GitHub", "Code",
                "source", "repository", "github", "code"]
    for key in gh_keys:
        url = project_urls.get(key, "")
        if "github.com" in url:
            parts = urlparse(url).path.strip("/").split("/")
            if len(parts) >= 2:
                info["github"] = f"{parts[0]}/{parts[1]}"
                break

    # Fallback: home_page
    if not info["github"] and data.get("home_page") and "github.com" in data["home_page"]:
        parts = urlparse(data["home_page"]).path.strip("/").split("/")
        if len(parts) >= 2:
            info["github"] = f"{parts[0]}/{parts[1]}"

    return info


def _discover_npm(library: str) -> dict:
    """Query npm registry for package URLs."""
    info: dict = {"domain": None, "github": None, "npm_found": False}
    try:
        r = SESSION.get(f"https://registry.npmjs.org/{library}", timeout=10)
        if r.status_code != 200:
            return info
    except Exception:
        return info

    data = r.json()
    info["npm_found"] = True
    _log(f"npm: found '{library}'")

    # Homepage
    homepage = data.get("homepage", "")
    if homepage and "github.com" not in homepage and "npmjs.com" not in homepage:
        parsed = urlparse(homepage)
        info["domain"] = parsed.netloc or parsed.hostname

    # Repository
    repo = data.get("repository", {})
    repo_url = repo.get("url", "") if isinstance(repo, dict) else str(repo)
    if "github.com" in repo_url:
        # normalize git+https://github.com/owner/repo.git
        cleaned = repo_url.replace("git+", "").replace("git://", "https://").replace(".git", "")
        parts = urlparse(cleaned).path.strip("/").split("/")
        if len(parts) >= 2:
            info["github"] = f"{parts[0]}/{parts[1]}"

    return info


NOISE_DOMAINS = {"pypi.org", "npmjs.com", "crates.io", "github.com",
                 "rubygems.org", "packagist.org", "stackoverflow.com",
                 "en.wikipedia.org", "medium.com", "dev.to", "reddit.com"}

# Language-specific doc hosts — these are VALID targets, not noise
LANG_DOC_HOSTS = {"docs.rs", "pkg.go.dev", "hexdocs.pm", "metacpan.org",
                  "javadoc.io", "hackage.haskell.org", "rubydoc.info",
                  "pub.dev"}


def _discover_crates_io(library: str) -> dict:
    """Query crates.io API for Rust crate URLs."""
    info: dict = {"source": "crates.io", "domain": None, "github": None, "found": False}
    try:
        r = SESSION.get(f"https://crates.io/api/v1/crates/{library}", timeout=10,
                        headers={"User-Agent": "auto-doc/1.0 (llm-code-docs pipeline)"})
        if r.status_code != 200:
            return info
    except Exception:
        return info

    crate = r.json().get("crate", {})
    info["found"] = True
    _log(f"crates.io: found '{library}'")

    doc_url = crate.get("documentation") or ""
    if doc_url and "docs.rs" not in doc_url and "github.com" not in doc_url:
        parsed = urlparse(doc_url)
        info["domain"] = parsed.netloc or parsed.hostname

    if not info["domain"]:
        homepage = crate.get("homepage") or ""
        if homepage and "github.com" not in homepage and "crates.io" not in homepage:
            parsed = urlparse(homepage)
            info["domain"] = parsed.netloc or parsed.hostname

    repo_url = crate.get("repository") or ""
    if "github.com" in repo_url:
        parts = urlparse(repo_url).path.strip("/").rstrip(".git").split("/")
        if len(parts) >= 2:
            info["github"] = f"{parts[0]}/{parts[1]}"

    return info


def _discover_github_search(library: str) -> dict:
    """Search GitHub API for repositories matching the library name.

    Returns raw results for the LLM to reason about — does NOT pick a winner.
    """
    info: dict = {"source": "github_search", "domain": None, "github": None,
                  "candidates": [], "found": False}

    search_data = _github_api_get(
        f"search/repositories?q={library}+in:name&sort=stars&order=desc&per_page=25",
        timeout=10,
    )
    if not search_data or "items" not in search_data:
        return info

    for repo in search_data["items"]:
        candidate = {
            "full_name": repo.get("full_name", ""),
            "name": repo.get("name", ""),
            "description": (repo.get("description") or "")[:200],
            "stars": repo.get("stargazers_count", 0),
            "homepage": repo.get("homepage") or "",
            "language": repo.get("language") or "",
            "fork": repo.get("fork", False),
            "archived": repo.get("archived", False),
        }
        info["candidates"].append(candidate)

    _log(f"github_search: {len(info['candidates'])} candidates")
    # Best-effort pick: exact name match with most stars
    for c in info["candidates"]:
        if c["name"].lower() == library.lower() and not c["fork"]:
            info["found"] = True
            info["github"] = c["full_name"]
            if c["homepage"] and urlparse(c["homepage"]).netloc not in NOISE_DOMAINS:
                info["domain"] = urlparse(c["homepage"]).netloc
            break

    return info


def _discover_tavily(library: str) -> dict:
    """Use Tavily search to find documentation sites and repos.

    This is the primary discovery mechanism for libraries not in any
    package registry. Returns raw search results for the LLM.
    Always runs — even with index hits — to provide grounding.
    """
    info: dict = {"source": "tavily", "domain": None, "github": None,
                  "search_results": [], "answer": None, "available": False}

    stdout = _run_cmd(
        ["tavily", "-f", "json", "search",
         f"{library} official documentation", "-n", "10"],
        timeout=15,
    )
    if not stdout:
        return info

    info["available"] = True
    _log(f"tavily: search returned results")

    try:
        parsed = json.loads(stdout)
    except (json.JSONDecodeError, AttributeError):
        _log("tavily: failed to parse JSON response")
        return info

    info["answer"] = parsed.get("answer")
    results = parsed.get("results", [])
    _log(f"tavily: {len(results)} results, answer={'yes' if info['answer'] else 'no'}")

    for item in results:
        url = item.get("url", "")
        title = item.get("title", "")
        p = urlparse(url)
        host = p.netloc or ""

        info["search_results"].append({"title": title, "url": url})

        if "github.com" in host:
            parts = p.path.strip("/").split("/")
            if len(parts) >= 2 and not info["github"]:
                info["github"] = f"{parts[0]}/{parts[1]}"
        elif host and host not in NOISE_DOMAINS:
            if not info["domain"]:
                info["domain"] = host

    return info


def _discover_unified_index(library: str) -> dict:
    """Check the unified package index (5.14M packages / 53 registries) for doc URLs."""
    info: dict = {"source": "unified_index", "found": False, "matches": [],
                  "domain": None, "github": None}
    if not UNIFIED_INDEX_DB.exists():
        _log(f"unified_index: DB not found at {UNIFIED_INDEX_DB}")
        return info
    norm = library.lower().replace("_", "-")
    conn = sqlite3.connect(str(UNIFIED_INDEX_DB))
    try:
        rows = conn.execute(
            "SELECT registry, name, docs_url, homepage, repository_url, "
            "doc_host, downloads FROM packages "
            "WHERE LOWER(REPLACE(name, '_', '-')) = ? "
            "AND docs_url IS NOT NULL AND docs_url <> '' "
            "ORDER BY downloads DESC LIMIT 20",
            (norm,)
        ).fetchall()
        cols = ["registry", "name", "docs_url", "homepage", "repository_url",
                "doc_host", "downloads"]
        for row in rows:
            m = dict(zip(cols, row))
            host = m.get("doc_host", "") or ""
            # Filter out forge URLs (github/gitlab/bitbucket)
            if host in ("github.com", "gitlab.com", "bitbucket.org"):
                continue
            info["matches"].append(m)
            if not info["domain"] and host:
                info["domain"] = host
            if not info["github"] and m.get("repository_url"):
                repo = m["repository_url"]
                if "github.com" in repo:
                    parts = urlparse(repo).path.strip("/").rstrip(".git").split("/")
                    if len(parts) >= 2:
                        info["github"] = f"{parts[0]}/{parts[1]}"
        info["found"] = bool(info["matches"])
        _log(f"unified_index: {len(info['matches'])} matches, domain={info['domain']}, github={info['github']}")
    finally:
        conn.close()
    return info


_DOMAIN_CACHE: dict[str, list[tuple[str, str]]] = {}  # {platform: [(domain, full_url)]}


def _load_domains() -> list[tuple[str, str]]:
    """Load all enumerated doc domains (cached)."""
    if _DOMAIN_CACHE:
        return [(d, p) for p, pairs in _DOMAIN_CACHE.items() for d, _ in pairs]
    files = {
        "gitbook": DOMAINS_DIR / "gitbook" / "clean-gitbook.txt",
        "readme": DOMAINS_DIR / "readme" / "clean-readme.txt",
        "mintlify": DOMAINS_DIR / "mintlify" / "clean-mintlify-app-names.txt",
        "fern": DOMAINS_DIR / "fern" / "clean-ferndocs.txt",
        "custom": DOMAINS_DIR / "custom-domains" / "clean-custom-domains.txt",
    }
    for platform, path in files.items():
        if not path.exists():
            continue
        entries = []
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line:
                continue
            if platform == "mintlify":
                entries.append((line, f"https://{line}.mintlify.app"))
            elif platform == "custom":
                entries.append((line.split("/")[0], f"https://{line}"))
            else:
                entries.append((line, f"https://{line}"))
        _DOMAIN_CACHE[platform] = entries
    return [(d, p) for p, pairs in _DOMAIN_CACHE.items() for d, _ in pairs]


def _discover_domains(library: str) -> dict:
    """Check enumerated doc-hosting domains (6.8K) for matches."""
    info: dict = {"source": "enumerated_domains", "found": False, "matches": [], "domain": None}
    norm = library.lower().replace("_", "-")
    _load_domains()
    for platform, entries in _DOMAIN_CACHE.items():
        for domain, url in entries:
            slug = domain.split(".")[0].lower() if "." in domain else domain.lower()
            if slug == norm or norm in slug.split("-"):
                info["matches"].append({"domain": domain, "platform": platform, "url": url})
                if not info["domain"]:
                    info["domain"] = domain
    info["found"] = bool(info["matches"])
    _log(f"enumerated_domains: {len(info['matches'])} matches, domain={info['domain']}")
    return info


def _enrich_stack_v2(github_repo: str) -> dict:
    """Check Stack V2 for doc-platform signals on a GitHub repo."""
    info: dict = {"found": False, "platforms": [], "star_events_count": 0}
    if not STACK_V2_DB.exists() or not github_repo:
        _log(f"stack_v2: skipped (db_exists={STACK_V2_DB.exists()}, repo={github_repo})")
        return info
    conn = sqlite3.connect(str(STACK_V2_DB))
    try:
        rows = conn.execute(
            "SELECT platform, matched_files FROM platform_repos WHERE repo_name = ?",
            (github_repo,)
        ).fetchall()
        for platform, matched_files in rows:
            info["platforms"].append({"platform": platform, "matched_files": matched_files})
        star_row = conn.execute(
            "SELECT star_events_count FROM repos_with_docs WHERE repo_name = ?",
            (github_repo,)
        ).fetchone()
        if star_row:
            info["star_events_count"] = star_row[0] or 0
        info["found"] = bool(info["platforms"])
        _log(f"stack_v2: {len(info['platforms'])} platforms, stars={info['star_events_count']}")
    finally:
        conn.close()
    return info


def _discover_domain_guess(library: str) -> dict:
    """HEAD-probe common TLDs to find documentation sites."""
    info: dict = {"source": "domain_guess", "domain": None, "probed": []}

    clean = library.lower().replace("_", "").replace("-", "")
    tlds = [".dev", ".io", ".org", ".com", ".sh", ".rs", ".land"]
    candidates = []
    for tld in tlds:
        candidates.append(f"{clean}{tld}")
        if clean != library.lower():
            candidates.append(f"{library.lower()}{tld}")

    # Deduplicate
    seen = set()
    unique = []
    for c in candidates:
        if c not in seen:
            seen.add(c)
            unique.append(c)

    results: dict[str, int] = {}
    with ThreadPoolExecutor(max_workers=len(unique)) as pool:
        futures = {pool.submit(_head, f"https://{c}/", 3.0): c for c in unique}
        for fut in as_completed(futures):
            d = futures[fut]
            status = fut.result()
            info["probed"].append({"domain": d, "status": status})
            if 200 <= status < 400:
                results[d] = status

    if results:
        info["domain"] = next(iter(results))

    return info


def _lookup_doc_index(library: str) -> list[dict] | None:
    """Check the pre-computed doc index for known documentation sources.

    Returns a list of {platform, doc_url, doc_type, ...} dicts if found,
    or None if the index doesn't exist or has no entry for this library.
    """
    if not DOC_INDEX_DB.exists():
        return None
    try:
        from doc_index import get_db, lookup
        conn = get_db(DOC_INDEX_DB)
        try:
            results = lookup(conn, library)
        finally:
            conn.close()
        return results if results else None
    except Exception:
        return None


def _best_guess_from_index(index_results: list[dict]) -> dict:
    """Extract a best_guess {domain, github} from doc index results."""
    domain = None
    for r in index_results:
        url = r.get("doc_url", "")
        if url:
            from urllib.parse import urlparse as _urlparse
            host = _urlparse(url).netloc
            if host:
                domain = host
                break
    return {"domain": domain, "github": None}


def discover(library: str) -> dict:
    """Discover all possible documentation sources for a library.

    Runs ALL discovery sources in parallel and returns structured results
    for downstream LLM decision-making. Does NOT pick a single winner —
    that's the LLM's job (MiniMax-M2.5 via clauded-mm).

    Returns dict with:
      - registries: results from PyPI, npm, crates.io
      - github_search: GitHub search results with candidates
      - tavily_search: web search results (always runs, even with index hit)
      - domain_guess: HEAD-probed common TLDs
      - best_guess: {domain, github} — our best deterministic pick (may be wrong)
      - doc_index: pre-computed index results (if found)
    """
    discovery: dict = {
        "registries": {},
        "github_search": {},
        "tavily_search": {},
        "domain_guess": {},
        "unified_index": {},
        "enumerated_domains": {},
        "best_guess": {"domain": None, "github": None},
    }

    # Check pre-computed doc index (fast, local)
    _log(f"discover: starting parallel discovery for '{library}'")
    index_results = _lookup_doc_index(library)
    if index_results:
        discovery["doc_index"] = index_results
        discovery["best_guess"] = _best_guess_from_index(index_results)
        _log(f"discover: doc_index hit — {len(index_results)} entries, best_guess={discovery['best_guess']}")
    else:
        _log("discover: no doc_index hit")

    # Always run Tavily for grounding + full discovery for non-index cases
    _log("discover: launching 8 parallel discovery workers")
    with ThreadPoolExecutor(max_workers=8) as pool:
        fut_pypi = pool.submit(_discover_pypi, library)
        fut_npm = pool.submit(_discover_npm, library)
        fut_crates = pool.submit(_discover_crates_io, library)
        fut_gh = pool.submit(_discover_github_search, library)
        fut_tavily = pool.submit(_discover_tavily, library)
        fut_guess = pool.submit(_discover_domain_guess, library)
        fut_unified = pool.submit(_discover_unified_index, library)
        fut_domains = pool.submit(_discover_domains, library)

        pypi = fut_pypi.result()
        npm = fut_npm.result()
        crates = fut_crates.result()
        gh_search = fut_gh.result()
        tavily_info = fut_tavily.result()
        domain_guess = fut_guess.result()
        unified = fut_unified.result()
        domains = fut_domains.result()

    _log("discover: all workers completed")

    # Store raw results
    if pypi.get("pypi_found"):
        discovery["registries"]["pypi"] = pypi
    if npm.get("npm_found"):
        discovery["registries"]["npm"] = npm
    if crates.get("found"):
        discovery["registries"]["crates_io"] = crates

    discovery["github_search"] = gh_search
    discovery["tavily_search"] = tavily_info
    discovery["domain_guess"] = domain_guess
    if unified.get("found"):
        discovery["unified_index"] = unified
    if domains.get("found"):
        discovery["enumerated_domains"] = domains

    regs = list(discovery["registries"].keys())
    _log(f"discover: registries={regs}, gh_candidates={len(gh_search.get('candidates', []))}, "
         f"tavily_results={len(tavily_info.get('search_results', []))}, "
         f"unified={'yes' if unified.get('found') else 'no'}, "
         f"domains={'yes' if domains.get('found') else 'no'}")

    # Build best_guess using a scoring approach rather than first-wins
    # The GLM gets ALL data and can override this
    domain_candidates: list[tuple[str, int]] = []  # (domain, confidence)
    github_candidates: list[tuple[str, int]] = []  # (owner/repo, confidence)

    # GitHub search: highest-star exact-name match is very strong signal
    if gh_search.get("github"):
        stars = 0
        for c in gh_search.get("candidates", []):
            if c["full_name"] == gh_search["github"]:
                stars = c.get("stars", 0)
                break
        # High-star repos are almost certainly the right one
        confidence = min(100, 50 + stars // 1000)
        github_candidates.append((gh_search["github"], confidence))
        if gh_search.get("domain"):
            domain_candidates.append((gh_search["domain"], confidence))

    # Registry results: strong for domain if the package is popular,
    # but registries can have name squatters (e.g., "caddy" on PyPI)
    for src in [pypi, npm, crates]:
        if src.get("github"):
            # Registry github link is reliable
            github_candidates.append((src["github"], 70))
        if src.get("domain"):
            domain_candidates.append((src["domain"], 40))

    # Tavily: good signal when available
    if tavily_info.get("github"):
        github_candidates.append((tavily_info["github"], 60))
    if tavily_info.get("domain"):
        domain_candidates.append((tavily_info["domain"], 60))

    # Unified index: strong for github, moderate for domain
    if unified.get("github"):
        github_candidates.append((unified["github"], 75))
    if unified.get("domain"):
        domain_candidates.append((unified["domain"], 65))

    # Enumerated domains: moderate signal
    if domains.get("domain"):
        domain_candidates.append((domains["domain"], 55))

    # Domain guessing: weakest signal
    if domain_guess.get("domain"):
        domain_candidates.append((domain_guess["domain"], 20))

    # Pick highest-confidence candidates
    domain = None
    github = None
    if github_candidates:
        github_candidates.sort(key=lambda x: x[1], reverse=True)
        github = github_candidates[0][0]
    if domain_candidates:
        domain_candidates.sort(key=lambda x: x[1], reverse=True)
        domain = domain_candidates[0][0]

    # Cross-validate: if the top GitHub repo has a homepage that matches
    # a domain candidate, prefer that domain (strong correlation signal)
    if github and gh_search.get("candidates"):
        for c in gh_search["candidates"]:
            if c["full_name"] == github and c.get("homepage"):
                hp_host = urlparse(c["homepage"]).netloc
                if hp_host and hp_host not in NOISE_DOMAINS:
                    domain = hp_host
                    break

    discovery["best_guess"] = {"domain": domain, "github": github}
    _log(f"discover: best_guess domain={domain}, github={github}")

    return discovery


# ---------------------------------------------------------------------------
# Check existing docs
# ---------------------------------------------------------------------------

def check_existing(library: str) -> dict:
    """Check if documentation already exists in the repo."""
    result = {
        "already_exists": False,
        "existing_paths": [],
        "configured_in": [],
    }

    # Normalize: try common variations
    names = {library, library.lower(), library.replace("-", ""), library.replace("_", "-")}

    # Check docs directories
    for source in ["llms-txt", "github-scraped", "web-scraped"]:
        source_dir = DOCS_DIR / source
        if not source_dir.exists():
            continue
        for d in source_dir.iterdir():
            if d.is_dir() and d.name.lower() in {n.lower() for n in names}:
                result["existing_paths"].append(str(d.relative_to(REPO_ROOT)))
                result["already_exists"] = True

    # Check YAML configs
    if LLMS_SITES_YAML.exists():
        with open(LLMS_SITES_YAML) as f:
            sites_config = yaml.safe_load(f) or {}
        for site in sites_config.get("sites", []):
            if site.get("name", "").lower() in {n.lower() for n in names}:
                result["configured_in"].append("llms-sites.yaml")
                break

    if REPO_CONFIG_YAML.exists():
        with open(REPO_CONFIG_YAML) as f:
            repo_config = yaml.safe_load(f) or {}
        for repo in repo_config.get("repositories", []):
            if repo.get("name", "").lower() in {n.lower() for n in names}:
                result["configured_in"].append("repo_config.yaml")
                break

    return result


# ---------------------------------------------------------------------------
# Probe llms.txt
# ---------------------------------------------------------------------------

LLMS_TXT_PATHS = [
    "/llms.txt",
    "/llms-full.txt",
    "/docs/llms.txt",
    "/docs/llms-full.txt",
    "/.well-known/llms.txt",
]

SUBDOMAIN_PREFIXES = ["docs.", "www.", "developers."]


def _build_probe_urls(domain: str) -> list[str]:
    """Build list of candidate llms.txt URLs for a domain."""
    urls = []
    # Strip any path from domain
    domain = domain.split("/")[0]

    # Base domain
    for path in LLMS_TXT_PATHS:
        urls.append(f"https://{domain}{path}")

    # Subdomains
    for prefix in SUBDOMAIN_PREFIXES:
        if not domain.startswith(prefix):
            sub = f"{prefix}{domain}"
            for path in LLMS_TXT_PATHS:
                urls.append(f"https://{sub}{path}")

    return urls


def _assess_llms_txt_content(url: str, content: str) -> dict:
    """Assess quality of an llms.txt file's content."""
    result = {
        "url": url,
        "http_status": 200,
        "size_bytes": len(content.encode("utf-8")),
        "num_linked_pages": 0,
        "num_headings": 0,
        "sample_links_alive": 0,
        "sample_links_dead": 0,
        "validation_score": None,
        "is_stub": False,
    }

    # Count headings
    headings = re.findall(r"^#{1,6}\s+\S", content, re.MULTILINE)
    result["num_headings"] = len(headings)

    # Extract linked pages
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
    result["num_linked_pages"] = len(links)

    # Stub detection — only flag truly empty/placeholder files
    if result["size_bytes"] < 1024 and len(headings) == 0:
        result["is_stub"] = True
    elif result["size_bytes"] < 500:
        # Very small files with placeholder-like content
        if re.search(r"^\s*#?\s*(TODO|placeholder|coming soon)\s*$", content, re.IGNORECASE | re.MULTILINE):
            result["is_stub"] = True

    # Check if content is actually text/markdown (not HTML)
    scraper = _get_llms_scraper()
    if scraper:
        is_valid, reason = scraper.is_valid_text_content(content.encode("utf-8"))
        if not is_valid:
            result["is_stub"] = True
            result["validation_score"] = 0
            return result

    # Sample link validation (HEAD requests, max 10)
    link_urls = [u for _, u in links if u.startswith("http")]
    sample = link_urls[:10]
    if sample:
        with ThreadPoolExecutor(max_workers=10) as pool:
            futures = {pool.submit(_head, u, 3.0): u for u in sample}
            for fut in as_completed(futures):
                status = fut.result()
                if 200 <= status < 400:
                    result["sample_links_alive"] += 1
                else:
                    result["sample_links_dead"] += 1

    # Validation score using validate-markdown (write temp file)
    validator = _get_validator()
    if validator:
        try:
            tmp = Path(tempfile.mktemp(suffix=".md"))
            tmp.write_text(content, encoding="utf-8")
            # analyze_file needs a docs_root; create a minimal structure
            fake_root = tmp.parent
            quality = validator.analyze_file(tmp, fake_root)
            if quality:
                result["validation_score"] = quality.overall_score
            tmp.unlink(missing_ok=True)
        except Exception:
            pass

    return result


def probe_llms_txt(domain: str) -> list[dict]:
    """Probe all candidate llms.txt URLs for a domain."""
    urls = _build_probe_urls(domain)
    results = []

    # Parallel HEAD probe first
    status_map: dict[str, int] = {}
    with ThreadPoolExecutor(max_workers=20) as pool:
        futures = {pool.submit(_head, u, 5.0): u for u in urls}
        for fut in as_completed(futures):
            url = futures[fut]
            status = fut.result()
            status_map[url] = status

    # For URLs that returned 200, download and assess
    found_urls = [u for u, s in status_map.items() if 200 <= s < 300]

    for url in found_urls:
        resp = _get(url, timeout=30.0)
        if resp is None:
            continue
        content = resp.text.strip()
        if not content:
            # Server returned 200 but empty body
            results.append({"url": url, "http_status": 200, "size_bytes": 0, "is_stub": True})
            continue
        assessment = _assess_llms_txt_content(url, content)
        results.append(assessment)

    # Also record non-200 results for common paths (just top-level)
    for url in urls:
        if url not in [r["url"] for r in results]:
            status = status_map.get(url, 0)
            if status > 0:  # Only include if we got a response
                results.append({"url": url, "http_status": status})

    return results


# ---------------------------------------------------------------------------
# Assess GitHub candidates
# ---------------------------------------------------------------------------

def _github_api_get(path: str, timeout: float = 10.0) -> Optional[dict]:
    """Call GitHub API, trying gh CLI first, falling back to authenticated requests.

    Authentication priority:
      1. gh CLI (uses its own auth)
      2. Direct HTTP with GH_TOKEN (set by _ensure_github_token at startup)
      3. Unauthenticated (60 req/hr — last resort)
    """
    # Try gh cli first
    meta_json = _run_cmd(["gh", "api", path], timeout=int(timeout))
    if meta_json:
        try:
            return json.loads(meta_json)
        except json.JSONDecodeError:
            pass

    # Fallback: direct HTTP with auth token if available
    headers = {"Accept": "application/vnd.github.v3+json"}
    token = os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"
    try:
        r = SESSION.get(f"https://api.github.com/{path}", timeout=timeout,
                        headers=headers)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return None


def assess_github(owner_repo: str) -> Optional[dict]:
    """Assess a GitHub repository as a documentation source."""
    result = {
        "repo": owner_repo,
        "stars": 0,
        "last_push": None,
        "is_fork": False,
        "is_archived": False,
        "docs_folder": None,
        "docs_file_count": 0,
        "docs_total_size": "0B",
        "has_markdown": False,
    }

    # Get repo metadata
    meta = _github_api_get(f"repos/{owner_repo}")
    if not meta:
        return None

    result["stars"] = meta.get("stargazers_count", 0)
    pushed = meta.get("pushed_at", "")
    result["last_push"] = pushed[:10] if pushed else None
    result["is_fork"] = meta.get("fork", False)
    result["is_archived"] = meta.get("archived", False)
    default_branch = meta.get("default_branch", "main")

    # Check for docs folder — try common paths
    docs_candidates = ["docs", "doc", "documentation", "docs/en/docs", "website/docs"]
    for folder in docs_candidates:
        contents = _github_api_get(f"repos/{owner_repo}/contents/{folder}")
        if contents and isinstance(contents, list) and len(contents) > 0:
            result["docs_folder"] = folder

            # Get recursive tree for accurate file counts and sizes
            tree_data = _github_api_get(
                f"repos/{owner_repo}/git/trees/{default_branch}?recursive=1"
            )
            if tree_data and "tree" in tree_data:
                doc_files = [
                    entry for entry in tree_data["tree"]
                    if entry.get("path", "").startswith(f"{folder}/")
                    and re.search(r"\.(md|mdx|rst|txt)$", entry.get("path", ""))
                ]
                result["docs_file_count"] = len(doc_files)
                result["has_markdown"] = len(doc_files) > 0

                total_bytes = sum(entry.get("size", 0) for entry in doc_files)
                result["docs_total_size"] = _format_size(total_bytes)

            break  # Found a docs folder, stop looking

    return result


# ---------------------------------------------------------------------------
# Decision logic
# ---------------------------------------------------------------------------

def decide(probe_output: dict) -> dict:
    """Decide which documentation source to use based on probe results.

    Applies rules in priority order:
      1. llms-txt with valid content (not stub, >5KB, score>=75)
      2. Language-specific doc hosts (docs.rs, pkg.go.dev) + GitHub homepage
      3. GitHub repo with substantial docs (>5 files, has markdown, not fork)
      4. LLM-guided URL selection via MiniMax-M2.5
      5. Skip if nothing viable

    Returns: {"source": "llms-txt"|"github"|"web"|"skip", "url": "...", "reason": "..."}
    """
    _log("decide: evaluating rules...")

    # --- Rule 0: doc_index hit + Tavily grounding ---
    index_hits = probe_output.get("discovery", {}).get("doc_index")
    if index_hits:
        # Prefer html/llms-txt over cheatsheets/api-specs
        type_priority = {"llms-txt": 0, "html": 1, "api-spec": 2, "cheatsheet": 3}
        best_hit = min(index_hits, key=lambda h: type_priority.get(
            h.get("doc_type", "html"), 99))
        doc_url = best_hit["doc_url"]
        platform = best_hit["platform"]
        doc_type = best_hit.get("doc_type", "html")

        # Tavily grounding check: if Tavily ran, verify the index domain
        # appears in search results. If Tavily disagrees, fall through to other rules.
        tavily = probe_output.get("discovery", {}).get("tavily_search", {})
        tavily_available = tavily.get("available", False)
        index_domain = urlparse(doc_url).netloc.lower() if doc_url else ""

        tavily_confirms = False
        if tavily_available and index_domain:
            for sr in tavily.get("search_results", []):
                sr_domain = urlparse(sr.get("url", "")).netloc.lower()
                if sr_domain == index_domain or sr_domain.endswith("." + index_domain) or index_domain.endswith("." + sr_domain):
                    tavily_confirms = True
                    break
        _log(f"decide: Rule 0 — index_hit={platform}/{doc_type}, url={doc_url}, "
             f"tavily_available={tavily_available}, tavily_confirms={tavily_confirms}")

        # Use index hit if: Tavily confirms, OR Tavily unavailable (trust index)
        if tavily_confirms or not tavily_available:
            # Map doc_type to auto_doc source type
            if doc_type == "llms-txt":
                source = "llms-txt"
            elif doc_type == "api-spec":
                source = "web"
            else:
                source = "web"
            grounding = "tavily-confirmed" if tavily_confirms else "no-tavily"
            return {
                "source": source,
                "url": doc_url,
                "reason": f"doc-index: {platform} ({doc_type}) [{grounding}]",
            }
        # Tavily available but disagrees — fall through to other rules
        _log(f"decide: Rule 0 — tavily disagrees with index domain '{index_domain}', falling through")

    # --- Rule 1: llms-txt ---
    # Build set of domains that are relevant to this library
    library = probe_output.get("library", "").lower()
    lib_clean = library.replace("-", "").replace("_", "")
    discovery = probe_output.get("discovery", {})
    best_guess = discovery.get("best_guess", {})
    best_domain = best_guess.get("domain", "")

    # A domain is relevant if it's from a registry (strong signal),
    # matches best_guess backed by a registry or name match, or contains
    # the library name as a domain segment
    relevant_domains: set[str] = set()

    # Registry domains are trusted (PyPI, npm, crates.io verified ownership)
    registries = discovery.get("registries", {})
    has_registry = len(registries) > 0
    for reg_info in registries.values():
        if reg_info.get("domain"):
            relevant_domains.add(reg_info["domain"])
    # GitHub search: only add homepage from the best-guess repo, not all candidates
    best_github = best_guess.get("github", "")
    if best_github:
        for c in discovery.get("github_search", {}).get("candidates", []):
            if c.get("full_name") == best_github:
                hp = c.get("homepage", "")
                if hp:
                    host = urlparse(hp).netloc
                    if host and host not in NOISE_DOMAINS:
                        relevant_domains.add(host)
                break

    # Add best_guess domain only if backed by registry or already in relevant set
    # (prevents trusting garbage discovery for nonexistent libraries)
    if best_domain and (best_domain in relevant_domains or has_registry):
        relevant_domains.add(best_domain)

    def _is_relevant_llms_domain(url: str) -> bool:
        """Check if an llms-txt URL is from a domain relevant to this library."""
        host = urlparse(url).netloc.lower()
        # Exact match with a known relevant domain
        if host in relevant_domains:
            return True
        # Any relevant domain is a suffix (e.g. docs.fastapi.tiangolo.com matches fastapi.tiangolo.com)
        for rd in relevant_domains:
            if host.endswith("." + rd) or rd.endswith("." + host):
                return True
        # Check if the library name appears as a dot-separated domain segment
        # e.g., "fastapi.tiangolo.com" has segment "fastapi" matching library "fastapi"
        # but "fastapi-mcp.tadata.com" has segment "fastapi-mcp" which does NOT match
        dot_parts = host.split(".")
        if library and library in dot_parts:
            return True
        # For multi-word libs like "drizzle-orm", check if all key parts appear as
        # dot-separated segments: "orm.drizzle.team" -> ["orm", "drizzle", "team"]
        lib_parts = re.split(r"[\-_]", library)
        if len(lib_parts) > 1 and all(p in dot_parts for p in lib_parts):
            return True
        return False

    viable_llms = []
    for r in probe_output.get("llms_txt", []):
        if (
            r.get("http_status") == 200
            and not r.get("is_stub", True)
            and r.get("size_bytes", 0) > 5120
            and _is_relevant_llms_domain(r.get("url", ""))
        ):
            score = r.get("validation_score")
            if score is None or score >= 75:
                viable_llms.append(r)

    _log(f"decide: Rule 1 — {len(viable_llms)} viable llms-txt files from {len(probe_output.get('llms_txt', []))} probed")
    if viable_llms:
        # Pick best: highest validation_score first, then largest size
        def _llms_sort_key(r):
            score = r.get("validation_score")
            # Treat None as -1 so entries with actual scores win ties
            return (score if score is not None else -1, r.get("size_bytes", 0))

        best = max(viable_llms, key=_llms_sort_key)
        url = best["url"]
        domain = urlparse(url).netloc
        size_kb = best.get("size_bytes", 0) / 1024
        score = best.get("validation_score", "n/a")
        headings = best.get("num_headings", 0)
        # Derive the filename from the URL path
        path_tail = urlparse(url).path.rstrip("/").rsplit("/", 1)[-1] or "llms.txt"
        return {
            "source": "llms-txt",
            "url": url,
            "reason": f"{path_tail} at {domain}: {size_kb:.0f}KB, score {score}, {headings} headings",
        }

    # --- Rule 2: Language-specific doc hosts (NEW) ---
    # Deterministic checks based on which registry found the library.

    # 2a: crates.io → docs.rs always exists for published crates
    if "crates.io" in registries and registries["crates.io"].get("found"):
        crate_name = library  # crate name matches library name
        docs_rs_url = f"https://docs.rs/{crate_name}/latest/{crate_name}/"
        return {
            "source": "web",
            "url": docs_rs_url,
            "reason": f"docs.rs/{crate_name}: crates.io crate has auto-generated docs",
        }

    # 2b: Elixir/Erlang hex.pm → hexdocs.pm
    if "hex" in registries or any(
        c.get("language", "").lower() in ("elixir", "erlang")
        for c in discovery.get("github_search", {}).get("candidates", [])
        if c.get("full_name") == best_github
    ):
        hex_url = f"https://hexdocs.pm/{library}"
        if 200 <= _head(hex_url) < 400:
            return {
                "source": "web",
                "url": hex_url,
                "reason": f"hexdocs.pm/{library}: Elixir/Erlang package docs",
            }

    # 2c: Perl CPAN → metacpan.org
    if any(
        c.get("language", "").lower() == "perl"
        for c in discovery.get("github_search", {}).get("candidates", [])
        if c.get("full_name") == best_github
    ):
        cpan_name = library.replace("-", "::")
        metacpan_url = f"https://metacpan.org/pod/{cpan_name}"
        if 200 <= _head(metacpan_url) < 400:
            return {
                "source": "web",
                "url": metacpan_url,
                "reason": f"metacpan.org/{cpan_name}: Perl CPAN module docs",
            }

    # 2d: Go module → pkg.go.dev
    if best_github:
        for c in discovery.get("github_search", {}).get("candidates", []):
            if c.get("full_name") == best_github and c.get("language", "").lower() == "go":
                pkg_url = f"https://pkg.go.dev/{best_github}"
                return {
                    "source": "web",
                    "url": pkg_url,
                    "reason": f"pkg.go.dev/{best_github}: Go module auto-docs",
                }

    # 2c: GitHub repo homepage field → often points to docs site
    if best_github:
        for c in discovery.get("github_search", {}).get("candidates", []):
            if c.get("full_name") == best_github:
                homepage = c.get("homepage", "")
                if homepage:
                    hp_host = urlparse(homepage).netloc
                    if hp_host and hp_host not in NOISE_DOMAINS:
                        status = _head(homepage)
                        if 200 <= status < 400:
                            return {
                                "source": "web",
                                "url": homepage,
                                "reason": f"GitHub repo homepage: {homepage} (HTTP {status})",
                            }
                break

    # --- Rule 3: GitHub with substantial docs (unchanged) ---
    # Only consider the best_guess repo (from discovery scoring).
    # Never pick a random repo that happens to have docs — that's how
    # we end up with GinSkeleton instead of gin-gonic/gin.
    if best_github:
        for gh in probe_output.get("github_candidates", []):
            if (
                gh["repo"] == best_github
                and gh.get("docs_file_count", 0) > 5
                and gh.get("has_markdown", False)
                and not gh.get("is_fork", True)
            ):
                repo = gh["repo"]
                count = gh["docs_file_count"]
                folder = gh.get("docs_folder", "docs")
                return {
                    "source": "github",
                    "url": repo,
                    "reason": f"github {repo}: {count} doc files in {folder}/",
                }

    # --- Rule 4: LLM-guided URL selection (NEW) ---
    # Pass the full discovery context to MiniMax-M2.5 to pick the best docs URL.
    import shutil
    _log("decide: Rules 1-3 didn't match, trying Rule 4 (LLM-guided)")
    if shutil.which("clauded-mm"):
        # Build discovery data summary for the prompt
        _github_candidates = discovery.get("github_search", {}).get("candidates", [])[:5]
        gh_summary_lines = []
        for c in _github_candidates:
            stars = c.get("stargazers_count", c.get("stars", 0))
            lang = c.get("language", "unknown")
            hp = c.get("homepage", "")
            gh_summary_lines.append(
                f"  - {c.get('full_name', '?')} ({stars} stars, {lang})"
                + (f" homepage: {hp}" if hp else "")
            )
        gh_summary = "\n".join(gh_summary_lines) if gh_summary_lines else "  (none)"

        tavily = discovery.get("tavily_search", {})
        tavily_results = (tavily.get("search_results") or [])[:10]
        tavily_summary_lines = []
        for sr in tavily_results:
            title = sr.get("title", "")[:80]
            url = sr.get("url", "")
            tavily_summary_lines.append(f"  - {title}: {url}")
        tavily_summary = "\n".join(tavily_summary_lines) if tavily_summary_lines else "  (none)"
        tavily_answer = tavily.get("answer") or "(none)"

        reg_names = [k for k, v in registries.items() if v.get("found")]
        reg_summary = ", ".join(reg_names) if reg_names else "(none)"

        # Unified index matches
        unified_data = discovery.get("unified_index", {})
        unified_lines = []
        for m in (unified_data.get("matches") or [])[:5]:
            dl = m.get("downloads") or 0
            unified_lines.append(
                f"  - [{m.get('registry', '?')}] {m.get('name', '?')}: "
                f"{m.get('docs_url', '?')} (downloads: {dl:,})"
            )
        unified_summary = "\n".join(unified_lines) if unified_lines else "  (none)"

        # Enumerated domain matches
        enum_domains = discovery.get("enumerated_domains", {})
        enum_lines = []
        for m in (enum_domains.get("matches") or [])[:5]:
            enum_lines.append(f"  - {m.get('platform', '?')}: {m.get('url', '?')}")
        enum_summary = "\n".join(enum_lines) if enum_lines else "  (none)"

        # Stack V2 data (if available from probe)
        stack_v2 = probe_output.get("stack_v2", {})
        stack_lines = []
        for p in (stack_v2.get("platforms") or [])[:5]:
            stack_lines.append(f"  - {p.get('platform', '?')}: {p.get('matched_files', '?')}")
        stack_summary = "\n".join(stack_lines) if stack_lines else "  (none)"

        llm_prompt = f"""Given these discovery results for the library "{library}", pick the single
best URL to fetch documentation from.

Consider:
- Name collisions: "{library}" may refer to different projects in different
  ecosystems. Use the registry data and GitHub stars to determine which
  project the user most likely means.
- Language-specific canonical doc hosts (always prefer these when applicable):
  * Rust: docs.rs/CRATE (always exists for published crates)
  * Go: pkg.go.dev/MODULE-PATH (always exists for Go modules)
  * Elixir/Erlang: hexdocs.pm/PACKAGE (always exists on hex.pm)
  * Dart/Flutter: pub.dev/documentation/PACKAGE/latest/
  * Perl: metacpan.org/pod/MODULE-NAME
  * Haskell: hackage.haskell.org/package/NAME/docs/
  * Ruby: rubydoc.info/gems/GEM
  * Java/Scala: javadoc.io/doc/GROUP-ID/ARTIFACT-ID/
  * OCaml: ocaml.org/p/PACKAGE/VERSION/doc/
  * R: cran.r-project.org/web/packages/PKG/
- GitHub Pages: the repo homepage field often points to a docs site.
- ReadTheDocs: many Python projects host docs on readthedocs.io.
- Separate doc repos: some projects host docs in a different repo
  (e.g., pact-foundation/docs.pact.io, kubernetes/website).
- Mirror sites: chromium.googlesource.com, code mirrors, etc.
  are NOT primary sources. Avoid them.
- Prefer official documentation over third-party tutorials or blog posts.

DISCOVERY DATA:
Library: {library}
Registries found in: {reg_summary}
Best guess domain: {best_domain or "(none)"}
Best guess GitHub: {best_github or "(none)"}

Top GitHub candidates:
{gh_summary}

Unified index matches (5.14M packages / 53 registries):
{unified_summary}

Enumerated doc domains:
{enum_summary}

Stack V2 doc platforms:
{stack_summary}

Tavily answer: {tavily_answer}

Top Tavily search results:
{tavily_summary}

Respond with ONLY valid JSON:
{{"url": "https://...", "reason": "one sentence explanation"}}

If no good documentation URL can be determined, respond with:
{{"url": "", "reason": "explanation of why no URL was found"}}"""

        try:
            result = subprocess.run(
                ["clauded-mm", "-p"],
                input=llm_prompt, capture_output=True, text=True, timeout=60,
            )
        except (subprocess.TimeoutExpired, Exception):
            result = None

        if result and result.returncode == 0 and result.stdout.strip():
            stdout = result.stdout.strip()
            parsed = None
            try:
                parsed = json.loads(stdout)
            except json.JSONDecodeError:
                # Try to find JSON object in the output
                match = re.search(r'\{[^{}]*"url"\s*:', stdout)
                if match:
                    json_start = match.start()
                    brace_depth = 0
                    for i in range(json_start, len(stdout)):
                        if stdout[i] == '{':
                            brace_depth += 1
                        elif stdout[i] == '}':
                            brace_depth -= 1
                            if brace_depth == 0:
                                try:
                                    parsed = json.loads(stdout[json_start:i + 1])
                                except json.JSONDecodeError:
                                    pass
                                break

            if (
                isinstance(parsed, dict)
                and parsed.get("url")
                and parsed["url"].startswith("http")
            ):
                return {
                    "source": "web",
                    "url": parsed["url"],
                    "reason": parsed.get("reason", "MiniMax-M2.5 selected URL"),
                }
        # LLM failed or returned invalid — fall through to skip

    # --- Rule 5: Skip ---
    return {
        "source": "skip",
        "url": "",
        "reason": "no viable sources found",
    }


# ---------------------------------------------------------------------------
# probe command
# ---------------------------------------------------------------------------

@app.command()
def probe(
    library: str = typer.Argument(help="Library name to probe"),
    domain: Optional[str] = typer.Option(None, help="Skip discovery, use this domain"),
    github: Optional[str] = typer.Option(None, help="Skip discovery, use this GitHub repo (owner/repo)"),
    json_output: bool = typer.Option(False, "--json", help="Output structured JSON to stdout"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable debug logging"),
):
    """Discover, probe, and assess all documentation sources for a library."""
    global _VERBOSE
    if verbose:
        _VERBOSE = True

    output: dict = {
        "library": library,
        "already_exists": False,
        "existing_paths": [],
        "configured_in": [],
        "official_site": None,
        "discovery": {},
        "llms_txt": [],
        "github_candidates": [],
        "recommendation": "needs_decision",
    }

    # Step 1: Check existing
    existing = check_existing(library)
    output["already_exists"] = existing["already_exists"]
    output["existing_paths"] = existing["existing_paths"]
    output["configured_in"] = existing["configured_in"]

    if not json_output and existing["already_exists"]:
        typer.echo(f"Library '{library}' already exists:", err=True)
        for p in existing["existing_paths"]:
            typer.echo(f"  {p}", err=True)

    # Step 2: Discover — collect ALL sources in parallel
    discovered_domain = domain
    discovered_github = github

    if not domain or not github:
        if not json_output:
            typer.echo(f"Discovering sources for '{library}'...", err=True)

        discovery = discover(library)
        output["discovery"] = discovery
        best = discovery.get("best_guess", {})
        discovered_domain = domain or best.get("domain")
        discovered_github = github or best.get("github")

    if discovered_domain:
        output["official_site"] = f"https://{discovered_domain}"

    # Step 3: Probe llms.txt on ALL discovered domains (not just the best guess)
    domains_to_probe = set()
    if discovered_domain:
        domains_to_probe.add(discovered_domain)

    # Also probe domains from ALL discovery sources
    if not domain:  # Only if we ran discovery
        disc = output.get("discovery", {})
        for reg_info in disc.get("registries", {}).values():
            if reg_info.get("domain"):
                domains_to_probe.add(reg_info["domain"])
        # Extract domains from tavily results — only those that appear 2+ times
        # (single mentions are likely pages that reference the library, not its docs)
        tavily_domain_counts: dict[str, int] = {}
        lib_lower = library.lower().replace("-", "").replace("_", "")
        for sr in disc.get("tavily_search", {}).get("search_results", []):
            host = urlparse(sr.get("url", "")).netloc
            if host and host not in NOISE_DOMAINS:
                tavily_domain_counts[host] = tavily_domain_counts.get(host, 0) + 1
        for host, count in tavily_domain_counts.items():
            # Include if: appears 2+ times, OR domain contains the library name
            host_clean = host.lower().replace("-", "").replace(".", "")
            if count >= 2 or lib_lower in host_clean:
                domains_to_probe.add(host)
        if disc.get("github_search", {}).get("domain"):
            domains_to_probe.add(disc["github_search"]["domain"])
        # GitHub search candidate homepages
        for c in disc.get("github_search", {}).get("candidates", []):
            hp = c.get("homepage", "")
            if hp:
                host = urlparse(hp).netloc
                if host and host not in NOISE_DOMAINS:
                    domains_to_probe.add(host)
        if disc.get("domain_guess", {}).get("domain"):
            domains_to_probe.add(disc["domain_guess"]["domain"])
        # Unified index domains
        if disc.get("unified_index", {}).get("domain"):
            domains_to_probe.add(disc["unified_index"]["domain"])
        # Enumerated domain matches
        for m in disc.get("enumerated_domains", {}).get("matches", [])[:3]:
            d = m.get("domain", "")
            if d:
                domains_to_probe.add(d)

    # Cap domains to probe — each domain generates ~20 HTTP calls
    if len(domains_to_probe) > 10:
        # Keep the best_guess domain and limit the rest
        priority = discovered_domain or ""
        others = sorted(domains_to_probe - {priority})[:9]
        domains_to_probe = ({priority} if priority else set()) | set(others)

    if domains_to_probe:
        if not json_output:
            typer.echo(f"Probing llms.txt at {len(domains_to_probe)} domain(s)...", err=True)
        all_llms_results = []
        for d in domains_to_probe:
            all_llms_results.extend(probe_llms_txt(d))
        # Deduplicate: by URL, then collapse identical content across domains
        seen_urls: set[str] = set()
        seen_content: dict[tuple[int, int], str] = {}  # fingerprint -> first URL
        deduped = []
        for r in all_llms_results:
            if r["url"] in seen_urls:
                continue
            seen_urls.add(r["url"])
            # For 200 responses, deduplicate by size+headings fingerprint
            if r.get("http_status") == 200 and r.get("size_bytes", 0) > 0:
                fingerprint = (r.get("size_bytes", 0), r.get("num_headings", -1))
                if fingerprint in seen_content:
                    # Skip — identical content already captured at another URL
                    continue
                seen_content[fingerprint] = r["url"]
            deduped.append(r)
        # Also skip non-200s for domains we already have 200 results from
        domains_with_200 = {urlparse(r["url"]).netloc for r in deduped if r.get("http_status") == 200}
        deduped = [
            r for r in deduped
            if r.get("http_status") == 200 or urlparse(r["url"]).netloc not in domains_with_200
        ]
        output["llms_txt"] = deduped

    # Step 4: Assess GitHub — assess ALL candidates from search, not just best guess
    github_repos_to_assess = set()
    if discovered_github:
        github_repos_to_assess.add(discovered_github)

    if not github:  # Only if we ran discovery
        disc = output.get("discovery", {})
        for c in disc.get("github_search", {}).get("candidates", []):
            if c.get("full_name") and not c.get("fork"):
                github_repos_to_assess.add(c["full_name"])
        # Also from tavily
        if disc.get("tavily_search", {}).get("github"):
            github_repos_to_assess.add(disc["tavily_search"]["github"])

    if github_repos_to_assess:
        if not json_output:
            typer.echo(f"Assessing {len(github_repos_to_assess)} GitHub repo(s)...", err=True)
        gh_results = []
        # Assess in parallel
        with ThreadPoolExecutor(max_workers=min(5, len(github_repos_to_assess))) as pool:
            futures = {pool.submit(assess_github, repo): repo for repo in github_repos_to_assess}
            for fut in as_completed(futures):
                result = fut.result()
                if result:
                    gh_results.append(result)
        # Sort by stars descending
        gh_results.sort(key=lambda x: x.get("stars", 0), reverse=True)
        output["github_candidates"] = gh_results

    # Step 4b: Enrich with Stack V2 doc-platform signals
    if discovered_github:
        stack_v2 = _enrich_stack_v2(discovered_github)
        if stack_v2.get("found"):
            output["stack_v2"] = stack_v2

    # Step 5: Determine recommendation
    has_good_llms = any(
        r.get("http_status") == 200
        and not r.get("is_stub", True)
        and r.get("size_bytes", 0) > 2048
        for r in output["llms_txt"]
    )
    has_github_docs = any(
        r.get("docs_file_count", 0) > 5 for r in output["github_candidates"]
    )

    if existing["already_exists"]:
        output["recommendation"] = "already_exists"
    elif has_good_llms and has_github_docs:
        output["recommendation"] = "needs_decision"
    elif has_good_llms:
        output["recommendation"] = "use_llms_txt"
    elif has_github_docs:
        output["recommendation"] = "use_github"
    elif not discovered_domain and not discovered_github:
        output["recommendation"] = "nothing_found"
    else:
        output["recommendation"] = "nothing_found"

    # Output
    if json_output:
        typer.echo(json.dumps(output, indent=2))
    else:
        _print_probe_report(output)

    # Return output for programmatic use
    return output


def _print_probe_report(output: dict):
    """Print a human-readable probe report to stderr."""
    w = typer.echo

    w(f"\n{'=' * 60}")
    w(f"  Probe Report: {output['library']}")
    w(f"{'=' * 60}")

    if output["already_exists"]:
        w(f"\n  Status: ALREADY EXISTS")
        for p in output["existing_paths"]:
            w(f"    {p}")

    if output["official_site"]:
        w(f"\n  Official site: {output['official_site']}")

    # Discovery summary
    disc = output.get("discovery", {})
    if disc:
        registries = disc.get("registries", {})
        if registries:
            names = ", ".join(registries.keys())
            w(f"\n  Found in registries: {names}")

        tavily = disc.get("tavily_search", {})
        if tavily.get("search_results"):
            w(f"  Tavily search: {len(tavily['search_results'])} results")
            if tavily.get("answer"):
                w(f"    Answer: {tavily['answer'][:120]}")
            for sr in tavily["search_results"][:3]:
                w(f"    {sr.get('title', '?')[:60]} — {sr['url']}")

        gh_search = disc.get("github_search", {})
        if gh_search.get("candidates"):
            w(f"  GitHub search: {len(gh_search['candidates'])} candidates")
            for c in gh_search["candidates"][:3]:
                w(f"    {c['full_name']} ({c['stars']:,} stars) — {c.get('language', '?')}")

        guess = disc.get("domain_guess", {})
        alive_guesses = [p for p in guess.get("probed", []) if 200 <= p.get("status", 0) < 400]
        if alive_guesses:
            w(f"  Domain guesses alive: {', '.join(p['domain'] for p in alive_guesses)}")

    # llms.txt results
    found_llms = [r for r in output["llms_txt"] if r.get("http_status") == 200]
    not_found = [r for r in output["llms_txt"] if r.get("http_status") != 200]

    if found_llms:
        w(f"\n  llms.txt found ({len(found_llms)}):")
        for r in found_llms:
            size = r.get("size_bytes", 0)
            size_str = f"{size / 1024:.1f}KB" if size >= 1024 else f"{size}B"
            stub = " [STUB]" if r.get("is_stub") else ""
            links = r.get("num_linked_pages", 0)
            score = r.get("validation_score", "?")
            alive = r.get("sample_links_alive", 0)
            dead = r.get("sample_links_dead", 0)
            w(f"    {r['url']}")
            w(f"      Size: {size_str} | Pages: {links} | Headings: {r.get('num_headings', 0)} | Score: {score}{stub}")
            if alive or dead:
                w(f"      Links: {alive} alive, {dead} dead")

    if not_found:
        w(f"\n  llms.txt not found ({len(not_found)} URLs checked)")

    # GitHub results
    for gh in output.get("github_candidates", []):
        w(f"\n  GitHub: {gh['repo']}")
        w(f"    Stars: {gh['stars']:,} | Last push: {gh.get('last_push', '?')}")
        w(f"    Fork: {gh['is_fork']} | Archived: {gh['is_archived']}")
        if gh.get("docs_folder"):
            w(f"    Docs folder: {gh['docs_folder']} ({gh['docs_file_count']} files, {gh['docs_total_size']})")
        else:
            w(f"    Docs folder: not found")

    # Recommendation
    rec = output["recommendation"]
    w(f"\n  Recommendation: {rec}")
    w(f"{'=' * 60}\n")


# ---------------------------------------------------------------------------
# fetch command
# ---------------------------------------------------------------------------

@app.command()
def fetch(
    library: str = typer.Argument(help="Library name"),
    source: str = typer.Option(..., help="Source type: llms-txt or github"),
    url: str = typer.Option(..., help="URL to fetch from (llms.txt URL or GitHub repo)"),
    force: bool = typer.Option(False, help="Force re-download even if recent"),
    json_output: bool = typer.Option(False, "--json", help="Output JSON"),
):
    """Download documentation from a chosen source."""

    result = {"library": library, "source": source, "url": url, "success": False}

    if source == "llms-txt":
        result = _fetch_llms_txt(library, url, force)
    elif source == "github":
        result = _fetch_github(library, url, force)
    else:
        typer.echo(f"Unknown source: {source}. Use 'llms-txt' or 'github'.", err=True)
        raise typer.Exit(2)

    # Update index
    try:
        updater = _get_index_updater()
        if updater:
            updater.main()
    except Exception:
        pass

    if json_output:
        typer.echo(json.dumps(result, indent=2))
    else:
        if result.get("success"):
            typer.echo(f"Fetched {library} from {source} successfully.")
            if result.get("file_count") is not None:
                typer.echo(f"  Files: {result['file_count']}")
            if result.get("output_dir"):
                typer.echo(f"  Output: {result['output_dir']}")
        else:
            typer.echo(f"Failed to fetch {library}: {result.get('error', 'unknown')}", err=True)
            raise typer.Exit(2)


def _fetch_llms_txt(library: str, url: str, force: bool) -> dict:
    """Fetch documentation via llms.txt."""
    result = {"library": library, "source": "llms-txt", "url": url, "success": False}

    # Determine base_url from the llms.txt URL
    parsed = urlparse(url)
    # Base URL is everything up to the last path component
    path_parts = parsed.path.rsplit("/", 1)
    base_path = path_parts[0] + "/" if len(path_parts) > 1 else "/"
    base_url = f"{parsed.scheme}://{parsed.netloc}{base_path}"

    # Add to llms-sites.yaml if not already there
    _ensure_llms_site_config(library, base_url)

    # Create output directory
    output_dir = DOCS_DIR / "llms-txt" / library
    output_dir.mkdir(parents=True, exist_ok=True)

    scraper = _get_llms_scraper()
    if not scraper:
        result["error"] = "llms-txt-scraper.py not found"
        return result

    # Use the scraper's process_site function
    site_config = {
        "name": library,
        "base_url": base_url,
        "description": f"{library} documentation",
        "rate_limit_seconds": 0,
    }

    try:
        # Redirect stdout to stderr during scraper call — the scraper prints
        # progress to stdout which corrupts JSON output from the CLI.
        _saved_stdout = sys.stdout
        sys.stdout = sys.stderr
        try:
            stats = scraper.process_site(site_config, mode="both", force=force)
        finally:
            sys.stdout = _saved_stdout
        individual = stats.get("individual_success", 0)
        full = 1 if stats.get("full_success") else 0
        result["success"] = individual > 0 or full > 0
        result["file_count"] = individual + full
        result["output_dir"] = str(output_dir.relative_to(REPO_ROOT))
    except Exception as e:
        result["error"] = str(e)

    # Fallback: if scraper found nothing, directly download the specific URL
    # that probe found (scraper may have tried different paths)
    if not result["success"]:
        try:
            resp = _get(url, timeout=30.0)
            if resp and len(resp.text.strip()) > 500:
                # Save as {library}-full.md
                filename = f"{library}-full.md"
                filepath = output_dir / filename
                filepath.write_text(resp.text, encoding="utf-8")
                result["success"] = True
                result["file_count"] = 1
                result["output_dir"] = str(output_dir.relative_to(REPO_ROOT))
                result["error"] = None
        except Exception:
            pass

    return result


def _find_docs_folder_local(repo_path: Path) -> Optional[str]:
    """Scan a cloned repo for common docs folders."""
    candidates = ["docs", "doc", "documentation", "docs/en/docs", "website/docs"]
    for folder in candidates:
        candidate_path = repo_path / folder
        if candidate_path.is_dir():
            # Check it actually has doc files
            doc_files = list(candidate_path.rglob("*.md")) + list(candidate_path.rglob("*.mdx")) + \
                        list(candidate_path.rglob("*.rst")) + list(candidate_path.rglob("*.txt"))
            if doc_files:
                return folder
    return None



def _fetch_github(library: str, repo: str, force: bool) -> dict:
    """Fetch documentation from a GitHub repository."""
    result = {"library": library, "source": "github", "url": repo, "success": False}

    # Parse owner/repo
    if "/" not in repo:
        result["error"] = f"Invalid repo format: {repo}. Expected owner/repo."
        return result

    output_dir = DOCS_DIR / "github-scraped" / library
    output_dir.mkdir(parents=True, exist_ok=True)

    # Try to find docs folder via API first (fast, no clone needed)
    docs_folder = None
    gh_info = assess_github(repo)
    if gh_info and gh_info.get("docs_folder"):
        docs_folder = gh_info["docs_folder"]

    clone_url = f"https://github.com/{repo}.git"

    # Shallow clone and extract
    import shutil
    try:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp) / "repo"
            subprocess.run(
                ["git", "clone", "--depth", "1", "--single-branch", clone_url, str(tmp_path)],
                capture_output=True, text=True, timeout=300, check=True,
            )

            # If API didn't find docs folder (e.g. rate limited), scan locally
            if not docs_folder:
                docs_folder = _find_docs_folder_local(tmp_path)
                if not docs_folder:
                    result["error"] = f"No docs folder found in {repo}"
                    return result


            source_path = tmp_path / docs_folder
            if not source_path.exists():
                result["error"] = f"Docs folder '{docs_folder}' not found in clone"
                return result

            # Add to repo_config.yaml (after we confirmed docs_folder exists)
            _ensure_repo_config(library, clone_url, docs_folder, str(output_dir.relative_to(REPO_ROOT)))

            # Copy docs
            if output_dir.exists() and force:
                shutil.rmtree(output_dir)
                output_dir.mkdir(parents=True, exist_ok=True)

            file_count = 0
            for src_file in source_path.rglob("*"):
                if src_file.is_file() and src_file.suffix in (".md", ".mdx", ".rst"):
                    rel = src_file.relative_to(source_path)
                    dst = output_dir / rel
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_file, dst)
                    file_count += 1

            result["success"] = True
            result["file_count"] = file_count
            result["docs_folder"] = docs_folder
            result["output_dir"] = str(output_dir.relative_to(REPO_ROOT))

    except subprocess.TimeoutExpired:
        result["error"] = "Git clone timed out (300s)"
    except subprocess.CalledProcessError as e:
        result["error"] = f"Git clone failed: {e.stderr[:200]}"
    except Exception as e:
        result["error"] = str(e)

    return result


def _ensure_llms_site_config(name: str, base_url: str):
    """Add a site to llms-sites.yaml if not already present."""
    config = {"sites": []}
    if LLMS_SITES_YAML.exists():
        with open(LLMS_SITES_YAML) as f:
            config = yaml.safe_load(f) or {"sites": []}

    sites = config.get("sites", [])
    if any(s.get("name") == name for s in sites):
        return

    sites.append({
        "name": name,
        "base_url": base_url,
        "description": f"{name} documentation",
    })
    config["sites"] = sites

    with open(LLMS_SITES_YAML, "w") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def _ensure_repo_config(name: str, repo_url: str, source_folder: str, target_folder: str):
    """Add a repo to repo_config.yaml if not already present."""
    config = {"settings": {"overwrite_existing": True, "clone_timeout": 300, "temp_dir_base": None}, "repositories": []}
    if REPO_CONFIG_YAML.exists():
        with open(REPO_CONFIG_YAML) as f:
            config = yaml.safe_load(f) or config

    repos = config.get("repositories", [])
    if any(r.get("name") == name for r in repos):
        return

    repos.append({
        "name": name,
        "description": f"{name} from GitHub",
        "repo_url": repo_url,
        "source_folder": source_folder,
        "target_folder": target_folder,
        "branch": "main",
    })
    config["repositories"] = repos

    with open(REPO_CONFIG_YAML, "w") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


# ---------------------------------------------------------------------------
# validate command
# ---------------------------------------------------------------------------

@app.command()
def validate(
    path: Optional[str] = typer.Argument(None, help="Specific path to validate (default: all docs)"),
    source: Optional[str] = typer.Option(None, help="Filter by source: llms-txt, github-scraped, web-scraped"),
    max_score: int = typer.Option(100, help="Only show files at or below this score"),
    min_score: int = typer.Option(0, help="Only show files at or above this score"),
    json_output: bool = typer.Option(False, "--json", help="Output JSON"),
    fix_report: bool = typer.Option(False, "--fix-report", help="Generate fix recommendations"),
    limit: int = typer.Option(0, help="Limit output to N files per category"),
):
    """Validate markdown quality across the docs repository."""
    validator = _get_validator()
    if not validator:
        typer.echo("Error: validate-markdown.py not found", err=True)
        raise typer.Exit(2)

    docs_root = DOCS_DIR
    if path:
        search_path = Path(path)
        if not search_path.is_absolute():
            search_path = REPO_ROOT / path
    elif source:
        search_path = docs_root / source
    else:
        search_path = docs_root

    if not search_path.exists():
        typer.echo(f"Path not found: {search_path}", err=True)
        raise typer.Exit(2)

    md_files = list(search_path.rglob("*.md"))
    typer.echo(f"Scanning {len(md_files)} markdown files...", err=True)

    results = []
    for p in md_files:
        quality = validator.analyze_file(p, docs_root)
        if quality and min_score <= quality.overall_score <= max_score:
            results.append(quality)

    results.sort(key=lambda x: (x.overall_score, x.path))

    if json_output:
        from dataclasses import asdict
        output = {
            "total_files": len(md_files),
            "analyzed_files": len(results),
            "files": [asdict(r) for r in results],
        }
        typer.echo(json.dumps(output, indent=2))
    else:
        # Summary
        typer.echo(f"\nScanned: {len(md_files)} files, {len(results)} in score range [{min_score}-{max_score}]")

        if results:
            avg = sum(r.overall_score for r in results) / len(results)
            typer.echo(f"Average score: {avg:.1f}")

        display_limit = limit or 50
        for r in results[:display_limit]:
            issues = ", ".join(r.issues) if r.issues else "ok"
            typer.echo(f"  [{r.overall_score:>3}] {r.path}  ({issues})")

        if len(results) > display_limit:
            typer.echo(f"  ... and {len(results) - display_limit} more")


# ---------------------------------------------------------------------------
# status command
# ---------------------------------------------------------------------------

@app.command()
def status(
    json_output: bool = typer.Option(False, "--json", help="Output JSON"),
):
    """Report current repository documentation status."""
    result = {
        "docs_dir": str(DOCS_DIR),
        "sources": {},
        "total_libraries": 0,
        "total_files": 0,
        "total_size_bytes": 0,
    }

    for source_name in ["llms-txt", "github-scraped", "web-scraped"]:
        source_dir = DOCS_DIR / source_name
        if not source_dir.exists():
            result["sources"][source_name] = {"libraries": 0, "files": 0, "size_bytes": 0}
            continue

        libraries = [d for d in source_dir.iterdir() if d.is_dir()]
        files = list(source_dir.rglob("*.md"))
        size = sum(f.stat().st_size for f in files if f.exists())

        result["sources"][source_name] = {
            "libraries": len(libraries),
            "files": len(files),
            "size_bytes": size,
            "size_human": _format_size(size),
        }
        result["total_libraries"] += len(libraries)
        result["total_files"] += len(files)
        result["total_size_bytes"] += size

    result["total_size_human"] = _format_size(result["total_size_bytes"])

    # Config counts
    if LLMS_SITES_YAML.exists():
        with open(LLMS_SITES_YAML) as f:
            cfg = yaml.safe_load(f) or {}
        result["llms_sites_configured"] = len(cfg.get("sites", []))

    if REPO_CONFIG_YAML.exists():
        with open(REPO_CONFIG_YAML) as f:
            cfg = yaml.safe_load(f) or {}
        result["repos_configured"] = len(cfg.get("repositories", []))

    if json_output:
        typer.echo(json.dumps(result, indent=2))
    else:
        typer.echo(f"\n{'=' * 50}")
        typer.echo(f"  llm-code-docs Status")
        typer.echo(f"{'=' * 50}")
        typer.echo(f"\n  Total: {result['total_libraries']} libraries, {result['total_files']} files, {result['total_size_human']}")
        for src, info in result["sources"].items():
            typer.echo(f"  {src}: {info['libraries']} libraries, {info['files']} files, {info.get('size_human', '0B')}")
        if "llms_sites_configured" in result:
            typer.echo(f"\n  Configured: {result.get('llms_sites_configured', 0)} llms-txt sites, {result.get('repos_configured', 0)} GitHub repos")
        typer.echo(f"{'=' * 50}\n")


# ---------------------------------------------------------------------------
# trckr integration
# ---------------------------------------------------------------------------

DOCS_PROJECT_ID = "0e5104bf-8740-4115-9d70-5036b76186b3"


def trckr_get_next_ticket(project_id: str = DOCS_PROJECT_ID) -> Optional[dict]:
    """Get the next todo ticket from a trckr project. Returns {identifier, title, library_name} or None."""
    data = None
    for priority in ("urgent", "high", "medium", "low"):
        stdout = _run_cmd(
            ["trckr", "issue", "list", "--status", "todo", "--project-id", project_id,
             "--priority", priority, "--sort", "created", "--desc", "--limit", "1"],
            timeout=15,
        )
        if stdout:
            try:
                data = json.loads(stdout)
            except (json.JSONDecodeError, TypeError):
                continue
            if data.get("issues"):
                break
    else:
        stdout = _run_cmd(
            ["trckr", "issue", "list", "--status", "todo", "--project-id", project_id,
             "--sort", "created", "--desc", "--limit", "1"],
            timeout=15,
        )
        if not stdout:
            return None
        try:
            data = json.loads(stdout)
        except (json.JSONDecodeError, TypeError):
            return None

    if not data:
        return None

    issues = data.get("issues", [])
    if not issues:
        return None

    issue = issues[0]
    identifier = issue.get("identifier", "")
    title = issue.get("title", "")
    library_name = _extract_library_name(title)

    return {
        "identifier": identifier,
        "title": title,
        "library_name": library_name,
    }


def trckr_update_ticket(identifier: str, status: str, comment: str):
    """Update a trckr ticket's status and add a comment."""
    _run_cmd(
        ["trckr", "issue", "update", identifier, "--status", status],
        timeout=15,
    )
    _run_cmd(
        ["trckr", "comment", "add", "--issue", identifier, "--body", comment, "--author", "auto-doc"],
        timeout=15,
    )


def _extract_library_name(title: str) -> str:
    """Extract library name from ticket title like 'Add docs for fastapi' or just 'fastapi'."""
    prefixes = [
        "Add docs for ",
        "Add documentation for ",
        "Documentation for ",
        "Add ",
        "Docs for ",
    ]
    result = title
    for prefix in prefixes:
        if result.lower().startswith(prefix.lower()):
            result = result[len(prefix):]
            break
    # Strip trailing qualifiers like " docs"
    suffixes = [" docs", " documentation"]
    for suffix in suffixes:
        if result.lower().endswith(suffix.lower()):
            result = result[: -len(suffix)]
            break
    result = re.sub(r"\s+", "-", result)
    return result.strip().lower()


# ---------------------------------------------------------------------------
# Markdownlint cleanup
# ---------------------------------------------------------------------------

# Rules disabled by project convention (not auto-fixed):
#   MD013 - line length
#   MD033 - inline HTML
#   MD034 - bare URLs
#   MD055 - table pipe style
#   MD056 - table body row count
#   MD059 - table column count
#   MD060 - table header delimiter
_MARKDOWNLINT_DISABLED_RULES = [
    "MD013", "MD033", "MD034", "MD055", "MD056", "MD059", "MD060",
]

_MARKDOWNLINT_BATCH_SIZE = 50


def cleanup_markdownlint(docs_dir: Path) -> dict:
    """Run markdownlint --fix on all markdown files in *docs_dir*.

    Processes files in batches to avoid command-line length limits.
    Returns a summary dict::

        {
            "files_checked": int,
            "files_with_issues": int,
            "issues_fixed": int,
            "errors": [],
        }
    """
    result: dict = {
        "files_checked": 0,
        "files_with_issues": 0,
        "issues_fixed": 0,
        "errors": [],
    }

    # Collect all .md files
    md_files = sorted(docs_dir.rglob("*.md"))
    if not md_files:
        return result

    result["files_checked"] = len(md_files)

    # Build the shared flags
    disable_flags: list[str] = ["--disable"] + _MARKDOWNLINT_DISABLED_RULES

    files_with_issues: set[str] = set()
    total_issues = 0

    # Process in batches
    for i in range(0, len(md_files), _MARKDOWNLINT_BATCH_SIZE):
        batch = md_files[i : i + _MARKDOWNLINT_BATCH_SIZE]
        cmd = ["npx", "markdownlint", "--fix"] + [str(f) for f in batch] + disable_flags

        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60,
            )
        except FileNotFoundError:
            result["errors"].append("npx not found - install Node.js and npx to use markdownlint")
            return result
        except subprocess.TimeoutExpired:
            result["errors"].append(f"markdownlint timed out on batch starting at index {i}")
            continue
        except Exception as exc:
            result["errors"].append(f"unexpected error: {exc}")
            continue

        # markdownlint exits non-zero when it finds (and fixes) issues.
        # Output lines look like: "path/file.md:10 MD010/no-hard-tabs ..."
        # or "path/file.md:10:5 MD010/no-hard-tabs ..."
        output = (proc.stdout or "") + (proc.stderr or "")
        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue
            # Match pattern: filepath:line or filepath:line:col followed by rule
            match = re.match(r"^(.+?):(\d+)(:\d+)?\s+(MD\d+)", line)
            if match:
                files_with_issues.add(match.group(1))
                total_issues += 1

    result["files_with_issues"] = len(files_with_issues)
    result["issues_fixed"] = total_issues

    return result


def review_content(library: str, docs_dir: Path) -> dict:
    """Review fetched documentation content using MiniMax-M2.5 via clauded-mm.

    Reads markdown files from docs_dir, samples up to 10 (prioritizing largest),
    and asks MiniMax-M2.5 to evaluate identity, substance, encoding, duplication,
    coverage, and completeness.

    Returns: {"pass": bool, "issues": [...], "files_to_delete": [...], "summary": "..."}
    On any failure: returns a failing result with the reason.
    """
    fail_result = lambda reason: {
        "pass": False,
        "issues": [f"review failed: {reason}"],
        "files_to_delete": [],
        "summary": f"MiniMax-M2.5 review failed: {reason}",
    }

    # Collect markdown files
    if not docs_dir.exists() or not docs_dir.is_dir():
        return fail_result(f"docs_dir does not exist: {docs_dir}")

    md_files = sorted(
        [f for ext in ("*.md", "*.mdx", "*.rst") for f in docs_dir.rglob(ext)],
        key=lambda f: f.stat().st_size, reverse=True,
    )
    if not md_files:
        return fail_result("no markdown files found")

    # Sample up to 10 files, prioritizing largest
    sampled = md_files[:10]

    # Build file listing (name + size)
    file_listing = []
    for f in sampled:
        size = f.stat().st_size
        rel = f.relative_to(docs_dir)
        file_listing.append(f"  {rel} ({_format_size(size)})")

    # Content samples from the 3 largest files (first 2000 chars each)
    content_samples = []
    for f in sampled[:3]:
        try:
            text = f.read_text(encoding="utf-8", errors="replace")[:2000]
        except Exception as e:
            text = f"<error reading file: {e}>"
        rel = f.relative_to(docs_dir)
        content_samples.append(f"--- {rel} ---\n{text}\n--- end ---")

    prompt = f"""You are reviewing fetched documentation files for the library "{library}".

FILE LISTING ({len(sampled)} files sampled from {len(md_files)} total):
{chr(10).join(file_listing)}

CONTENT SAMPLES (3 largest files, first 2000 chars each):
{chr(10).join(content_samples)}

Evaluate these docs on the following criteria:
1. Identity: Is this actually documentation for "{library}"? (not a different library or project)
2. Substance: Is this real documentation content, or boilerplate/nav cruft/cookie banners/placeholder text?
3. Encoding: Any mojibake, unconverted HTML entities, or garbled text?
4. Duplication: Are there near-identical files that should be deduplicated?
5. Coverage: Does this doc set make sense for a library like "{library}"?
6. Completeness: Are there obvious gaps or broken cross-references?

Respond with ONLY valid JSON matching this exact schema:
{{
  "pass": true/false,
  "issues": ["list of specific issues found, empty if none"],
  "files_to_delete": ["relative paths of files that should be removed (duplicates, cruft, wrong library)"],
  "summary": "one-sentence overall assessment"
}}

Set "pass" to true if the docs are usable (minor issues are OK). Set "pass" to false if there are serious problems (wrong library, mostly cruft, severe encoding issues).
"""

    # Check if clauded-mm is available
    import shutil
    if not shutil.which("clauded-mm"):
        return fail_result("clauded-mm not found in PATH")

    # Call MiniMax-M2.5 via subprocess
    try:
        result = subprocess.run(
            ["clauded-mm", "-p"],
            input=prompt, capture_output=True, text=True, timeout=300,
        )
    except subprocess.TimeoutExpired:
        return fail_result("clauded-mm timed out after 300s")
    except Exception as e:
        return fail_result(f"clauded-mm execution error: {e}")

    if result.returncode != 0:
        stderr_snippet = (result.stderr or "")[:200]
        return fail_result(f"clauded-mm returned exit code {result.returncode}: {stderr_snippet}")

    # Parse JSON response
    stdout = result.stdout.strip()
    if not stdout:
        return fail_result("clauded-mm returned empty output")

    # Try to extract JSON from the output (may have non-JSON preamble)
    try:
        parsed = json.loads(stdout)
    except json.JSONDecodeError:
        # Try to find JSON object in the output
        match = re.search(r'\{[^{}]*"pass"\s*:', stdout)
        if match:
            # Find the matching closing brace
            json_start = match.start()
            brace_depth = 0
            for i in range(json_start, len(stdout)):
                if stdout[i] == '{':
                    brace_depth += 1
                elif stdout[i] == '}':
                    brace_depth -= 1
                    if brace_depth == 0:
                        try:
                            parsed = json.loads(stdout[json_start:i + 1])
                            break
                        except json.JSONDecodeError:
                            pass
            else:
                return fail_result(f"could not parse JSON from clauded-mm output: {stdout[:200]}")
        else:
            return fail_result(f"could not parse JSON from clauded-mm output: {stdout[:200]}")

    # Validate expected schema fields
    if not isinstance(parsed, dict) or "pass" not in parsed:
        return fail_result(f"clauded-mm response missing 'pass' field: {stdout[:200]}")

    return {
        "pass": bool(parsed.get("pass", False)),
        "issues": list(parsed.get("issues", [])),
        "files_to_delete": list(parsed.get("files_to_delete", [])),
        "summary": str(parsed.get("summary", "")),
    }

# ---------------------------------------------------------------------------
# Web scraping via Jina Reader
# ---------------------------------------------------------------------------

def _slugify_url_path(url: str) -> str:
    """Convert a URL path into a filesystem-safe filename slug.

    Examples:
        https://example.com/docs/getting-started/ -> getting-started
        https://example.com/docs/api/v2/auth     -> api-v2-auth
        https://example.com/                      -> index
    """
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        return "index"
    # Replace path separators and non-alphanumeric chars with hyphens
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", path).strip("-")
    # Collapse multiple hyphens
    slug = re.sub(r"-{2,}", "-", slug)
    # Truncate to a reasonable length for filenames
    if len(slug) > 120:
        slug = slug[:120].rsplit("-", 1)[0]
    return slug or "index"


def _extract_links_from_markdown(markdown_text: str, docs_prefix: str) -> list[str]:
    """Extract all links from markdown that match the docs path prefix.

    Finds markdown links [text](url) and bare URLs that start with docs_prefix.
    Returns deduplicated list preserving discovery order.
    """
    # Match markdown links: [text](url) and bare URLs
    link_pattern = re.compile(
        r"\[(?:[^\]]*)\]\((https?://[^)]+)\)"  # [text](url)
        r"|"
        r"(?<!\()(https?://\S+)"                # bare URLs
    )
    seen = set()
    links = []
    for match in link_pattern.finditer(markdown_text):
        url = match.group(1) or match.group(2)
        # Strip trailing punctuation that isn't part of the URL
        url = url.rstrip(".,;:!?)")
        # Strip fragment identifiers
        url = url.split("#")[0]
        if not url:
            continue
        if url.startswith(docs_prefix) and url not in seen:
            seen.add(url)
            links.append(url)
    return links


def fetch_via_jina(library: str, docs_url: str) -> dict:
    """Fetch documentation pages via Jina Reader and save as markdown.

    1. Fetches the docs index page via https://r.jina.ai/{docs_url}
    2. Extracts all links matching the docs path prefix
    3. Fetches each linked page (up to 100) via Jina Reader
    4. Saves each page as a markdown file in docs/web-scraped/{library}/

    Rate limit: 0.5s between requests (well under Jina free tier 20 RPM).
    Timeout: 30s per page request.

    Returns: {"success": bool, "scraper_path": None, "output_dir": str,
              "file_count": int, "error": str|None}
    """
    output_dir = str(DOCS_DIR / "web-scraped" / library)
    output_path = Path(output_dir)
    result = {
        "success": False,
        "scraper_path": None,
        "output_dir": output_dir,
        "file_count": 0,
        "error": None,
    }

    MAX_PAGES = 100
    MIN_CONTENT_BYTES = 500
    REQUEST_TIMEOUT = 30
    RATE_LIMIT_DELAY = 3.5  # Jina free tier: 20 RPM, stay safely under

    jina_headers = {
        "User-Agent": "auto-doc/1.0 (llm-code-docs pipeline)",
        "Accept": "text/markdown",
    }

    # Normalize the docs URL prefix for link matching
    # e.g. https://example.com/docs/ -> match all links under /docs/
    parsed_docs = urlparse(docs_url)
    docs_prefix = f"{parsed_docs.scheme}://{parsed_docs.netloc}{parsed_docs.path}"
    if not docs_prefix.endswith("/"):
        # Go up one level for prefix matching if URL points to a file
        docs_prefix = docs_prefix.rsplit("/", 1)[0] + "/"

    # Step 1: Fetch the index page via Jina Reader
    jina_index_url = f"https://r.jina.ai/{docs_url}"
    try:
        r = SESSION.get(jina_index_url, headers=jina_headers, timeout=REQUEST_TIMEOUT)
        if r.status_code != 200:
            result["error"] = f"Jina Reader returned {r.status_code} for index page {docs_url}"
            return result
        index_markdown = r.text
    except requests.exceptions.Timeout:
        result["error"] = f"Timeout fetching index page via Jina Reader: {docs_url}"
        return result
    except Exception as e:
        result["error"] = f"Failed to fetch index page via Jina Reader: {e}"
        return result

    if len(index_markdown.encode("utf-8")) < MIN_CONTENT_BYTES:
        result["error"] = f"Index page too small ({len(index_markdown.encode('utf-8'))} bytes): {docs_url}"
        return result

    # Step 2: Extract links matching the docs prefix
    links = _extract_links_from_markdown(index_markdown, docs_prefix)

    # If few links found, try to discover a docs subpath.
    # Common pattern: domain root has links to /docs/, /en/docs/, /documentation/, etc.
    if len(links) < 10:
        # Extract ALL links from the page, find common docs-like subpaths
        all_page_links = re.findall(r'\[([^\]]*)\]\((https?://[^)]+)\)', index_markdown)
        base_host = parsed_docs.netloc
        doc_path_candidates: dict[str, int] = {}
        for _, url in all_page_links:
            p = urlparse(url)
            if p.netloc == base_host and p.path:
                # Find path segments that look like docs roots
                parts = p.path.strip("/").split("/")
                for i, part in enumerate(parts):
                    if part in ("docs", "documentation", "guide", "guides", "api", "reference"):
                        candidate = f"{p.scheme}://{p.netloc}/{'/'.join(parts[:i+1])}/"
                        doc_path_candidates[candidate] = doc_path_candidates.get(candidate, 0) + 1
                        break
        # Pick the docs subpath with the most links
        if doc_path_candidates:
            best_subpath = max(doc_path_candidates, key=doc_path_candidates.get)
            if doc_path_candidates[best_subpath] >= 2:
                # Re-fetch the docs subpath index to get real doc links
                sub_jina_url = f"https://r.jina.ai/{best_subpath}"
                try:
                    time.sleep(RATE_LIMIT_DELAY)
                    sub_resp = SESSION.get(sub_jina_url, headers=jina_headers, timeout=REQUEST_TIMEOUT)
                    if sub_resp.status_code == 200:
                        sub_links = _extract_links_from_markdown(sub_resp.text, best_subpath)
                        if len(sub_links) > len(links):
                            links = sub_links
                            docs_prefix = best_subpath
                            docs_url = best_subpath
                except Exception:
                    pass  # Fall back to original links

    # Always include the index page itself
    all_urls = [docs_url] + [l for l in links if l != docs_url]
    all_urls = all_urls[:MAX_PAGES]

    print(f"  Jina Reader: found {len(links)} doc links, will fetch {len(all_urls)} pages (including index)", file=sys.stderr)

    # Step 3: Create output directory
    output_path.mkdir(parents=True, exist_ok=True)

    # Step 4: Fetch each page and save as markdown
    saved_count = 0
    errors = []

    for i, page_url in enumerate(all_urls):
        if i > 0:
            time.sleep(RATE_LIMIT_DELAY)

        slug = _slugify_url_path(page_url)
        filename = f"{slug}.md"
        filepath = output_path / filename

        # Avoid overwriting: append a numeric suffix if needed
        counter = 1
        while filepath.exists():
            filepath = output_path / f"{slug}-{counter}.md"
            counter += 1

        jina_page_url = f"https://r.jina.ai/{page_url}"
        try:
            # Retry on 429 (rate limit) with exponential backoff
            r = None
            for attempt in range(3):
                r = SESSION.get(jina_page_url, headers=jina_headers, timeout=REQUEST_TIMEOUT)
                if r.status_code == 429:
                    wait = RATE_LIMIT_DELAY * (2 ** attempt)
                    print(f"  [{i+1}/{len(all_urls)}] 429 rate limited, waiting {wait:.0f}s...", file=sys.stderr)
                    time.sleep(wait)
                    continue
                break
            if r.status_code != 200:
                errors.append(f"HTTP {r.status_code} for {page_url}")
                print(f"  [{i+1}/{len(all_urls)}] SKIP {page_url} (HTTP {r.status_code})", file=sys.stderr)
                continue

            page_markdown = r.text
            content_size = len(page_markdown.encode("utf-8"))
            if content_size < MIN_CONTENT_BYTES:
                errors.append(f"Too small ({content_size}b) for {page_url}")
                print(f"  [{i+1}/{len(all_urls)}] SKIP {page_url} (too small: {content_size}b)", file=sys.stderr)
                continue

            # Write with source header
            full_content = f"# Source: {page_url}\n\n{page_markdown}"
            filepath.write_text(full_content, encoding="utf-8")
            saved_count += 1
            print(f"  [{i+1}/{len(all_urls)}] OK   {page_url} -> {filepath.name} ({content_size}b)", file=sys.stderr)

        except requests.exceptions.Timeout:
            errors.append(f"Timeout for {page_url}")
            print(f"  [{i+1}/{len(all_urls)}] SKIP {page_url} (timeout)", file=sys.stderr)
            continue
        except Exception as e:
            errors.append(f"Error for {page_url}: {e}")
            print(f"  [{i+1}/{len(all_urls)}] SKIP {page_url} ({e})", file=sys.stderr)
            continue

    # Step 5: Validate results
    if saved_count == 0:
        result["error"] = f"No pages saved. Errors: {'; '.join(errors[:5])}"
        return result

    result["success"] = True
    result["file_count"] = saved_count
    if errors:
        print(f"  Jina Reader: {saved_count} pages saved, {len(errors)} skipped", file=sys.stderr)
    else:
        print(f"  Jina Reader: {saved_count} pages saved successfully", file=sys.stderr)
    return result


def _format_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f}KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f}MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f}GB"


# ---------------------------------------------------------------------------
# add command – full pipeline for a single library
# ---------------------------------------------------------------------------

def _git_commit_and_push(library: str, source: str, docs_dir: Path) -> dict:
    """Stage docs, commit, and push to origin.

    Returns: {"commit_sha": str|None, "error": str|None}
    """
    result: dict = {"commit_sha": None, "error": None}

    # Stage the docs directory
    rel_docs = str(docs_dir.relative_to(REPO_ROOT))
    stage_cmd = ["git", "add", rel_docs]

    # Also stage config changes (llms-sites.yaml, repo_config.yaml)
    config_files = ["scripts/llms-sites.yaml", "scripts/repo_config.yaml"]

    proc = subprocess.run(stage_cmd, capture_output=True, text=True, timeout=30,
                          cwd=str(REPO_ROOT))
    if proc.returncode != 0:
        result["error"] = f"git add failed: {proc.stderr[:200]}"
        return result

    for cf in config_files:
        cf_path = REPO_ROOT / cf
        if cf_path.exists():
            subprocess.run(["git", "add", cf], capture_output=True, text=True,
                           timeout=10, cwd=str(REPO_ROOT))

    # Check if there's anything to commit
    status_proc = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        capture_output=True, text=True, timeout=10, cwd=str(REPO_ROOT),
    )
    if status_proc.returncode == 0:
        result["error"] = "nothing to commit (no changes staged)"
        return result

    # Commit
    msg = f"Add {library} docs via {source}\n\nCo-Authored-By: auto-doc pipeline"
    commit_proc = subprocess.run(
        ["git", "commit", "-m", msg],
        capture_output=True, text=True, timeout=30, cwd=str(REPO_ROOT),
    )
    if commit_proc.returncode != 0:
        result["error"] = f"git commit failed: {commit_proc.stderr[:200]}"
        return result

    # Get commit SHA
    sha_proc = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True, text=True, timeout=10, cwd=str(REPO_ROOT),
    )
    if sha_proc.returncode == 0:
        result["commit_sha"] = sha_proc.stdout.strip()

    # Push
    push_proc = subprocess.run(
        ["git", "push"],
        capture_output=True, text=True, timeout=60, cwd=str(REPO_ROOT),
    )
    if push_proc.returncode != 0:
        # Non-fatal — commit succeeded but push failed
        result["error"] = f"push failed (commit saved locally): {push_proc.stderr[:200]}"

    return result


def _count_files_in_dir(docs_dir: Path) -> int:
    """Count markdown files in a directory."""
    if not docs_dir.exists():
        return 0
    return len(list(docs_dir.rglob("*.md")))


def _invoke_probe(library: str) -> dict:
    """Invoke the probe command via CliRunner and return parsed JSON output.

    Since probe is a typer @app.command(), calling it directly as a Python
    function results in typer OptionInfo objects instead of real values.
    We use CliRunner to invoke it properly through the CLI layer.

    Returns parsed probe output dict.
    Raises RuntimeError if probe fails or returns invalid JSON.
    """
    from typer.testing import CliRunner as _CliRunner
    _runner = _CliRunner()
    # Pass --verbose if active so probe logs during its execution.
    # _log() uses os.write to the real fd 2, bypassing CliRunner's capture.
    args = ["probe", library, "--json"]
    if _VERBOSE:
        args.append("--verbose")
    probe_result = _runner.invoke(app, args)
    if probe_result.exit_code != 0:
        raise RuntimeError(f"probe failed: {probe_result.output[:300]}")
    try:
        return json.loads(probe_result.output)
    except json.JSONDecodeError:
        raise RuntimeError(f"probe returned invalid JSON: {probe_result.output[:300]}")


def add_library(
    library: str,
    dry_run: bool = False,
    no_commit: bool = False,
) -> dict:
    """Orchestrate the full add pipeline for a single library.

    Steps: probe → decide → fetch/scrape → markdownlint → LLM review → git commit+push

    Returns structured result dict.
    """
    result: dict = {
        "library": library,
        "source_used": None,
        "files_added": 0,
        "quality_score": None,
        "commit_sha": None,
        "success": False,
        "error": None,
    }

    # Step 1: Probe
    _log(f"add_library: Step 1 — probing '{library}'")
    try:
        probe_output = _invoke_probe(library)
    except (RuntimeError, Exception) as e:
        _log(f"add_library: probe failed — {e}")
        result["error"] = str(e)
        return result

    # Check if already exists
    if probe_output.get("already_exists"):
        _log(f"add_library: '{library}' already exists")
        result["success"] = True
        result["source_used"] = "already_exists"
        result["error"] = None
        return result

    # Step 2: Decide
    _log(f"add_library: Step 2 — deciding source")
    decision = decide(probe_output)
    source = decision.get("source", "skip")
    url = decision.get("url", "")
    reason = decision.get("reason", "")
    _log(f"add_library: decision — source={source}, url={url}, reason={reason}")

    result["source_used"] = source

    if source == "skip":
        result["error"] = f"no viable documentation source found: {reason}"
        return result

    # Dry run stops here
    if dry_run:
        result["success"] = True
        result["error"] = None
        return result

    # Step 3: Fetch or scrape
    _log(f"add_library: Step 3 — fetching via {source}")
    fetch_result: dict = {}

    if source == "llms-txt":
        fetch_result = _fetch_llms_txt(library, url, force=False)
    elif source == "github":
        fetch_result = _fetch_github(library, url, force=False)
    elif source == "web":
        fetch_result = fetch_via_jina(library, url)
    else:
        result["error"] = f"unknown source type: {source}"
        return result

    if not fetch_result.get("success"):
        _log(f"add_library: fetch failed — {fetch_result.get('error', 'unknown')}")
        result["error"] = f"fetch failed ({source}): {fetch_result.get('error', 'unknown')}"
        return result

    result["files_added"] = fetch_result.get("file_count", 0)
    _log(f"add_library: fetched {result['files_added']} files")

    # Determine the docs directory
    if source == "llms-txt":
        docs_dir = DOCS_DIR / "llms-txt" / library
    elif source == "github":
        docs_dir = DOCS_DIR / "github-scraped" / library
    elif source == "web":
        docs_dir = DOCS_DIR / "web-scraped" / library
    else:
        docs_dir = DOCS_DIR / library

    # Step 4: Markdownlint cleanup
    _log(f"add_library: Step 4 — markdownlint cleanup in {docs_dir}")
    if docs_dir.exists():
        lint_result = cleanup_markdownlint(docs_dir)
        _log(f"add_library: markdownlint — {lint_result.get('files_checked', 0)} files, {lint_result.get('issues_fixed', 0)} issues fixed")

    # Step 5: LLM content review
    _log(f"add_library: Step 5 — LLM content review")
    review = review_content(library, docs_dir)
    _log(f"add_library: review result — pass={review.get('pass')}, summary={review.get('summary', '')[:100]}")
    if review.get("pass"):
        result["quality_score"] = "pass"
    else:
        # Delete files flagged by review
        for rel_path in review.get("files_to_delete", []):
            target = docs_dir / rel_path
            if target.exists():
                target.unlink()

        result["quality_score"] = "fail"
        issues = review.get("issues", [])
        summary = review.get("summary", "")
        result["error"] = f"content review failed: {summary}. Issues: {'; '.join(issues[:3])}"
        import shutil
        if docs_dir.exists():
            shutil.rmtree(docs_dir)
        subprocess.run(["git", "checkout", "--", "scripts/llms-sites.yaml", "scripts/repo_config.yaml"],
                       capture_output=True, cwd=str(REPO_ROOT), timeout=10)
        return result

    # Step 6: Git commit + push
    _log("add_library: Step 6 — git commit + push")
    if no_commit:
        result["success"] = True
        return result

    git_result = _git_commit_and_push(library, source, docs_dir)
    result["commit_sha"] = git_result.get("commit_sha")

    if git_result.get("error") and not git_result.get("commit_sha"):
        # Commit itself failed
        result["error"] = git_result["error"]
        return result

    result["success"] = True
    return result


@app.command()
def add(
    library: str = typer.Argument(help="Library name to add documentation for"),
    json_output: bool = typer.Option(False, "--json", help="Output structured JSON"),
    no_commit: bool = typer.Option(False, "--no-commit", help="Skip git commit and push"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Probe and decide only, don't fetch or commit"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable debug logging"),
):
    """Add documentation for a library: probe, decide, fetch, clean, review, commit."""
    global _VERBOSE
    if verbose:
        _VERBOSE = True
    result = add_library(library, dry_run=dry_run, no_commit=no_commit)

    if json_output:
        typer.echo(json.dumps(result, indent=2))
    else:
        if result["success"]:
            typer.echo(f"Successfully added docs for '{library}'")
            if result["source_used"]:
                typer.echo(f"  Source: {result['source_used']}")
            if result["files_added"]:
                typer.echo(f"  Files: {result['files_added']}")
            if result["commit_sha"]:
                typer.echo(f"  Commit: {result['commit_sha'][:12]}")
            if dry_run:
                typer.echo(f"  (dry run — no files fetched or committed)")
        else:
            typer.echo(f"Failed to add docs for '{library}': {result.get('error', 'unknown')}", err=True)

    if not result["success"]:
        raise typer.Exit(1)


# ---------------------------------------------------------------------------
# Plow: batch mode — process tickets from the DOCS queue
# ---------------------------------------------------------------------------

def plow_batch(
    limit: int = 0,
    dry_run: bool = False,
    project_id: str = DOCS_PROJECT_ID,
) -> dict:
    """Process documentation tickets from a trckr project queue.

    Pulls todo tickets one at a time, extracts the library name, runs
    add_library(), and updates the ticket status based on the result.

    Args:
        limit: Maximum tickets to process (0 = unlimited).
        dry_run: If True, probe+decide only — don't fetch or commit.
        project_id: trckr project UUID to pull tickets from.

    Returns:
        Summary dict with processed/succeeded/failed counts and per-ticket details.
    """
    summary: dict = {
        "processed": 0,
        "succeeded": 0,
        "failed": 0,
        "skipped": 0,
        "tickets": [],
        "stopped_reason": None,
    }

    while True:
        # Check limit
        if limit > 0 and summary["processed"] >= limit:
            summary["stopped_reason"] = f"reached --limit {limit}"
            break

        # Pull next todo ticket
        ticket = trckr_get_next_ticket(project_id)
        if ticket is None:
            summary["stopped_reason"] = "queue empty"
            break

        identifier = ticket["identifier"]
        library = ticket["library_name"]
        ticket_result: dict = {
            "identifier": identifier,
            "title": ticket["title"],
            "library": library,
            "success": False,
            "error": None,
            "source_used": None,
            "files_added": 0,
        }

        if not library:
            ticket_result["error"] = "could not extract library name from title"
            trckr_update_ticket(
                identifier, "in-review",
                f"auto-doc plow: could not extract library name from title '{ticket['title']}'",
            )
            summary["skipped"] += 1
            summary["processed"] += 1
            summary["tickets"].append(ticket_result)
            continue

        # Mark in-progress
        trckr_update_ticket(identifier, "in-progress", f"auto-doc plow: processing '{library}'")

        # Run add_library
        try:
            result = add_library(library, dry_run=dry_run)
        except Exception as e:
            result = {
                "library": library,
                "source_used": None,
                "files_added": 0,
                "quality_score": None,
                "commit_sha": None,
                "success": False,
                "error": str(e),
            }

        ticket_result["success"] = result.get("success", False)
        ticket_result["error"] = result.get("error")
        ticket_result["source_used"] = result.get("source_used")
        ticket_result["files_added"] = result.get("files_added", 0)

        # Update ticket based on result
        if result.get("success"):
            parts = [f"auto-doc plow: successfully added docs for '{library}'"]
            if result.get("source_used"):
                parts.append(f"Source: {result['source_used']}")
            if result.get("files_added"):
                parts.append(f"Files: {result['files_added']}")
            if result.get("commit_sha"):
                parts.append(f"Commit: {result['commit_sha'][:12]}")
            if dry_run:
                parts.append("(dry run — no files fetched)")
            comment = "\n".join(parts)
            trckr_update_ticket(identifier, "done", comment)
            summary["succeeded"] += 1
        else:
            error_msg = result.get("error", "unknown error")
            trckr_update_ticket(
                identifier, "in-review",
                f"auto-doc plow: failed to add docs for '{library}': {error_msg}",
            )
            summary["failed"] += 1

        summary["processed"] += 1
        summary["tickets"].append(ticket_result)

    return summary


@app.command()
def plow(
    limit: int = typer.Option(0, "--limit", help="Max tickets to process (0 = unlimited)"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Probe and decide only, don't fetch or commit"),
    project_id: str = typer.Option(DOCS_PROJECT_ID, "--project-id", help="trckr project UUID"),
    json_output: bool = typer.Option(False, "--json", help="Output structured JSON"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable debug logging"),
):
    """Batch-process documentation tickets from the DOCS project queue."""
    global _VERBOSE
    if verbose:
        _VERBOSE = True
    summary = plow_batch(limit=limit, dry_run=dry_run, project_id=project_id)

    if json_output:
        typer.echo(json.dumps(summary, indent=2))
    else:
        typer.echo(f"Plow complete: {summary['processed']} processed, "
                   f"{summary['succeeded']} succeeded, {summary['failed']} failed, "
                   f"{summary['skipped']} skipped")
        if summary["stopped_reason"]:
            typer.echo(f"Stopped: {summary['stopped_reason']}")

        for t in summary["tickets"]:
            status = "OK" if t["success"] else "FAIL"
            typer.echo(f"  [{status}] {t['identifier']} ({t['library']}): "
                       f"{t.get('source_used') or t.get('error', 'unknown')}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app()
