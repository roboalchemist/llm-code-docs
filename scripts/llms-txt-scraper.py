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
        response = requests.get(url, timeout=30)
        response.raise_for_status()

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

    Follows llms.txt standard: extracts URLs from markdown links [title](url)

    Args:
        content: Raw text content of llms.txt file
        base_url: Base URL to resolve relative URLs (optional)

    Returns:
        list: URLs to documentation files
    """
    # Extract URLs from markdown links: [Title](URL)
    # Pattern matches markdown links with .md or .md.txt URLs (both absolute and relative)
    pattern_absolute_md = r'\[([^\]]+)\]\((https?://[^\)]+\.md(?:\.txt)?)\)'
    pattern_relative_md = r'\[([^\]]+)\]\((/[^\)]+\.md(?:\.txt)?)\)'
    # Pattern for bare relative paths (no leading slash) - must end with .md or .md.txt and close paren
    # Use [^\)] to match anything except closing paren to avoid matching across lines
    pattern_bare_relative_nested = r'\[([^\]]+)\]\(([^\)]+\.md(?:\.txt)?)\)'
    # Pattern for URLs without .md extension (some sites use path-based URLs)
    pattern_relative_path = r'\[([^\]]+)\]\((/[^\)]+)\)'
    urls = []

    # First try absolute .md or .md.txt URLs
    for match in re.finditer(pattern_absolute_md, content):
        url = match.group(2)
        urls.append(url)

    # If no absolute .md URLs found, try relative .md or .md.txt URLs (starting with /)
    if not urls and base_url:
        for match in re.finditer(pattern_relative_md, content):
            relative_url = match.group(2)
            url = urljoin(base_url, relative_url)
            urls.append(url)

    # If still no URLs, try bare relative paths with .md or .md.txt (like "Accordion.md" or "releases/v0-1-0.md")
    if not urls and base_url:
        for match in re.finditer(pattern_bare_relative_nested, content):
            relative_url = match.group(2)
            # Skip anchor links, javascript, and absolute URLs
            if relative_url.startswith('#') or relative_url.startswith('javascript:') or relative_url.startswith('http'):
                continue
            url = urljoin(base_url, relative_url)
            urls.append(url)

    # If still no URLs, try relative path-based URLs (without .md extension)
    if not urls and base_url:
        for match in re.finditer(pattern_relative_path, content):
            relative_url = match.group(2)
            # Skip anchor links and javascript
            if relative_url.startswith('#') or relative_url.startswith('javascript:'):
                continue
            url = urljoin(base_url, relative_url)
            urls.append(url)

    return urls


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

    for i, url in enumerate(urls):
        # Extract filename from URL
        path = urlparse(url).path
        filename = Path(path).name

        # If no filename (path ends with /), use the last directory as filename
        if not filename:
            parts = [p for p in path.split('/') if p]
            filename = parts[-1] if parts else 'index'

        # Ensure .md extension (handle .md.txt files by converting to .md)
        if filename.endswith('.md.txt'):
            filename = filename[:-4]  # Remove .txt, keep .md
        elif not filename.endswith('.md'):
            filename += '.md'

        output_path = output_dir / filename

        success, size = download_file(url, output_path, filename, force)
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

    return stats


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

    args = parser.parse_args()

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
