#!/usr/bin/env python3
"""
Graphite Documentation Downloader

Downloads LLM-friendly documentation from Graphite.
By default, downloads both individual files (for efficient context management)
and the comprehensive full documentation file.

Modes:
1. both (default): Download both individual files and comprehensive file
2. individual: Parse llms.txt and download each markdown file separately
3. full: Download only the comprehensive file (llms-full.txt)

Usage:
    python3 graphite-docs.py [--mode both|individual|full]
"""

import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests

# Configuration
BASE_URL = "https://graphite.com/docs"
LLMS_TXT_URL = f"{BASE_URL}/llms.txt"
LLMS_FULL_URL = f"{BASE_URL}/llms-full.txt"
OUTPUT_DIR = Path(__file__).parent.parent / "graphite"


def download_file(url: str, output_path: Path) -> bool:
    """Download a file from URL to output_path."""
    try:
        print(f"Downloading: {url}")
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(response.text, encoding='utf-8')

        size_kb = len(response.text) / 1024
        print(f"  ✓ Saved: {output_path.name} ({size_kb:.1f} KB)")
        return True

    except requests.RequestException as e:
        print(f"  ✗ Error downloading {url}: {e}", file=sys.stderr)
        return False


def download_full_docs() -> bool:
    """Download the comprehensive llms-full.txt file."""
    print("\n=== Downloading Full Documentation ===")
    output_path = OUTPUT_DIR / "graphite-full.md"

    success = download_file(LLMS_FULL_URL, output_path)

    if success:
        # Add source header
        content = output_path.read_text(encoding='utf-8')
        header = f"# Graphite Documentation\n\nSource: {LLMS_FULL_URL}\n\n---\n\n"
        output_path.write_text(header + content, encoding='utf-8')
        print(f"\n✓ Full documentation saved to: {output_path}")

    return success


def parse_llms_txt() -> list[str]:
    """Parse llms.txt and extract all documentation URLs."""
    print("\n=== Parsing llms.txt ===")

    try:
        response = requests.get(LLMS_TXT_URL, timeout=30)
        response.raise_for_status()
        content = response.text

        # Extract URLs from markdown links: [Title](URL)
        # Pattern matches markdown links with .md URLs
        pattern = r'\[([^\]]+)\]\((https://[^\)]+\.md)\)'
        urls = []

        for match in re.finditer(pattern, content):
            url = match.group(2)  # Extract URL from the second capture group
            urls.append(url)

        print(f"Found {len(urls)} documentation URLs")
        return urls

    except requests.RequestException as e:
        print(f"Error fetching llms.txt: {e}", file=sys.stderr)
        return []


def download_individual_docs() -> tuple[int, int]:
    """Download individual markdown files listed in llms.txt."""
    print("\n=== Downloading Individual Files ===")

    urls = parse_llms_txt()
    if not urls:
        print("No URLs found in llms.txt", file=sys.stderr)
        return 0, 0

    success_count = 0
    fail_count = 0

    for url in urls:
        # Extract filename from URL
        # e.g., https://graphite-58cc94ce.mintlify.dev/docs/ai-ingestion.md -> ai-ingestion.md
        filename = Path(urlparse(url).path).name
        if not filename.endswith('.md'):
            filename += '.md'

        output_path = OUTPUT_DIR / filename

        if download_file(url, output_path):
            # Add source header
            content = output_path.read_text(encoding='utf-8')
            header = f"# Source: {url}\n\n"
            output_path.write_text(header + content, encoding='utf-8')
            success_count += 1
        else:
            fail_count += 1

    print(f"\n✓ Downloaded {success_count} files")
    if fail_count > 0:
        print(f"✗ Failed: {fail_count} files", file=sys.stderr)

    return success_count, fail_count


def main():
    parser = argparse.ArgumentParser(
        description="Download Graphite LLM-friendly documentation"
    )
    parser.add_argument(
        '--mode',
        choices=['full', 'individual', 'both'],
        default='both',
        help='Download mode: full (llms-full.txt), individual (separate files), or both (default: both)'
    )

    args = parser.parse_args()

    print("Graphite Documentation Downloader")
    print("=" * 50)
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Mode: {args.mode}")

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    success = True

    if args.mode in ['full', 'both']:
        success = download_full_docs() and success

    if args.mode in ['individual', 'both']:
        success_count, fail_count = download_individual_docs()
        success = (fail_count == 0) and success

    print("\n" + "=" * 50)
    if success:
        print("✓ Documentation download complete!")
        return 0
    else:
        print("✗ Some errors occurred during download", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
