#!/usr/bin/env python3
"""
JSHint Web Documentation Scraper
Downloads comprehensive JSHint documentation from jshint.com website.
Includes configuration options, CLI, API, and FAQ documentation.
"""

import os
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser
import requests
import subprocess

# Base URL for JSHint documentation
BASE_URL = "https://jshint.com"

# Pages to scrape
PAGES_TO_SCRAPE = [
    "/docs/",
    "/docs/options/",
    "/docs/cli/",
    "/docs/api/",
    "/docs/reporters/",
    "/docs/faq/",
    "/install/",
    "/about/",
]

def fetch_page(url, timeout=10):
    """Fetch a page from JSHint website."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"    -> Error fetching {url}: {e}")
        return None


def extract_main_content(html_content, url):
    """Extract main content from HTML page."""
    try:
        # Use pandoc if available for better HTML to Markdown conversion
        try:
            process = subprocess.Popen(
                ['pandoc', '-f', 'html', '-t', 'markdown'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            markdown, _ = process.communicate(input=html_content, timeout=10)
            if process.returncode == 0:
                return markdown
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        # Fallback: Simple HTML tag stripping
        import re
        # Remove script and style tags
        text = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '\n', text)
        # Clean up whitespace
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r'[ \t]+', ' ', text)
        return text.strip()

    except Exception as e:
        print(f"    -> Error extracting content from {url}: {e}")
        return None


def get_filename_from_url(url):
    """Generate filename from URL."""
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    if not path or path == 'docs':
        return 'index.md'
    return path.replace('/', '-') + '.md'


def scrape_jshint_docs(output_dir):
    """Scrape JSHint documentation from website."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("\nScraping JSHint documentation...")
    successful_pages = 0

    for page_path in PAGES_TO_SCRAPE:
        url = urljoin(BASE_URL, page_path)
        filename = get_filename_from_url(url)

        print(f"  Fetching: {page_path}")

        # Fetch page
        html_content = fetch_page(url)
        if not html_content:
            continue

        # Extract content
        markdown_content = extract_main_content(html_content, url)
        if not markdown_content:
            continue

        # Add source header
        source_header = f"""# Source: {url}

"""
        final_content = source_header + markdown_content

        # Write to file
        output_file = output_dir / filename
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(final_content)
            print(f"    -> Saved: {filename} ({len(final_content)} bytes)")
            successful_pages += 1
        except Exception as e:
            print(f"    -> Error writing {filename}: {e}")

        # Rate limiting
        time.sleep(0.5)

    return successful_pages


def main():
    """Main function to scrape JSHint documentation."""
    print("=" * 70)
    print("JSHint Web Documentation Scraper")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "jshint"

    print(f"Base URL: {BASE_URL}")
    print(f"Output directory: {output_dir}")
    print()

    # Remove existing output directory if it exists
    if output_dir.exists():
        import shutil
        print(f"Removing existing output directory: {output_dir}")
        shutil.rmtree(output_dir)

    # Scrape documentation
    successful_pages = scrape_jshint_docs(output_dir)

    # Verify extraction
    print("\nVerifying extraction...")
    if not output_dir.exists():
        print("  Error: Output directory was not created")
        sys.exit(1)

    files = list(output_dir.glob("**/*"))
    files = [f for f in files if f.is_file()]
    total_size = sum(f.stat().st_size for f in files)

    print(f"  Total files: {len(files)}")
    print(f"  Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")

    if len(files) == 0:
        print("\n  Warning: No files found in output directory")
        sys.exit(1)

    # List files
    print("\n  Scraped documentation files:")
    for doc_file in sorted(files):
        file_size = doc_file.stat().st_size
        print(f"    - {doc_file.name} ({file_size:,} bytes)")

    print()
    print("=" * 70)
    print("Scraping Complete")
    print("=" * 70)
    print(f"Output: {output_dir}")
    print(f"Pages scraped: {successful_pages}")
    print()


if __name__ == "__main__":
    main()
