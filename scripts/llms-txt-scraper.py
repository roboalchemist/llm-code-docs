#!/usr/bin/env python3
"""
Generic llms.txt Documentation Scraper

Downloads LLM-friendly documentation from websites following the llms.txt standard.
Reads site configuration from llms-sites.yaml and downloads both individual files
and comprehensive documentation.

Standard: https://llmstxt.org/

Usage:
    python3 llms-txt-scraper.py [--site SITENAME] [--mode individual|full|both] [--workers N]
"""

import argparse
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
import yaml

# Configuration
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONFIG_FILE = SCRIPT_DIR / "llms-sites.yaml"

# Thread-safe printing
print_lock = threading.Lock()


def load_config() -> dict:
    """Load site configuration from YAML file."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file not found: {CONFIG_FILE}", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML configuration: {e}", file=sys.stderr)
        sys.exit(1)


def is_file_recent(file_path: Path, max_age_hours: int = 23) -> bool:
    """Check if a file was modified recently.

    Args:
        file_path: Path to file to check
        max_age_hours: Maximum age in hours (default: 23)

    Returns:
        bool: True if file exists and is newer than max_age_hours
    """
    if not file_path.exists():
        return False

    current_time = time.time()
    max_age_seconds = max_age_hours * 3600
    file_age = current_time - file_path.stat().st_mtime

    return file_age < max_age_seconds


def is_valid_text_content(content: bytes) -> tuple[bool, str]:
    """Check if content is valid text (not binary/compressed).

    Args:
        content: Raw bytes from response

    Returns:
        tuple: (is_valid: bool, reason: str)
    """
    # Check for common binary signatures
    binary_signatures = [
        (b'\x1f\x8b', 'gzip compressed'),
        (b'PK\x03\x04', 'zip archive'),
        (b'%PDF', 'PDF document'),
        (b'\x89PNG', 'PNG image'),
        (b'\xff\xd8\xff', 'JPEG image'),
        (b'GIF8', 'GIF image'),
        (b'\x00\x00\x00', 'binary data'),
    ]

    for sig, desc in binary_signatures:
        if content.startswith(sig):
            return False, desc

    # Check if content is valid UTF-8
    try:
        text = content.decode('utf-8')
    except UnicodeDecodeError:
        return False, 'invalid UTF-8 encoding'

    # Check for excessive null bytes (binary indicator)
    if b'\x00' in content[:1000]:
        return False, 'contains null bytes'

    # Check if it looks like HTML page instead of markdown
    text_lower = text.strip().lower()
    if text_lower.startswith('<!doctype') or text_lower.startswith('<html'):
        # Check for signs this is actually markdown content
        has_code_blocks = '```' in text
        has_md_headings = bool(re.search(r'^#{1,6}\s+\S', text, re.MULTILINE))
        has_md_links = bool(re.search(r'\[([^\]]+)\]\(([^)]+)\)', text))

        # If no markdown indicators, it's likely an HTML page
        if not (has_code_blocks or has_md_headings or has_md_links):
            # Additional check: is it a short error/redirect page?
            if len(text) < 2000 or '<title>301' in text or '<title>404' in text:
                return False, 'HTML redirect/error page'
            return False, 'HTML page (not markdown)'

    return True, 'valid'


def download_file(url: str, output_path: Path, description: str = None, force: bool = False) -> tuple[bool, int]:
    """Download a file from URL to output_path.

    Args:
        url: URL to download from
        output_path: Path to save the file
        description: Optional description for logging
        force: Force download even if file is recent

    Returns:
        tuple: (success: bool, file_size: int)
    """
    # Check if file is recently downloaded (skip if not forced)
    if not force and is_file_recent(output_path):
        age_hours = (time.time() - output_path.stat().st_mtime) / 3600
        with print_lock:
            print(f"  ⏭ Skipping {output_path.name}: Downloaded {age_hours:.1f}h ago")
        return (True, output_path.stat().st_size)
    try:
        desc = description or url
        with print_lock:
            print(f"  Downloading: {desc}")

        # Use headers that encourage text/markdown response
        headers = {
            'Accept': 'text/plain, text/markdown, text/x-markdown, */*',
            'Accept-Encoding': 'identity',  # Avoid compressed responses
        }
        response = requests.get(url, timeout=30, headers=headers)
        response.raise_for_status()

        # Validate content is actually text/markdown
        is_valid, reason = is_valid_text_content(response.content)
        if not is_valid:
            with print_lock:
                print(f"    ✗ Skipping {output_path.name}: {reason}", file=sys.stderr)
            return False, 0

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(response.text, encoding='utf-8')

        size_kb = len(response.text) / 1024
        with print_lock:
            print(f"    ✓ Saved: {output_path.name} ({size_kb:.1f} KB)")
        return True, len(response.text)

    except requests.RequestException as e:
        with print_lock:
            print(f"    ✗ Error downloading {url}: {e}", file=sys.stderr)
        return False, 0


def parse_llms_txt(content: str, base_url: str = "") -> list[str]:
    """Parse llms.txt content and extract all documentation URLs.

    Follows llms.txt standard: extracts URLs from markdown links [title](url).
    Deduplicates by base URL (strips query params and anchors) so that
    single-page docs with anchor navigation (e.g. ``?id=foo``) yield one URL
    instead of hundreds.

    Args:
        content: Raw text content of llms.txt file
        base_url: Base URL to resolve relative URLs (optional)

    Returns:
        list: Deduplicated URLs to documentation files
    """
    # Extract ALL markdown links: [Title](URL)
    # Use [^\)\n]+ to prevent matching across line breaks (some TOCs have
    # truncated URLs like "https://git..." that lack a closing paren).
    raw_urls = []
    for match in re.finditer(r'\[([^\]\n]+)\]\(([^\)\n]+)\)', content):
        href = match.group(2).strip()
        # Skip anchors, javascript, and mailto
        if href.startswith('#') or href.startswith('javascript:') or href.startswith('mailto:'):
            continue
        # Resolve relative URLs
        if href.startswith('http://') or href.startswith('https://'):
            raw_urls.append(href)
        elif base_url:
            raw_urls.append(urljoin(base_url, href))

    # Deduplicate: strip query params and fragments to collapse anchor-style
    # links (e.g. /api?id=foo, /api?id=bar → /api) into one URL per page.
    seen = {}
    for url in raw_urls:
        parsed = urlparse(url)
        # Canonical = scheme + netloc + path (no query, no fragment)
        canonical = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        # Normalize trailing slashes for dedup but keep original for download
        canon_key = canonical.rstrip('/')
        if canon_key not in seen:
            seen[canon_key] = canonical

    return list(seen.values())


def download_individual_files(site_name: str, base_url: str, output_dir: Path, force: bool = False, rate_limit_seconds: float = 0) -> tuple[int, int]:
    """Download individual markdown files from llms.txt.

    Args:
        site_name: Name of the site (for display)
        base_url: Base URL where llms.txt is located
        output_dir: Directory to save downloaded files
        force: Force download even if files are recent
        rate_limit_seconds: Optional delay between requests in seconds

    Returns:
        tuple: (success_count, fail_count)
    """
    with print_lock:
        print(f"\n  === Downloading Individual Files for {site_name} ===")

    # Download llms.txt
    llms_txt_url = urljoin(base_url, "llms.txt")

    try:
        response = requests.get(llms_txt_url, timeout=30)
        response.raise_for_status()
        llms_content = response.text
    except requests.RequestException as e:
        with print_lock:
            print(f"  ✗ Error fetching llms.txt from {llms_txt_url}: {e}", file=sys.stderr)
        return 0, 0

    # Parse URLs
    urls = parse_llms_txt(llms_content, base_url)
    with print_lock:
        print(f"  Found {len(urls)} documentation URLs")
        if rate_limit_seconds > 0:
            print(f"  Rate limit: {rate_limit_seconds}s between requests")

    if not urls:
        with print_lock:
            print(f"  ⚠ Warning: No URLs found in llms.txt", file=sys.stderr)
        return 0, 0

    success_count = 0
    fail_count = 0
    used_filenames: set[str] = set()

    for i, url in enumerate(urls):
        # Extract filename from URL path
        path = urlparse(url).path
        filename = _url_to_filename(path)

        # Deduplicate filenames by appending _2, _3, etc.
        orig_filename = filename
        counter = 2
        while filename in used_filenames:
            stem = orig_filename.rsplit('.', 1)[0]
            filename = f"{stem}_{counter}.md"
            counter += 1
        used_filenames.add(filename)

        output_path = output_dir / filename

        # Per llms.txt spec, try the .md version of the URL first, then the
        # original URL.  Many sites serve markdown at url.md even when the TOC
        # links to the HTML page.
        download_url = url
        if not url.endswith('.md'):
            md_url = url.rstrip('/') + '.md'
            # Quick HEAD check to see if .md version exists
            try:
                head_resp = requests.head(md_url, timeout=10, allow_redirects=True)
                if head_resp.status_code == 200:
                    ct = head_resp.headers.get('content-type', '')
                    if 'html' not in ct:
                        download_url = md_url
            except requests.RequestException:
                pass

        success, size = download_file(download_url, output_path, filename, force)
        if success:
            # Add source header (only if not already present)
            content = output_path.read_text(encoding='utf-8')
            if not content.startswith(f"# Source: {url}"):
                header = f"# Source: {url}\n\n"
                output_path.write_text(header + content, encoding='utf-8')
            success_count += 1
        else:
            fail_count += 1

        # Apply rate limiting (but not after the last request)
        if rate_limit_seconds > 0 and i < len(urls) - 1:
            time.sleep(rate_limit_seconds)

    return success_count, fail_count


def _url_to_filename(path: str) -> str:
    """Convert a URL path to a safe, unique-ish filename.

    Examples:
        /docs/guide/apps.md         → apps.md
        /docs/guide/apps            → apps.md
        /                           → index.md
        /workers/runtime-apis/fetch → workers_runtime-apis_fetch.md
    """
    name = Path(path).name

    # No filename (trailing slash or root)
    if not name:
        parts = [p for p in path.split('/') if p]
        name = parts[-1] if parts else 'index'

    # Ensure .md extension
    if not name.endswith('.md'):
        name += '.md'

    # Path-based naming for generic filenames to avoid collisions
    if name in ('index.md', 'index.html.md'):
        parts = [p for p in path.strip('/').split('/') if p and p not in ('index.md', 'index.html.md')]
        if parts:
            name = '_'.join(parts) + '.md'

    return name


def download_full_file(site_name: str, base_url: str, output_dir: Path, force: bool = False) -> bool:
    """Download the comprehensive llms-full.txt file.

    Args:
        site_name: Name of the site
        base_url: Base URL where llms-full.txt is located
        output_dir: Directory to save the file
        force: Force download even if file is recent

    Returns:
        bool: Success status
    """
    with print_lock:
        print(f"\n  === Downloading Full Documentation for {site_name} ===")

    llms_full_url = urljoin(base_url, "llms-full.txt")
    output_path = output_dir / f"{site_name}-full.md"

    success, size = download_file(llms_full_url, output_path, "llms-full.txt", force)

    if success:
        # Add source header (only if not already present)
        content = output_path.read_text(encoding='utf-8')
        expected_title = f"# {site_name.replace('-', ' ').title()} Documentation"
        if not content.startswith(expected_title):
            header = f"{expected_title}\n\n"
            header += f"Source: {llms_full_url}\n\n---\n\n"
            output_path.write_text(header + content, encoding='utf-8')
        with print_lock:
            print(f"  ✓ Full documentation saved to: {output_path}")

    return success


def split_full_file(full_path: Path, output_dir: Path) -> int:
    """Split an llms-full.txt/md file into individual documents using H1 headers.

    Each H1 (``# Title``) starts a new document. The first H1 is treated as the
    overall title/preamble and is skipped (it's already in the full file).
    Documents shorter than 200 chars are skipped as likely noise.

    Args:
        full_path: Path to the full markdown file
        output_dir: Directory to write individual files

    Returns:
        Number of individual files created
    """
    content = full_path.read_text(encoding='utf-8')
    lines = content.split('\n')

    # Find all H1 header positions
    h1_positions = []
    for i, line in enumerate(lines):
        if line.startswith('# ') and not line.startswith('# Source:'):
            h1_positions.append(i)

    if len(h1_positions) < 2:
        return 0  # Single document or no clear boundaries

    # Split into documents (skip the first H1 which is the file title/preamble)
    documents = []
    for idx in range(1, len(h1_positions)):
        start = h1_positions[idx]
        end = h1_positions[idx + 1] if idx + 1 < len(h1_positions) else len(lines)
        title = lines[start].lstrip('# ').strip()
        body = '\n'.join(lines[start:end]).strip()
        if len(body) >= 200 and title:
            documents.append((title, body))

    if not documents:
        return 0

    count = 0
    used: set[str] = set()
    for title, body in documents:
        # Convert title to filename
        fname = re.sub(r'[^\w\s-]', '', title.lower())
        fname = re.sub(r'[\s]+', '-', fname).strip('-')[:80]
        if not fname:
            fname = f"section-{count}"
        fname += '.md'
        # Deduplicate
        orig = fname
        n = 2
        while fname in used:
            fname = f"{orig.rsplit('.', 1)[0]}_{n}.md"
            n += 1
        used.add(fname)

        out_path = output_dir / fname
        if not out_path.exists():  # Don't overwrite existing individual files
            out_path.write_text(body, encoding='utf-8')
            count += 1

    return count


def process_site(site: dict, mode: str, force: bool = False) -> dict:
    """Process a single site configuration.

    Args:
        site: Site configuration dictionary
        mode: Download mode ('individual', 'full', or 'both')
        force: Force re-download even if files are recent

    Returns:
        dict: Statistics about the download
    """
    name = site['name']
    base_url = site['base_url']
    description = site.get('description', '')
    rate_limit_seconds = site.get('rate_limit_seconds', 0)

    with print_lock:
        print(f"\n{'=' * 70}")
        print(f"Processing: {name}")
        print(f"Base URL: {base_url}")
        if description:
            print(f"Description: {description}")
        if rate_limit_seconds > 0:
            print(f"Rate limit: {rate_limit_seconds}s between requests")
        print('=' * 70)

    # Create output directory under docs/llms-txt/
    output_dir = REPO_ROOT / "docs/llms-txt" / name
    output_dir.mkdir(parents=True, exist_ok=True)

    stats = {
        'name': name,
        'success': True,
        'individual_success': 0,
        'individual_fail': 0,
        'full_success': False
    }

    # Download based on mode
    if mode in ['individual', 'both']:
        success_count, fail_count = download_individual_files(name, base_url, output_dir, force, rate_limit_seconds)
        stats['individual_success'] = success_count
        stats['individual_fail'] = fail_count
        if fail_count > 0:
            stats['success'] = False

    if mode in ['full', 'both']:
        full_success = download_full_file(name, base_url, output_dir, force)
        stats['full_success'] = full_success
        if not full_success:
            stats['success'] = False

    # If we got a full file but no individual files, try to split the full file
    # using H1 headers as document boundaries.
    if stats['full_success'] and stats['individual_success'] == 0:
        full_path = output_dir / f"{name}-full.md"
        if full_path.exists():
            split_count = split_full_file(full_path, output_dir)
            if split_count > 0:
                stats['individual_success'] = split_count
                with print_lock:
                    print(f"  Split full file into {split_count} individual documents")

    return stats


def _backfill_one_site(name: str, full_path: Path, sites_by_name: dict) -> dict:
    """Backfill a single full-only dir. Returns result dict."""
    llms_dir = full_path.parent.parent
    output_dir = llms_dir / name
    site_config = sites_by_name.get(name)

    if site_config:
        base_url = site_config['base_url']
        rate_limit = site_config.get('rate_limit_seconds', 0)
        with print_lock:
            print(f"\n{name}: trying individual download from {base_url}")

        success, fail = download_individual_files(name, base_url, output_dir, force=True, rate_limit_seconds=rate_limit)
        if success > 0:
            with print_lock:
                print(f"  {name}: downloaded {success} individual files")
            return {"name": name, "result": "downloaded", "count": success}

    # Fallback: split the full file
    with print_lock:
        print(f"  {name}: splitting full file by H1 headers")
    split_count = split_full_file(full_path, output_dir)
    if split_count > 0:
        with print_lock:
            print(f"  {name}: split into {split_count} files")
        return {"name": name, "result": "split", "count": split_count}

    with print_lock:
        print(f"  {name}: could not split (single document or no H1 boundaries)")
    return {"name": name, "result": "failed", "count": 0}


def backfill_full_only_dirs(workers: int = 10) -> int:
    """Find llms-txt dirs that have only a full file and attempt to add individual files.

    Processes sites in parallel — each site's downloads are sequential (no rate
    limit issues), but multiple sites run concurrently.

    Returns:
        Exit code (0 = success)
    """
    llms_dir = REPO_ROOT / "docs" / "llms-txt"
    config = load_config()
    sites_by_name = {s['name']: s for s in config.get('sites', [])}

    # Find full-only dirs (only 1 file, and it's a -full.md/txt)
    full_only = []
    for d in sorted(llms_dir.iterdir()):
        if not d.is_dir():
            continue
        files = [f for f in d.iterdir() if not f.name.startswith('.')]
        full_files = [f for f in files if f.name.endswith(('-full.md', '-full.txt'))]
        non_full = [f for f in files if not f.name.endswith(('-full.md', '-full.txt'))]
        if full_files and not non_full:
            full_only.append((d.name, full_files[0]))

    print(f"Found {len(full_only)} dirs with only a full file")
    print(f"Processing with {workers} parallel workers\n")

    results = {"downloaded": 0, "split": 0, "failed": 0}

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(_backfill_one_site, name, full_path, sites_by_name): name
            for name, full_path in full_only
        }
        for future in as_completed(futures):
            name = futures[future]
            try:
                r = future.result()
                if r["result"] == "downloaded":
                    results["downloaded"] += 1
                elif r["result"] == "split":
                    results["split"] += 1
                else:
                    results["failed"] += 1
            except Exception as e:
                with print_lock:
                    print(f"  {name}: ERROR — {e}")
                results["failed"] += 1

    print(f"\n{'=' * 70}")
    print(f"Backfill Summary:")
    print(f"  Individual downloads: {results['downloaded']}")
    print(f"  Split from full file: {results['split']}")
    print(f"  Failed:               {results['failed']}")
    print(f"  Total:                {sum(results.values())}")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Download llms.txt-compliant documentation from configured sites"
    )
    parser.add_argument(
        '--site',
        type=str,
        action='append',
        help='Download only the specified site(s) - can be used multiple times'
    )
    parser.add_argument(
        '--mode',
        choices=['full', 'individual', 'both'],
        default='both',
        help='Download mode: full (llms-full.txt), individual (separate files), or both (default: both)'
    )
    parser.add_argument(
        '--workers',
        type=int,
        default=10,
        help='Number of parallel workers for downloading multiple sites (default: 10)'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Force re-download even if files were downloaded in last 23 hours'
    )
    parser.add_argument(
        '--backfill',
        action='store_true',
        help='Find dirs with only a full file and attempt to download individual files or split'
    )

    args = parser.parse_args()

    # Handle --backfill mode
    if args.backfill:
        return backfill_full_only_dirs()

    # Load configuration
    config = load_config()
    sites = config.get('sites', [])

    if not sites:
        print("Error: No sites configured in YAML file", file=sys.stderr)
        return 1

    # Filter sites if --site specified
    if args.site:
        sites = [s for s in sites if s['name'] in args.site]
        if not sites:
            print(f"Error: Site(s) '{', '.join(args.site)}' not found in configuration", file=sys.stderr)
            print(f"Available sites: {', '.join([s['name'] for s in config['sites']])}")
            return 1

    print("llms.txt Documentation Scraper")
    print("=" * 70)
    print(f"Configuration: {CONFIG_FILE}")
    print(f"Mode: {args.mode}")
    print(f"Sites to process: {len(sites)}")
    print(f"Parallel workers: {args.workers}")
    print(f"Force re-download: {'Yes' if args.force else 'No (skip if <23hrs old)'}")

    # Process sites in parallel
    all_stats = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        # Submit all site processing tasks
        future_to_site = {
            executor.submit(process_site, site, args.mode, args.force): site
            for site in sites
        }

        # Collect results as they complete
        for future in as_completed(future_to_site):
            try:
                stats = future.result()
                all_stats.append(stats)
            except Exception as e:
                site = future_to_site[future]
                with print_lock:
                    print(f"\n✗ Error processing {site['name']}: {e}", file=sys.stderr)
                # Add failed stats
                all_stats.append({
                    'name': site['name'],
                    'success': False,
                    'individual_success': 0,
                    'individual_fail': 0,
                    'full_success': False
                })

    # Print summary
    print("\n" + "=" * 70)
    print("📊 Download Summary")
    print("=" * 70)

    for stats in all_stats:
        print(f"\n{stats['name']}:")

        if args.mode in ['individual', 'both']:
            print(f"  Individual files: {stats['individual_success']} successful, {stats['individual_fail']} failed")
        if args.mode in ['full', 'both']:
            status = "✓" if stats['full_success'] else "✗"
            print(f"  Full documentation: {status}")

        overall = "✓ Success" if stats['success'] else "✗ Some errors"
        print(f"  Overall: {overall}")

    # Check if all succeeded
    all_success = all(s['success'] for s in all_stats)

    print("\n" + "=" * 70)
    if all_success:
        print("✓ All documentation downloads completed successfully!")
        return 0
    else:
        print("✗ Some errors occurred during download", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
