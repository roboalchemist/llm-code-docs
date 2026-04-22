#!/usr/bin/env python3
"""
llms.txt Scraper

Downloads llms.txt (and llms-full.txt) documentation from sites listed in
scripts/llms-sites.yaml. Output is written to docs/{site_name}/llms/.

After writing files, creates or updates docs/{site_name}/_meta.yaml with
primary_source: llms.

With --expand, parses page links from the llms.txt index and fetches each
individual page, saving them as separate .md files with # Source: headers.

Usage:
    python3 scripts/llms-txt-scraper.py                 # all sites
    python3 scripts/llms-txt-scraper.py --site dspy     # single site
    python3 scripts/llms-txt-scraper.py --dry-run       # dry run (no writes)
    python3 scripts/llms-txt-scraper.py --workers 8     # parallel workers
    python3 scripts/llms-txt-scraper.py --site shadcn-ui --expand  # fetch individual pages
    python3 scripts/llms-txt-scraper.py --expand --dry-run         # preview page expansion
"""

import argparse
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from concurrent.futures import ThreadPoolExecutor, as_completed

import yaml

try:
    from markdownify import markdownify as _markdownify
    _HAS_MARKDOWNIFY = True
except ImportError:
    _HAS_MARKDOWNIFY = False


SCRIPT_DIR = Path(__file__).resolve().parent
DOCS_ROOT = SCRIPT_DIR.parent / "docs"
SITES_FILE = SCRIPT_DIR / "llms-sites.yaml"

DEFAULT_TIMEOUT = 30
DEFAULT_WORKERS = 4
DEFAULT_RATE_LIMIT = 1.0  # seconds between requests per site

# Regex for markdown links in llms.txt index: - [Title](url): description
PAGE_LINK_RE = re.compile(r'-\s+\[([^\]]+)\]\((https?://[^)]+)\)')


def load_sites(sites_file: Path) -> list[dict]:
    """Load site list from llms-sites.yaml."""
    with open(sites_file) as f:
        data = yaml.safe_load(f)
    return data.get("sites", [])


def slugify_url_path(url: str) -> str:
    """Convert a URL path component to a safe filename."""
    parsed = urlparse(url)
    path = parsed.path.strip("/").replace("/", "-")
    if not path:
        path = parsed.netloc.replace(".", "-")
    # Remove unsafe characters
    path = re.sub(r"[^a-zA-Z0-9_\-.]", "-", path)
    path = re.sub(r"-+", "-", path).strip("-")
    return path or "index"


def fetch_url(url: str, timeout: int = DEFAULT_TIMEOUT) -> str | None:
    """Fetch a URL and return content as text, or None on failure."""
    req = Request(url, headers={"User-Agent": "llm-code-docs-scraper/1.0"})
    try:
        with urlopen(req, timeout=timeout) as resp:
            charset = "utf-8"
            content_type = resp.headers.get("Content-Type", "")
            if "charset=" in content_type:
                charset = content_type.split("charset=")[-1].strip().split(";")[0].strip()
            return resp.read().decode(charset, errors="replace")
    except HTTPError as e:
        print(f"    -> HTTP {e.code} fetching {url}")
        return None
    except URLError as e:
        print(f"    -> URLError fetching {url}: {e.reason}")
        return None
    except Exception as e:
        print(f"    -> Error fetching {url}: {e}")
        return None


def write_meta_yaml(site_dir: Path, site: dict, fetched_at: str, dry_run: bool = False) -> None:
    """Create or update docs/{site_name}/_meta.yaml with primary_source: llms."""
    meta_path = site_dir / "_meta.yaml"

    # Load existing meta if present
    existing = {}
    if meta_path.exists():
        try:
            with open(meta_path) as f:
                existing = yaml.safe_load(f) or {}
        except Exception:
            existing = {}

    # Build updated meta - preserve existing fields, update sources
    sources = existing.get("sources", [])

    # Update or insert the llms source entry
    llms_source = None
    for s in sources:
        if s.get("type") == "llms":
            llms_source = s
            break

    if llms_source is None:
        llms_source = {"type": "llms", "url": site["base_url"], "last_fetched": fetched_at}
        sources.append(llms_source)
    else:
        llms_source["url"] = site["base_url"]
        llms_source["last_fetched"] = fetched_at

    meta = {
        "name": existing.get("name", site["name"]),
        "primary_source": "llms",
        "sources": sources,
        "description": existing.get("description", site.get("description", "")),
        "quality_score": existing.get("quality_score", 0),
    }

    if dry_run:
        print(f"    [dry-run] Would write {meta_path}")
        return

    site_dir.mkdir(parents=True, exist_ok=True)
    with open(meta_path, "w") as f:
        yaml.dump(meta, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def url_to_slug(url: str) -> str:
    """Convert a URL path to a filename slug.

    Uses the last 2-3 path segments for uniqueness, cleaned of unsafe chars.
    """
    path = urlparse(url).path.strip("/")
    parts = path.split("/")
    slug_parts = parts[-3:] if len(parts) > 2 else parts
    slug = "-".join(slug_parts)
    slug = re.sub(r"[^a-zA-Z0-9_-]", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug[:120] or "index"


def is_html_response(content: str) -> bool:
    """Check if content looks like HTML rather than markdown/text."""
    first = content[:200].strip().lower()
    return first.startswith("<!doctype html") or first.startswith("<html")


def html_to_markdown(html: str, url: str, title: str = "") -> str | None:
    """Extract <article> content from a pre-rendered HTML page and convert to markdown.

    Returns None if no article content found or markdownify not installed.
    """
    if not _HAS_MARKDOWNIFY:
        return None

    m = re.search(r"<article[^>]*>(.*?)</article>", html, re.DOTALL)
    if not m:
        return None

    article_html = m.group(1)

    if not title:
        t = re.search(r"<title>([^<]+)</title>", html)
        if t:
            title = re.sub(r"\s*\|[^|]*$", "", t.group(1)).strip()

    md = _markdownify(article_html, heading_style="ATX", bullets="-", strip=["script", "style"])
    md = re.sub(r"\n{3,}", "\n\n", md).strip()

    header = f"<!-- Source: {url} -->\n\n"
    if title and not md.startswith("# "):
        header += f"# {title}\n\n"
    return header + md + "\n"


def parse_page_links(llms_txt_content: str) -> list[tuple[str, str]]:
    """Extract (title, url) pairs from llms.txt index content."""
    return PAGE_LINK_RE.findall(llms_txt_content)


def expand_site_pages(
    site: dict,
    output_dir: Path,
    rate_limit: float,
    dry_run: bool = False,
) -> dict:
    """Fetch individual pages linked from a site's llms.txt index.

    Reads the already-downloaded llms.txt, parses page links, and fetches each
    one as a separate .md file with a # Source: header.

    Returns a stats dict: {pages_fetched, pages_skipped, pages_failed, pages_html}.
    """
    name = site["name"]

    # Find the llms.txt file (prefer plain llms.txt over llms-full.txt for index parsing)
    llms_txt_path = output_dir / "llms.txt"
    if not llms_txt_path.exists():
        llms_txt_path = output_dir / f"{name}-llms.md"
    if not llms_txt_path.exists():
        print(f"    -> No llms.txt found for {name}, skipping expansion")
        return {"pages_fetched": 0, "pages_skipped": 0, "pages_failed": 0, "pages_html": 0}

    content = llms_txt_path.read_text(encoding="utf-8", errors="replace")
    links = parse_page_links(content)

    if not links:
        print(f"    -> No page links found in {name} llms.txt")
        return {"pages_fetched": 0, "pages_skipped": 0, "pages_failed": 0, "pages_html": 0}

    total = len(links)
    print(f"  Expanding {name}: found {total} page links")

    fetched = 0
    skipped = 0
    failed = 0
    html_skipped = 0

    for i, (title, url) in enumerate(links, 1):
        slug = url_to_slug(url)
        out_path = output_dir / f"{slug}.md"

        # Skip if already on disk (idempotent)
        if out_path.exists():
            skipped += 1
            continue

        if dry_run:
            print(f"    [{i}/{total}] Would fetch: {url} -> {out_path.name}")
            fetched += 1
            continue

        time.sleep(rate_limit)
        page_content = fetch_url(url)

        if page_content is None:
            print(f"    [{i}/{total}] FAILED: {url}")
            failed += 1
            continue

        if is_html_response(page_content):
            md = html_to_markdown(page_content, url, title)
            if md:
                output_dir.mkdir(parents=True, exist_ok=True)
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(md)
                fetched += 1
                if fetched % 10 == 0 or i == total:
                    print(f"    Expanding {name}: {fetched}/{total} pages fetched...")
            else:
                print(f"    [{i}/{total}] HTML (no article, skipped): {url}")
                html_skipped += 1
            continue

        # Write with # Source: header
        output_dir.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"# Source: {url}\n\n")
            f.write(page_content)

        fetched += 1
        if fetched % 10 == 0 or i == total:
            print(f"    Expanding {name}: {fetched}/{total} pages fetched...")

    stats = {
        "pages_fetched": fetched,
        "pages_skipped": skipped,
        "pages_failed": failed,
        "pages_html": html_skipped,
    }
    parts = []
    parts.append(f"{fetched} pages fetched")
    parts.append(f"{skipped} skipped (already on disk)")
    if html_skipped:
        parts.append(f"{html_skipped} skipped (HTML)")
    if failed:
        parts.append(f"{failed} failed")
    print(f"    {name}: {', '.join(parts)}")

    return stats


def scrape_site(site: dict, dry_run: bool = False, expand: bool = False) -> dict:
    """
    Scrape a single site's llms.txt documentation.

    Returns a result dict with keys: name, status, files_written, error.
    """
    name = site["name"]
    base_url = site["base_url"].rstrip("/") + "/"
    rate_limit = site.get("rate_limit_seconds", DEFAULT_RATE_LIMIT)

    output_dir = DOCS_ROOT / name / "llms"
    site_dir = DOCS_ROOT / name

    print(f"Scraping {name} from {base_url}")

    files_written = 0
    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Candidate URLs to try
    candidates = [
        ("llms-full.txt", urljoin(base_url, "llms-full.txt")),
        ("llms.txt", urljoin(base_url, "llms.txt")),
    ]

    any_fetched = False
    for filename, url in candidates:
        time.sleep(rate_limit)
        content = fetch_url(url)
        if content is None:
            print(f"    -> Not found: {url}")
            continue

        # Determine output filename
        stem = filename.replace(".txt", "")
        out_filename = f"{name}-{stem}.md"
        out_path = output_dir / out_filename

        if dry_run:
            print(f"    [dry-run] Would write {out_path} ({len(content)} chars)")
            any_fetched = True
            files_written += 1
            continue

        output_dir.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"    -> Wrote {out_path} ({len(content):,} chars)")
        any_fetched = True
        files_written += 1

    if any_fetched:
        write_meta_yaml(site_dir, site, fetched_at, dry_run=dry_run)

        # Expand individual pages if requested
        expand_stats = {"pages_fetched": 0, "pages_skipped": 0, "pages_failed": 0, "pages_html": 0}
        if expand or site.get("expand", False):
            expand_stats = expand_site_pages(site, output_dir, rate_limit, dry_run=dry_run)

        return {
            "name": name,
            "status": "ok",
            "files_written": files_written,
            "error": None,
            **expand_stats,
        }
    else:
        return {"name": name, "status": "failed", "files_written": 0, "error": "No llms.txt found"}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scrape llms.txt documentation for sites in llms-sites.yaml"
    )
    parser.add_argument(
        "--site",
        metavar="NAME",
        help="Scrape only this site (matches 'name' field in llms-sites.yaml)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be written without writing any files",
    )
    parser.add_argument(
        "--expand",
        action="store_true",
        help="Fetch individual pages linked from llms.txt indexes",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        metavar="N",
        help="Number of parallel workers (default: 1 for safe rate limiting)",
    )
    args = parser.parse_args()

    sites = load_sites(SITES_FILE)

    if args.site:
        matched = [s for s in sites if s["name"] == args.site]
        if not matched:
            print(f"Error: site '{args.site}' not found in {SITES_FILE}", file=sys.stderr)
            sys.exit(1)
        sites = matched

    print(f"Processing {len(sites)} site(s) ...")
    if args.dry_run:
        print("(dry-run mode - no files will be written)")

    results = []

    if args.workers > 1 and len(sites) > 1:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(scrape_site, site, args.dry_run, args.expand): site
                for site in sites
            }
            for future in as_completed(futures):
                results.append(future.result())
    else:
        for site in sites:
            results.append(scrape_site(site, dry_run=args.dry_run, expand=args.expand))

    # Summary
    ok = [r for r in results if r["status"] == "ok"]
    failed = [r for r in results if r["status"] == "failed"]
    total_files = sum(r["files_written"] for r in results)

    summary = f"\nDone: {len(ok)} ok, {len(failed)} failed, {total_files} files written"

    if args.expand:
        total_pages = sum(r.get("pages_fetched", 0) for r in results)
        total_skipped = sum(r.get("pages_skipped", 0) for r in results)
        total_html = sum(r.get("pages_html", 0) for r in results)
        total_page_failed = sum(r.get("pages_failed", 0) for r in results)
        summary += f", {total_pages} pages expanded"
        if total_skipped:
            summary += f", {total_skipped} pages skipped (on disk)"
        if total_html:
            summary += f", {total_html} pages skipped (HTML)"
        if total_page_failed:
            summary += f", {total_page_failed} pages failed"

    print(summary)

    if failed:
        print("Failed sites:")
        for r in failed:
            print(f"  - {r['name']}: {r['error']}")

    sys.exit(0 if not failed or len(ok) > 0 else 1)


if __name__ == "__main__":
    main()
