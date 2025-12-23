#!/usr/bin/env python3
"""
FastAPI Documentation Scraper
Downloads all FastAPI documentation pages and converts to markdown.
FastAPI is a modern, fast web framework for building APIs with Python.
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

BASE_URL = "https://fastapi.tiangolo.com"
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"


def get_pages_from_sitemap():
    """Fetch all English documentation pages from sitemap.xml."""
    print(f"Fetching sitemap from: {SITEMAP_URL}")

    try:
        response = requests.get(SITEMAP_URL, timeout=15)
        response.raise_for_status()

        # Parse XML sitemap
        root = ET.fromstring(response.content)

        # Extract URLs (handle XML namespace)
        ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = []

        for url in root.findall('.//ns:loc', ns):
            loc = url.text
            # Filter out non-English pages
            if any(lang in loc for lang in ['/de/', '/es/', '/pt/', '/ru/', '/zh/', '/fr/', '/ja/']):
                continue
            # Filter out special pages
            if '/_llm-test/' in loc:
                continue
            urls.append(loc)

        print(f"Found {len(urls)} English documentation pages")
        return urls

    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        sys.exit(1)


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # First, extract just the main article content to avoid nav/sidebar noise
    # MkDocs Material uses <article class="md-content__inner md-typeset">
    article_match = re.search(
        r'<article[^>]*class="[^"]*md-content__inner[^"]*"[^>]*>(.*?)</article>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if article_match:
        html_content = article_match.group(1)
    else:
        # Try alternate selector
        main_match = re.search(
            r'<div[^>]*class="[^"]*md-content[^"]*"[^>]*>(.*?)</div>\s*<script',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if main_match:
            html_content = main_match.group(1)

    # Remove tabbed content duplicates (MkDocs shows same content in tabs)
    html_content = re.sub(r'<div[^>]*class="[^"]*tabbed-block[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL)

    # Try pandoc on cleaned content
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
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: basic HTML to text extraction
    # Remove script and style elements
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Extract main content (MkDocs Material uses md-content class)
    main_match = re.search(r'<article[^>]*class="[^"]*md-content[^"]*"[^>]*>(.*?)</article>', html_content, flags=re.DOTALL | re.IGNORECASE)
    if main_match:
        html_content = main_match.group(1)

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


def download_page(url, output_path):
    """Download a page and convert to markdown."""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Convert HTML to markdown
        markdown = html_to_markdown(response.text, url)

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def url_to_filename(url):
    """Convert URL to filename."""
    # Remove base URL
    path = url.replace(BASE_URL, '')

    if path == "/" or path == "":
        return "index.md"

    # Remove leading/trailing slashes
    clean_path = path.strip("/")

    # Handle nested paths like /tutorial/first-steps/
    if "/" in clean_path:
        # Convert to flat filename: tutorial/first-steps -> tutorial-first-steps.md
        return clean_path.replace("/", "-") + ".md"

    return clean_path + ".md"


def main():
    """Main function to download all FastAPI documentation."""
    print("=" * 60)
    print("FastAPI Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print()

    # Get pages from sitemap
    pages = get_pages_from_sitemap()
    print(f"Pages to download: {len(pages)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "fastapi"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, url in enumerate(pages, 1):
        filename = url_to_filename(url)
        output_path = output_dir / filename

        print(f"[{i:3d}/{len(pages)}] {url}")

        if download_page(url, output_path):
            successful += 1
            print(f"  -> Saved: {filename}")
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.5)

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} pages failed to download")
        sys.exit(1)
    else:
        print("All pages downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
