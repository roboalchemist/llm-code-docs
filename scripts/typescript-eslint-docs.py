#!/usr/bin/env python3
"""
typescript-eslint Documentation Scraper

Scrapes documentation from https://typescript-eslint.io/
Output: docs/web-scraped/typescript-eslint/
"""

import os
import sys
import time
import requests
from pathlib import Path
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser
import json
import re


class LinkExtractor(HTMLParser):
    """Extract links from HTML content."""

    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href' and value:
                    # Only collect relative links to typescript-eslint.io
                    if value.startswith('/'):
                        full_url = urljoin(self.base_url, value)
                        if 'typescript-eslint.io' in full_url and '#' not in full_url:
                            self.links.add(full_url)


class HTMLToMarkdown:
    """Simple HTML to Markdown converter for documentation."""

    @staticmethod
    def convert(html_content, url):
        """Convert HTML to markdown format."""
        # Remove script and style tags
        html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL)

        # Extract main content (docusaurus main content)
        main_match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL)
        if main_match:
            html_content = main_match.group(1)

        # Remove navigation and sidebars
        html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<aside[^>]*>.*?</aside>', '', html_content, flags=re.DOTALL)

        # Convert headers
        html_content = re.sub(r'<h([1-6])[^>]*>(.*?)</h[1-6]>', lambda m: '#' * int(m.group(1)) + ' ' + m.group(2).strip(), html_content, flags=re.DOTALL)

        # Convert code blocks
        html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL)

        # Convert bold and italics
        html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.DOTALL)

        # Convert links
        html_content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL)

        # Convert lists
        html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', html_content, flags=re.DOTALL)

        # Convert line breaks
        html_content = re.sub(r'<br\s*/?>', '\n', html_content)
        html_content = re.sub(r'</p>', '\n', html_content)
        html_content = re.sub(r'<p[^>]*>', '', html_content)

        # Remove HTML tags
        html_content = re.sub(r'<[^>]+>', '', html_content)

        # Decode HTML entities
        html_content = html_content.replace('&nbsp;', ' ')
        html_content = html_content.replace('&lt;', '<')
        html_content = html_content.replace('&gt;', '>')
        html_content = html_content.replace('&amp;', '&')
        html_content = html_content.replace('&quot;', '"')
        html_content = html_content.replace('&#39;', "'")

        # Clean up whitespace
        lines = [line.strip() for line in html_content.split('\n')]
        html_content = '\n'.join(line for line in lines if line)

        # Add source header
        markdown = f"# Source: {url}\n\n{html_content}"
        return markdown


def scrape_typescript_eslint():
    """Scrape typescript-eslint documentation."""
    print("=" * 70)
    print("typescript-eslint Documentation Scraper")
    print("=" * 70)
    print()

    base_url = "https://typescript-eslint.io"

    # Paths
    repo_dir = Path(__file__).parent.parent
    output_dir = repo_dir / "docs" / "web-scraped" / "typescript-eslint"

    print(f"Base URL: {base_url}")
    print(f"Output directory: {output_dir}")
    print()

    # Remove old output directory
    if output_dir.exists():
        print(f"Removing existing directory: {output_dir}")
        import shutil
        shutil.rmtree(output_dir)

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Created output directory: {output_dir}")
    print()

    # URLs to scrape
    urls_to_scrape = {
        base_url + "/getting-started/",
        base_url + "/linting/",
        base_url + "/rules/",
        base_url + "/typed-linting/",
        base_url + "/blog/",
    }

    visited_urls = set()
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })

    total_pages = 0
    total_size = 0

    print("Starting crawl...")
    print()

    while urls_to_scrape:
        url = urls_to_scrape.pop()

        if url in visited_urls:
            continue

        visited_urls.add(url)

        # Skip non-typescript-eslint URLs
        if 'typescript-eslint.io' not in url:
            continue

        # Skip playground and other non-docs sections
        if any(skip in url for skip in ['/play', '/discord', '/github']):
            continue

        print(f"Scraping: {url}")

        try:
            response = session.get(url, timeout=10)
            response.raise_for_status()
        except Exception as e:
            print(f"  Error: {e}")
            continue

        # Extract links for further crawling
        link_extractor = LinkExtractor(base_url)
        try:
            link_extractor.feed(response.text)
            for link in link_extractor.links:
                if link not in visited_urls:
                    urls_to_scrape.add(link)
        except Exception as e:
            print(f"  Warning: Could not extract links: {e}")

        # Convert HTML to Markdown
        try:
            markdown = HTMLToMarkdown.convert(response.text, url)
        except Exception as e:
            print(f"  Error converting to markdown: {e}")
            continue

        # Generate filename from URL
        parsed_url = urlparse(url)
        path_parts = parsed_url.path.strip('/').split('/')

        if not path_parts or path_parts[-1] == '':
            filename = 'index.md'
        else:
            filename = path_parts[-1]
            if not filename.endswith('.md'):
                filename += '.md'

        # Create subdirectories if needed
        if len(path_parts) > 1:
            subdir = output_dir / '/'.join(path_parts[:-1])
            subdir.mkdir(parents=True, exist_ok=True)
            filepath = subdir / filename
        else:
            filepath = output_dir / filename

        # Write markdown file
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown)

            file_size = filepath.stat().st_size
            total_size += file_size
            total_pages += 1
            print(f"  Saved: {filepath.relative_to(repo_dir)} ({file_size} bytes)")
        except Exception as e:
            print(f"  Error writing file: {e}")

        # Rate limiting
        time.sleep(0.5)

    print()
    print("=" * 70)
    print("Extraction Summary")
    print("=" * 70)
    print(f"Total pages scraped: {total_pages}")
    print(f"Total size: {total_size:,} bytes ({total_size / 1024 / 1024:.2f} MB)")
    print(f"Output directory: {output_dir}")
    print()

    if total_pages > 0:
        print("Success! Documentation extracted.")
        return 0
    else:
        print("Warning: No pages were scraped.")
        return 1


if __name__ == "__main__":
    sys.exit(scrape_typescript_eslint())
