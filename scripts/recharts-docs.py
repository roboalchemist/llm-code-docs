#!/usr/bin/env python3
"""
Recharts Documentation Scraper
Downloads all Recharts documentation pages from recharts.github.io and converts to markdown.
Recharts is a composable charting library built on React and D3.
Output: docs/web-scraped/recharts/
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse, urljoin
import time
import re
import subprocess
import xml.etree.ElementTree as ET

# Base configuration
BASE_URL = "https://recharts.github.io"
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "recharts"
DELAY_SECONDS = 0.5  # Be respectful to their server

def fetch_sitemap():
    """Fetch and parse the sitemap to get all documentation URLs."""
    print(f"Fetching sitemap from {SITEMAP_URL}...")
    try:
        response = requests.get(SITEMAP_URL, timeout=30)
        response.raise_for_status()

        # Parse XML
        root = ET.fromstring(response.content)

        # Extract all URLs (they don't have language prefix in sitemap)
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = []
        for url_elem in root.findall('.//ns:url/ns:loc', namespace):
            url = url_elem.text
            # Filter to only recharts.github.io URLs (no external links)
            if url.startswith(BASE_URL):
                # Convert to en-US version explicitly
                if url == BASE_URL or url == BASE_URL + '/':
                    urls.append(url)
                else:
                    # Add /en-US/ prefix to path
                    path = url.replace(BASE_URL, '')
                    en_us_url = f"{BASE_URL}/en-US{path}"
                    urls.append(en_us_url)

        # Sort for consistent ordering
        urls = sorted(set(urls))
        print(f"Found {len(urls)} documentation pages")
        return urls
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []

def sanitize_filename(url):
    """Convert URL to a safe filename."""
    # Remove BASE_URL
    path = url.replace(BASE_URL, '')

    # Remove /en-US/ prefix and /zh-CN/ prefix
    path = path.replace('/en-US/', '').replace('/zh-CN/', '')

    # Handle root page
    if not path or path == '/' or path == '/en-US' or path == '/en-US/':
        return 'index.md'

    # Remove leading/trailing slashes
    path = path.strip('/')

    # Replace slashes with underscores for nested paths
    path = path.replace('/', '_')

    # Ensure .md extension
    if not path.endswith('.md'):
        path = f"{path}.md"

    return path

def html_to_markdown(html_content, url):
    """Convert HTML to Markdown using pandoc, with fallback to basic conversion."""

    # Extract main content - Recharts uses React Router with main tag
    main_match = re.search(
        r'<main[^>]*>(.*?)</main>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if main_match:
        html_content = main_match.group(1)
    else:
        # Try article tag as fallback
        article_match = re.search(
            r'<article[^>]*>(.*?)</article>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if article_match:
            html_content = article_match.group(1)

    # Remove navigation elements
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<aside[^>]*>.*?</aside>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Try pandoc for conversion (best quality)
    try:
        result = subprocess.run(
            ['pandoc', '-f', 'html', '-t', 'markdown', '--wrap=none'],
            input=html_content,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            markdown = result.stdout
            # Clean up pandoc artifacts
            markdown = re.sub(r'^::+.*$', '', markdown, flags=re.MULTILINE)  # Remove ::: div markers
            markdown = re.sub(r'\{[^}]*\}', '', markdown)  # Remove {.class} attributes
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)  # Normalize whitespace
            markdown = markdown.strip()
            return f"# Source: {url}\n\n{markdown}"
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        print(f"  Pandoc conversion failed ({e}), using fallback")

    # Fallback: basic HTML to text extraction
    # Remove script and style elements
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Convert common HTML elements to markdown
    # Headers
    for i in range(6, 0, -1):
        html_content = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', r'\n' + '#' * i + r' \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Code blocks
    html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Links
    html_content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Bold and italic
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Lists
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<[ou]l[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</[ou]l>', '\n', html_content, flags=re.IGNORECASE)

    # Paragraphs and line breaks
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</div>', '\n', html_content, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Decode HTML entities
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&quot;', '"')
    html_content = html_content.replace('&#39;', "'")

    # Clean up whitespace
    html_content = re.sub(r'\n\s*\n\s*\n', '\n\n', html_content)
    html_content = html_content.strip()

    return f"# Source: {url}\n\n{html_content}"

def download_page(url):
    """Download a single page and convert to markdown."""
    try:
        print(f"  Downloading: {url}")
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # Convert to markdown
        markdown = html_to_markdown(response.text, url)

        # Save to file
        filename = sanitize_filename(url)
        filepath = OUTPUT_DIR / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  ✓ Saved to {filename}")
        return True
    except Exception as e:
        print(f"  ✗ Error downloading {url}: {e}")
        return False

def main():
    """Main scraper function."""
    print("=" * 70)
    print("Recharts Documentation Scraper")
    print("=" * 70)
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"✓ Created output directory: {OUTPUT_DIR}\n")

    # Fetch URLs from sitemap
    urls = fetch_sitemap()
    if not urls:
        print("✗ No URLs found in sitemap. Exiting.")
        return 1

    print(f"\nStarting download of {len(urls)} pages...")
    print(f"Delay between requests: {DELAY_SECONDS}s\n")

    # Download all pages
    success_count = 0
    fail_count = 0

    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}]")
        if download_page(url):
            success_count += 1
        else:
            fail_count += 1

        # Rate limiting
        if i < len(urls):  # Don't sleep after last page
            time.sleep(DELAY_SECONDS)

    # Summary
    print("\n" + "=" * 70)
    print("Download Summary")
    print("=" * 70)
    print(f"Total pages: {len(urls)}")
    print(f"Successful: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"Output directory: {OUTPUT_DIR}")
    print("=" * 70)

    return 0 if fail_count == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
