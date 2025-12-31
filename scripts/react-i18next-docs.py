#!/usr/bin/env python3
"""
react-i18next Documentation Scraper
Downloads react-i18next documentation from llms.txt file.
react-i18next provides React bindings for the i18next internationalization framework.
"""

import os
import sys
import requests
from pathlib import Path
import time
import re
from urllib.parse import urljoin, urlparse

# Base configuration
BASE_URL = "https://react.i18next.com"
LLMS_TXT_URL = f"{BASE_URL}/llms.txt"


def download_llms_txt():
    """Download the main llms.txt file."""
    try:
        print(f"Downloading llms.txt from {LLMS_TXT_URL}")
        response = requests.get(LLMS_TXT_URL, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error downloading llms.txt: {e}")
        return None


def parse_llms_txt(content):
    """Parse llms.txt content and extract linked documents."""
    # Find all markdown links in the format [text](url)
    link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    links = re.findall(link_pattern, content)

    # Filter for documentation URLs (typically markdown or html files)
    docs = []
    for title, url in links:
        # Make absolute URLs
        if url.startswith('http'):
            abs_url = url
        else:
            abs_url = urljoin(BASE_URL, url)

        # Only include URLs from the same domain
        if urlparse(abs_url).netloc in ['react.i18next.com']:
            docs.append({
                'title': title.strip(),
                'url': abs_url
            })

    return docs


def main():
    """Main function to download react-i18next documentation."""
    print("=" * 60)
    print("react-i18next Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "llms-txt" / "react-i18next"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Download main llms.txt
    print("Downloading main llms.txt...")
    llms_content = download_llms_txt()

    if not llms_content:
        print("Failed to download llms.txt")
        sys.exit(1)

    # Save the main llms.txt as README.md
    readme_path = output_dir / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(f"# react-i18next Documentation\n")
        f.write(f"# Source: {LLMS_TXT_URL}\n\n")
        f.write(llms_content)

    print(f"Saved main documentation: {readme_path}")
    print()

    # Parse and extract linked documents
    print("Parsing llms.txt for additional resources...")
    docs = parse_llms_txt(llms_content)
    print(f"Found {len(docs)} documentation links")
    print()

    # Note: For llms.txt sites, we typically only save the llms.txt itself
    # since it's already optimized for LLM consumption
    # The linked pages are just references, not additional content to download

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Main llms.txt: Saved")
    print(f"Additional links: {len(docs)} (referenced in llms.txt)")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    print("Documentation downloaded successfully!")
    sys.exit(0)


if __name__ == "__main__":
    main()
