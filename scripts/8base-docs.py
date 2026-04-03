#!/usr/bin/env python3
"""
8base Documentation Scraper

8base is a low-code platform for building full-stack JavaScript applications with GraphQL APIs.
This scraper extracts comprehensive documentation from docs.8base.com and converts to markdown.

Source: https://docs.8base.com/
Output: docs/web-scraped/8base/
"""

import os
import sys
import requests
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import re

# Base URL for 8base documentation
BASE_URL = "https://docs.8base.com"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "8base"

# Session for making requests
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

# Documentation structure - extracted from Docusaurus sidebar
DOCS_PAGES = [
    # Introduction
    ("/", "000-introduction.md"),
    ("/introduction/what-is-8base", "001-what-is-8base.md"),
    ("/introduction/who-uses-8base", "002-who-uses-8base.md"),
    ("/introduction/quickstart", "003-quickstart.md"),
    ("/introduction/main-modules-and-capabilities", "004-main-modules-capabilities.md"),
    ("/introduction/projects", "005-projects.md"),
    ("/introduction/backend-capabilities-overview", "006-backend-capabilities.md"),
    ("/introduction/frontend-capabilities-overview", "007-frontend-capabilities.md"),
    ("/introduction/built-application-architecture", "008-architecture.md"),
    ("/introduction/using-8base-at-scale", "009-at-scale.md"),
    ("/introduction/developer-resources", "010-developer-resources.md"),

    # Getting Started
    ("/gettingstarted", "100-getting-started.md"),

    # 8base Home
    ("/8basehome", "200-8base-home.md"),

    # Backend Development
    ("/backend", "300-backend-overview.md"),

    # Frontend Development
    ("/frontend", "400-frontend-overview.md"),

    # Advanced Development
    ("/advanced", "500-advanced-overview.md"),
]

def fetch_page(url):
    """Fetch a page and return its HTML content."""
    try:
        print(f"  Fetching: {url}")
        full_url = urljoin(BASE_URL, url)
        response = session.get(full_url, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"    Error fetching {url}: {e}")
        return None

def extract_main_content(html):
    """Extract main content from Docusaurus HTML page."""
    if not html:
        return None

    soup = BeautifulSoup(html, 'html.parser')

    # Docusaurus main content is typically in .theme-doc-markdown or similar
    # Look for the main article container
    content = None

    # Try multiple selectors for different Docusaurus versions
    selectors = [
        'article .theme-doc-markdown',
        'article [class*="markdown"]',
        'main .theme-doc-markdown',
        'main article',
        'article',
    ]

    for selector in selectors:
        try:
            content = soup.select_one(selector)
            if content and content.get_text(strip=True):
                break
        except:
            pass

    if not content:
        return None

    # Extract title
    title = None
    h1 = content.find('h1')
    if h1:
        title = h1.get_text(strip=True)

    # Convert HTML to markdown-like format
    text = content.get_text(separator='\n', strip=True)

    # Clean up excessive whitespace
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    text = '\n'.join(lines)

    return text

def save_page(url, filename, html_content):
    """Save page content to file."""
    try:
        text = extract_main_content(html_content)
        if not text:
            print(f"    Warning: No content extracted from {url}")
            return False

        # Add metadata header
        header = f"""# Source: {urljoin(BASE_URL, url)}

"""
        content = header + text

        # Create output directory
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Write file
        output_path = OUTPUT_DIR / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {filename}")
        return True

    except Exception as e:
        print(f"    Error saving {filename}: {e}")
        return False

def main():
    """Main function to download all 8base documentation."""
    print("=" * 70)
    print("8base Documentation Scraper")
    print("=" * 70)
    print()

    print(f"Base URL: {BASE_URL}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, (url, filename) in enumerate(DOCS_PAGES, 1):
        print(f"[{idx:3d}/{len(DOCS_PAGES)}] ", end="")

        html = fetch_page(url)
        if html and save_page(url, filename, html):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.5)

    # Create index file
    print(f"\n[{len(DOCS_PAGES)+1}] Creating index...")
    create_index()

    elapsed = time.time() - start_time

    print()
    print("=" * 70)
    print("Download Summary")
    print("=" * 70)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {OUTPUT_DIR}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in OUTPUT_DIR.glob("*"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
    print()

    if failed > 0:
        print(f"Warning: {failed} pages failed to download")
        sys.exit(1)
    else:
        print("All documentation downloaded successfully!")
        sys.exit(0)

def create_index():
    """Create an index.md file listing all docs."""
    index_content = """# 8base Documentation Index

Welcome to the 8base comprehensive documentation archive.

8base is a powerful low-code platform designed for building full-stack JavaScript applications.

## Documentation Structure

### Introduction
- What is 8base?
- Who uses 8base?
- Quickstart guide
- Main modules and capabilities
- Projects overview
- Backend capabilities
- Frontend capabilities
- Application architecture
- Using 8base at scale
- Developer resources

### Getting Started
Start building your first 8base application

### 8base Home
Platform overview and workspace management

### Backend Development
Learn how to build backend services with 8base

### Frontend Development
Learn how to build frontend applications with 8base

### Advanced Development
Advanced patterns and techniques

## Source
Documentation extracted from: https://docs.8base.com/
"""

    index_path = OUTPUT_DIR / "index.md"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("    -> Created index.md")

if __name__ == "__main__":
    main()
