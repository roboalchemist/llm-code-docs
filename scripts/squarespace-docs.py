#!/usr/bin/env python3
"""
Squarespace Developer Documentation Scraper

Squarespace is a website builder and commerce platform that provides APIs
for custom development, including template customization, commerce APIs, and webhooks.

Source: https://developers.squarespace.com/
Output: docs/web-scraped/squarespace/
"""

import os
import sys
import requests
from pathlib import Path
import time
from urllib.parse import urljoin, urlparse
import re
import html
import html.parser

# Base URL for Squarespace Developer Documentation
BASE_URL = "https://developers.squarespace.com"

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "squarespace"

# Session for making requests
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

# Documentation pages to extract - organized by section
# Based on actual pages found in the Squarespace developer documentation
DOCS_PAGES = [
    # Home and Overview
    ("/", "index.md"),
    ("/quick-start", "quick-start.md"),

    # Quick Start / Template Docs - Start Here
    ("/guide/quick-start", "guide-quick-start.md"),
    ("/guide/beginner-tutorial", "guide-beginner-tutorial.md"),

    # The Basics
    ("/guide/template-overview", "guide-template-overview.md"),
    ("/guide/what-is-json", "guide-what-is-json.md"),
    ("/guide/view-json-data", "guide-view-json-data.md"),
    ("/guide/templating-basics", "guide-templating-basics.md"),

    # Template Files
    ("/guide/template-configuration", "guide-template-configuration.md"),
    ("/guide/layouts-regions", "guide-layouts-regions.md"),
    ("/guide/template-partials", "guide-template-partials.md"),
    ("/guide/menus-navigation", "guide-menus-navigation.md"),
    ("/guide/folders-indexes", "guide-folders-indexes.md"),
    ("/guide/collections", "guide-collections.md"),
    ("/guide/static-pages", "guide-static-pages.md"),

    # Template Language (JSON-T)
    ("/guide/json-t", "guide-json-t.md"),
    ("/guide/json-t-directives", "guide-json-t-directives.md"),
    ("/guide/json-t-predicates", "guide-json-t-predicates.md"),
    ("/guide/json-t-formatters", "guide-json-t-formatters.md"),
    ("/guide/json-t-helpers", "guide-json-t-helpers.md"),
    ("/guide/json-t-system-variables", "guide-json-t-system-variables.md"),

    # Squarespace Tags
    ("/guide/open-block-field", "guide-open-block-field.md"),
    ("/guide/navigation-tag", "guide-navigation-tag.md"),
    ("/guide/category-tag", "guide-category-tag.md"),
    ("/guide/custom-query-tag", "guide-custom-query-tag.md"),

    # JavaScript
    ("/guide/custom-javascript", "guide-custom-javascript.md"),
    ("/guide/image-loader", "guide-image-loader.md"),

    # Advanced
    ("/guide/local-development", "guide-local-development.md"),
    ("/guide/custom-post-types", "guide-custom-post-types.md"),
    ("/guide/template-annotations", "guide-template-annotations.md"),
    ("/guide/style-editor", "guide-style-editor.md"),
    ("/guide/error-reporting", "guide-error-reporting.md"),
    ("/guide/url-queries", "guide-url-queries.md"),

    # Commerce APIs
    ("/commerce-apis/overview", "commerce-overview.md"),
    ("/commerce-apis/getting-started", "commerce-getting-started.md"),
    ("/commerce-apis/orders-overview", "commerce-orders.md"),
    ("/commerce-apis/products-overview", "commerce-products.md"),
    ("/commerce-apis/inventory-overview", "commerce-inventory.md"),
    ("/commerce-apis/profiles-overview", "commerce-profiles.md"),

    # Webhooks
    ("/webhooks/overview", "webhooks-overview.md"),

    # Custom Code
    ("/custom-code/about", "custom-code-about.md"),

    # Changes & Updates
    ("/changes/upcoming-changes", "upcoming-changes.md"),
]

def fetch_page(url):
    """Fetch a page and return its content."""
    try:
        full_url = urljoin(BASE_URL, url)
        print(f"  Fetching: {full_url}")
        response = session.get(full_url, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"  Error fetching {url}: {e}")
        return None

def extract_text_from_html(html_content):
    """Extract text content from HTML, preserving structure."""
    if not html_content:
        return None

    # Simple HTML tag removal while preserving some structure
    # Remove script and style tags
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Remove comments
    html_content = re.sub(r'<!--.*?-->', '', html_content, flags=re.DOTALL)

    # Convert common block elements to markdown
    html_content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', html_content, flags=re.IGNORECASE | re.DOTALL)
    html_content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', html_content, flags=re.IGNORECASE | re.DOTALL)
    html_content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', html_content, flags=re.IGNORECASE | re.DOTALL)
    html_content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n#### \1\n', html_content, flags=re.IGNORECASE | re.DOTALL)
    html_content = re.sub(r'<h5[^>]*>(.*?)</h5>', r'\n##### \1\n', html_content, flags=re.IGNORECASE | re.DOTALL)
    html_content = re.sub(r'<h6[^>]*>(.*?)</h6>', r'\n###### \1\n', html_content, flags=re.IGNORECASE | re.DOTALL)

    # Convert paragraphs
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', html_content, flags=re.IGNORECASE | re.DOTALL)

    # Convert bold and italic
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.IGNORECASE | re.DOTALL)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.IGNORECASE | re.DOTALL)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.IGNORECASE | re.DOTALL)
    html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.IGNORECASE | re.DOTALL)

    # Convert code blocks
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.IGNORECASE | re.DOTALL)
    html_content = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```', html_content, flags=re.IGNORECASE | re.DOTALL)

    # Convert links
    html_content = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.IGNORECASE | re.DOTALL)

    # Convert lists
    html_content = re.sub(r'<ul[^>]*>', '', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</ul>', '', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<ol[^>]*>', '', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</ol>', '', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.IGNORECASE | re.DOTALL)

    # Convert line breaks
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Unescape HTML entities
    html_content = html.unescape(html_content)

    # Clean up whitespace
    lines = []
    for line in html_content.split('\n'):
        line = line.strip()
        if line:
            lines.append(line)

    return '\n\n'.join(lines)

def clean_markdown(content):
    """Clean and sanitize markdown content."""
    if not content:
        return content

    # Remove excessive blank lines
    content = re.sub(r'\n\n\n+', '\n\n', content)

    # Remove markdown links without text
    content = re.sub(r'\[\]\([^)]+\)', '', content)

    # Remove inline javascript
    content = re.sub(r'javascript:[^\s)]+', '', content)

    # Remove common navigation artifacts
    content = re.sub(r'\[Skip to content\].*?\n+', '', content)

    # Clean up leading/trailing whitespace per line
    lines = []
    for line in content.split('\n'):
        lines.append(line.rstrip())
    content = '\n'.join(lines)

    return content.strip()

def add_source_header(content, url):
    """Add source information to the beginning of the content."""
    full_url = urljoin(BASE_URL, url)
    header = f"""# Squarespace Developer Documentation
# Source: {full_url}

"""
    return header + content

def download_docs():
    """Download Squarespace developer documentation."""

    print(f"\nDownloading Squarespace Developer documentation...")
    print(f"Base URL: {BASE_URL}")
    print(f"Output directory: {OUTPUT_DIR}")

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    successful = 0
    failed = 0
    skipped = 0

    for url, filename in DOCS_PAGES:
        filepath = OUTPUT_DIR / filename

        # Skip if file already exists
        if filepath.exists():
            print(f"  Skipping {filename} (already exists)")
            skipped += 1
            continue

        html = fetch_page(url)
        if not html:
            print(f"  Failed to fetch {filename}")
            failed += 1
            continue

        content = extract_text_from_html(html)
        if not content or len(content.strip()) < 100:
            print(f"  No significant content extracted from {filename}")
            failed += 1
            continue

        # Add source header
        content = add_source_header(content, url)

        # Clean content
        content = clean_markdown(content)

        # Write to file
        try:
            filepath.write_text(content, encoding='utf-8')
            file_size = filepath.stat().st_size / 1024
            print(f"  Saved {filename} ({file_size:.1f} KB)")
            successful += 1
        except Exception as e:
            print(f"  Error writing {filename}: {e}")
            failed += 1

        # Rate limiting to be respectful to the server
        time.sleep(0.5)

    # Summary
    print(f"\nDownload complete!")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Skipped: {skipped}")

    total_files = len(list(OUTPUT_DIR.glob('*.md')))
    print(f"  Total files: {total_files}")

    if total_files > 0:
        total_size = sum(f.stat().st_size for f in OUTPUT_DIR.glob('*.md'))
        print(f"  Total size: {total_size / 1024 / 1024:.2f} MB")

    return successful > 0

if __name__ == "__main__":
    try:
        success = download_docs()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\nDownload interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
