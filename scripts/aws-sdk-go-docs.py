#!/usr/bin/env python3
"""
AWS SDK for Go Documentation Scraper
Downloads and converts AWS SDK for Go v1 and v2 documentation from AWS docs site.
Parses llms.txt files to get all documentation URLs and converts HTML to Markdown.
"""

import os
import sys
import requests
from pathlib import Path
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import html2text
import re

# Output directories
OUTPUT_BASE = Path(__file__).parent.parent / "docs" / "web-scraped"
OUTPUT_DIR_V1 = OUTPUT_BASE / "aws-sdk-go-v1"
OUTPUT_DIR_V2 = OUTPUT_BASE / "aws-sdk-go-v2"

# Base URLs
BASE_URL_V1 = "https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/"
BASE_URL_V2 = "https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/"
LLMS_TXT_V1 = BASE_URL_V1 + "llms.txt"
LLMS_TXT_V2 = BASE_URL_V2 + "llms.txt"


def html_to_markdown(html_content, url):
    """Convert HTML content to markdown."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # Don't wrap text

    try:
        markdown = h.handle(html_content)
        # Add source URL header if not already present
        if not markdown.startswith("# Source:"):
            markdown = f"# Source: {url}\n\n{markdown}"
        return markdown
    except Exception as e:
        print(f"    -> Warning: Error converting HTML to markdown: {e}")
        return None


def extract_main_content(soup):
    """Extract the main content from the AWS documentation page."""
    # Try to find the main content area
    main_content = None

    # Common selectors for AWS documentation
    selectors = [
        'main',
        'article',
        '[role="main"]',
        '.awsdocs',
        'div.awsdocs-content-container',
    ]

    for selector in selectors:
        main_content = soup.select_one(selector)
        if main_content:
            break

    if not main_content:
        # Fallback to body
        main_content = soup.find('body')

    return str(main_content) if main_content else str(soup)


def download_page(page_url, output_dir, version="v1"):
    """Download a documentation page and convert to markdown."""
    try:
        # Extract filename from URL
        parsed = urlparse(page_url)
        path_parts = parsed.path.split('/')
        filename = path_parts[-1] if path_parts[-1] else 'index'

        # Remove .html extension and add .md
        if filename.endswith('.html'):
            filename = filename[:-5]
        filename = filename + '.md' if not filename.endswith('.md') else filename

        output_path = output_dir / filename

        # Skip if already downloaded recently
        if output_path.exists():
            file_age = time.time() - output_path.stat().st_mtime
            if file_age < 86400:  # 24 hours
                print(f"    ⏭ Skipping {filename}: Already downloaded")
                return True

        # Download page
        response = requests.get(page_url, timeout=30)
        response.raise_for_status()

        # Parse HTML and extract main content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        # Extract main content
        main_content_html = extract_main_content(soup)
        main_soup = BeautifulSoup(main_content_html, 'html.parser')

        # Convert to markdown
        markdown = html_to_markdown(str(main_soup), page_url)

        if markdown:
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path.write_text(markdown, encoding='utf-8')
            size_kb = len(markdown) / 1024
            print(f"    ✓ {filename} ({size_kb:.1f} KB)")
            return True
        else:
            print(f"    ✗ Failed to convert {filename}")
            return False

    except requests.RequestException as e:
        print(f"    ✗ Error downloading {page_url}: {e}")
        return False
    except Exception as e:
        print(f"    ✗ Error processing {page_url}: {e}")
        return False


def parse_llms_txt(llms_txt_url):
    """Parse llms.txt and extract documentation URLs."""
    try:
        response = requests.get(llms_txt_url, timeout=30)
        response.raise_for_status()
        content = response.text

        # Extract all URLs from markdown links in llms.txt
        # Pattern: [text](url)
        pattern = r'\[([^\]]+)\]\((https?://[^\)]+)\)'
        matches = re.findall(pattern, content)

        urls = [url for _, url in matches]
        return urls

    except requests.RequestException as e:
        print(f"Error fetching llms.txt from {llms_txt_url}: {e}")
        return []


def scrape_version(version, llms_txt_url, output_dir, base_url):
    """Scrape a specific version of AWS SDK for Go docs."""
    print(f"\n{'='*70}")
    print(f"Scraping AWS SDK for Go {version}")
    print(f"{'='*70}")
    print(f"Source: {llms_txt_url}")
    print(f"Output: {output_dir}\n")

    # Get documentation URLs from llms.txt
    print("Parsing llms.txt...")
    urls = parse_llms_txt(llms_txt_url)

    if not urls:
        print("No documentation URLs found in llms.txt")
        return 0

    print(f"Found {len(urls)} documentation URLs\n")
    print(f"Downloading and converting documentation...\n")

    # Download and convert each page
    success_count = 0
    for i, url in enumerate(urls, 1):
        print(f"  [{i}/{len(urls)}]", end=" ")
        if download_page(url, output_dir, version):
            success_count += 1
        time.sleep(0.5)  # Rate limit

    return success_count


def main():
    """Main entry point."""
    print("\nAWS SDK for Go Documentation Scraper")
    print("=" * 70)

    # Scrape v1
    success_v1 = scrape_version("v1", LLMS_TXT_V1, OUTPUT_DIR_V1, BASE_URL_V1)

    # Scrape v2
    success_v2 = scrape_version("v2", LLMS_TXT_V2, OUTPUT_DIR_V2, BASE_URL_V2)

    # Summary
    print(f"\n{'='*70}")
    print("Summary")
    print(f"{'='*70}")
    print(f"AWS SDK for Go v1: {success_v1} files downloaded")
    print(f"AWS SDK for Go v2: {success_v2} files downloaded")
    print(f"Total: {success_v1 + success_v2} files")
    print(f"\nDocumentation saved to:")
    print(f"  - {OUTPUT_DIR_V1}")
    print(f"  - {OUTPUT_DIR_V2}")


if __name__ == "__main__":
    main()
