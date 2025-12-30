#!/usr/bin/env python3
"""
MLX Documentation Scraper
Downloads MLX (Apple's machine learning framework) documentation and converts to markdown.
Source: https://ml-explore.github.io/mlx/build/html/
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse, urljoin
import time
import re
import subprocess
from bs4 import BeautifulSoup

BASE_URL = "https://ml-explore.github.io/mlx/build/html/"

# Track visited URLs to avoid duplicates
visited_urls = set()
docs_to_download = []


def html_to_markdown(html_content, url):
    """Convert HTML to markdown using pandoc if available."""
    # First, extract just the main content (Sphinx uses div.body or div.document)
    soup = BeautifulSoup(html_content, 'html.parser')

    # Try to find the main content area
    main_content = soup.find('div', class_='body') or \
                   soup.find('div', class_='document') or \
                   soup.find('div', role='main') or \
                   soup.find('main')

    if main_content:
        html_content = str(main_content)

    # Try pandoc first
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
            markdown = re.sub(r'^::+.*$', '', markdown, flags=re.MULTILINE)
            markdown = re.sub(r'\{[^}]*\}', '', markdown)
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)
            markdown = markdown.strip()
            return f"# Source: {url}\n\n{markdown}"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: basic HTML to text extraction
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Convert common HTML elements to markdown
    for i in range(6, 0, -1):
        html_content = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', r'\n' + '#' * i + r' \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)

    html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<[ou]l[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</[ou]l>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</div>', '\n', html_content, flags=re.IGNORECASE)
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


def is_valid_doc_url(url):
    """Check if URL is a valid documentation page."""
    # Must be under the base URL
    if not url.startswith(BASE_URL):
        return False

    # Must be HTML
    if not url.endswith('.html'):
        return False

    # Skip index pages and special pages
    skip_patterns = [
        'genindex.html',
        'search.html',
        'py-modindex.html',
        '_sources/',
        '_static/',
        '_images/',
    ]

    for pattern in skip_patterns:
        if pattern in url:
            return False

    return True


def crawl_page(url, max_depth=3, current_depth=0):
    """Crawl a page and find all documentation links."""
    if url in visited_urls or current_depth > max_depth:
        return

    visited_urls.add(url)

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Add this page to download list
        if is_valid_doc_url(url):
            docs_to_download.append(url)

        # Parse page to find more links
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a', href=True):
            href = link['href']
            # Convert relative URLs to absolute
            absolute_url = urljoin(url, href)

            # Remove anchor fragments
            absolute_url = absolute_url.split('#')[0]

            if is_valid_doc_url(absolute_url) and absolute_url not in visited_urls:
                # Recursively crawl
                crawl_page(absolute_url, max_depth, current_depth + 1)

    except Exception as e:
        print(f"Error crawling {url}: {e}", file=sys.stderr)


def url_to_filename(url):
    """Convert URL to a safe filename."""
    # Remove base URL
    path = url.replace(BASE_URL, '')

    # Remove .html extension
    path = path.replace('.html', '')

    # Handle index
    if path == '' or path == 'index':
        return 'index.md'

    # Convert path separators to hyphens
    # e.g., python/_autosummary/mlx.core.abs -> python-_autosummary-mlx.core.abs.md
    filename = path.replace('/', '-')

    return filename + '.md'


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

    except Exception as e:
        print(f"  -> Error: {e}")
        return False


def main():
    """Main function to crawl and download all MLX documentation."""
    print("=" * 60)
    print("MLX Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "mlx"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Step 1: Crawl to discover all documentation pages
    print("Step 1: Discovering documentation pages...")
    start_crawl = time.time()

    # Start from main index and key entry points
    entry_points = [
        BASE_URL + 'index.html',
        BASE_URL + 'install.html',
        BASE_URL + 'python/index.html',
        BASE_URL + 'cpp/index.html',
        BASE_URL + 'examples/index.html',
        BASE_URL + 'dev/index.html',
    ]

    for entry_point in entry_points:
        crawl_page(entry_point, max_depth=3)

    crawl_time = time.time() - start_crawl
    print(f"Found {len(docs_to_download)} documentation pages in {crawl_time:.1f}s")
    print()

    # Step 2: Download all discovered pages
    print("Step 2: Downloading documentation...")
    print()

    successful = 0
    failed = 0
    start_download = time.time()

    for i, url in enumerate(sorted(set(docs_to_download)), 1):
        filename = url_to_filename(url)
        output_path = output_dir / filename

        print(f"[{i:3d}/{len(docs_to_download)}] {filename[:50]:50s} ", end="", flush=True)

        if download_page(url, output_path):
            successful += 1
            print("✓")
        else:
            failed += 1
            print("✗")

        # Be respectful with rate limiting
        time.sleep(0.3)

    download_time = time.time() - start_download
    total_time = crawl_time + download_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Crawl time: {crawl_time:.1f}s")
    print(f"Download time: {download_time:.1f}s")
    print(f"Total time: {total_time:.1f}s")
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
