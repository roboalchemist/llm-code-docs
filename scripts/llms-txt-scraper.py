#!/usr/bin/env python3
"""
llms.txt Scraper

Downloads llms.txt (and llms-full.txt) documentation from sites listed in
scripts/llms-sites.yaml. Output is written to docs/{site_name}/llms/.

After writing files, creates or updates docs/{site_name}/_meta.yaml with
primary_source: llms.

Usage:
    python3 scripts/llms-txt-scraper.py                 # all sites
    python3 scripts/llms-txt-scraper.py --site dspy     # single site
    python3 scripts/llms-txt-scraper.py --dry-run       # dry run (no writes)
    python3 scripts/llms-txt-scraper.py --workers 8     # parallel workers
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


SCRIPT_DIR = Path(__file__).resolve().parent
DOCS_ROOT = SCRIPT_DIR.parent / "docs"
SITES_FILE = SCRIPT_DIR / "llms-sites.yaml"

DEFAULT_TIMEOUT = 30
DEFAULT_WORKERS = 4
DEFAULT_RATE_LIMIT = 1.0  # seconds between requests per site


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


def scrape_site(site: dict, dry_run: bool = False) -> dict:
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
        return {"name": name, "status": "ok", "files_written": files_written, "error": None}
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
                executor.submit(scrape_site, site, args.dry_run): site
                for site in sites
            }
            for future in as_completed(futures):
                results.append(future.result())
    else:
        for site in sites:
            results.append(scrape_site(site, dry_run=args.dry_run))

    # Summary
    ok = [r for r in results if r["status"] == "ok"]
    failed = [r for r in results if r["status"] == "failed"]
    total_files = sum(r["files_written"] for r in results)

    print(f"\nDone: {len(ok)} ok, {len(failed)} failed, {total_files} files written")
    if failed:
        print("Failed sites:")
        for r in failed:
            print(f"  - {r['name']}: {r['error']}")

    sys.exit(0 if not failed or len(ok) > 0 else 1)


if __name__ == "__main__":
    main()
