#!/usr/bin/env python3
"""
Generic llms.txt Documentation Scraper

Downloads LLM-friendly documentation from websites following the llms.txt standard.
Reads site configuration from llms-sites.yaml and downloads both individual files
and comprehensive documentation.

Standard: https://llmstxt.org/

Usage:
    python3 llms-txt-scraper.py [--site SITENAME] [--mode individual|full|both]
"""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
import yaml

# Configuration
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONFIG_FILE = SCRIPT_DIR / "llms-sites.yaml"


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


def download_file(url: str, output_path: Path, description: str = None) -> tuple[bool, int]:
    """Download a file from URL to output_path.

    Returns:
        tuple: (success: bool, file_size: int)
    """
    try:
        desc = description or url
        print(f"  Downloading: {desc}")
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(response.text, encoding='utf-8')

        size_kb = len(response.text) / 1024
        print(f"    ✓ Saved: {output_path.name} ({size_kb:.1f} KB)")
        return True, len(response.text)

    except requests.RequestException as e:
        print(f"    ✗ Error downloading {url}: {e}", file=sys.stderr)
        return False, 0


def parse_llms_txt(content: str) -> list[str]:
    """Parse llms.txt content and extract all .md URLs.

    Follows llms.txt standard: extracts URLs from markdown links [title](url.md)

    Args:
        content: Raw text content of llms.txt file

    Returns:
        list: URLs to markdown documentation files
    """
    # Extract URLs from markdown links: [Title](URL)
    # Pattern matches markdown links with .md URLs
    pattern = r'\[([^\]]+)\]\((https?://[^\)]+\.md)\)'
    urls = []

    for match in re.finditer(pattern, content):
        url = match.group(2)  # Extract URL from the second capture group
        urls.append(url)

    return urls


def download_individual_files(site_name: str, base_url: str, output_dir: Path) -> tuple[int, int]:
    """Download individual markdown files from llms.txt.

    Args:
        site_name: Name of the site (for display)
        base_url: Base URL where llms.txt is located
        output_dir: Directory to save downloaded files

    Returns:
        tuple: (success_count, fail_count)
    """
    print(f"\n  === Downloading Individual Files for {site_name} ===")

    # Download llms.txt
    llms_txt_url = urljoin(base_url, "llms.txt")

    try:
        response = requests.get(llms_txt_url, timeout=30)
        response.raise_for_status()
        llms_content = response.text
    except requests.RequestException as e:
        print(f"  ✗ Error fetching llms.txt from {llms_txt_url}: {e}", file=sys.stderr)
        return 0, 0

    # Parse URLs
    urls = parse_llms_txt(llms_content)
    print(f"  Found {len(urls)} documentation URLs")

    if not urls:
        print(f"  ⚠ Warning: No URLs found in llms.txt", file=sys.stderr)
        return 0, 0

    success_count = 0
    fail_count = 0

    for url in urls:
        # Extract filename from URL
        filename = Path(urlparse(url).path).name
        if not filename.endswith('.md'):
            filename += '.md'

        output_path = output_dir / filename

        success, size = download_file(url, output_path, filename)
        if success:
            # Add source header
            content = output_path.read_text(encoding='utf-8')
            header = f"# Source: {url}\n\n"
            output_path.write_text(header + content, encoding='utf-8')
            success_count += 1
        else:
            fail_count += 1

    return success_count, fail_count


def download_full_file(site_name: str, base_url: str, output_dir: Path) -> bool:
    """Download the comprehensive llms-full.txt file.

    Args:
        site_name: Name of the site
        base_url: Base URL where llms-full.txt is located
        output_dir: Directory to save the file

    Returns:
        bool: Success status
    """
    print(f"\n  === Downloading Full Documentation for {site_name} ===")

    llms_full_url = urljoin(base_url, "llms-full.txt")
    output_path = output_dir / f"{site_name}-full.md"

    success, size = download_file(llms_full_url, output_path, "llms-full.txt")

    if success:
        # Add source header
        content = output_path.read_text(encoding='utf-8')
        header = f"# {site_name.replace('-', ' ').title()} Documentation\n\n"
        header += f"Source: {llms_full_url}\n\n---\n\n"
        output_path.write_text(header + content, encoding='utf-8')
        print(f"  ✓ Full documentation saved to: {output_path}")

    return success


def process_site(site: dict, mode: str) -> dict:
    """Process a single site configuration.

    Args:
        site: Site configuration dictionary
        mode: Download mode ('individual', 'full', or 'both')

    Returns:
        dict: Statistics about the download
    """
    name = site['name']
    base_url = site['base_url']
    description = site.get('description', '')

    print(f"\n{'=' * 70}")
    print(f"Processing: {name}")
    print(f"Base URL: {base_url}")
    if description:
        print(f"Description: {description}")
    print('=' * 70)

    # Create output directory under llms-txt-docs/
    output_dir = REPO_ROOT / "llms-txt-docs" / name
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
        success_count, fail_count = download_individual_files(name, base_url, output_dir)
        stats['individual_success'] = success_count
        stats['individual_fail'] = fail_count
        if fail_count > 0:
            stats['success'] = False

    if mode in ['full', 'both']:
        full_success = download_full_file(name, base_url, output_dir)
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
        help='Download only the specified site (use site name from config)'
    )
    parser.add_argument(
        '--mode',
        choices=['full', 'individual', 'both'],
        default='both',
        help='Download mode: full (llms-full.txt), individual (separate files), or both (default: both)'
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
        sites = [s for s in sites if s['name'] == args.site]
        if not sites:
            print(f"Error: Site '{args.site}' not found in configuration", file=sys.stderr)
            print(f"Available sites: {', '.join([s['name'] for s in config['sites']])}")
            return 1

    print("llms.txt Documentation Scraper")
    print("=" * 70)
    print(f"Configuration: {CONFIG_FILE}")
    print(f"Mode: {args.mode}")
    print(f"Sites to process: {len(sites)}")

    # Process each site
    all_stats = []
    for site in sites:
        stats = process_site(site, args.mode)
        all_stats.append(stats)

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
