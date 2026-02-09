#!/usr/bin/env python3
"""
Scraper for GritQL documentation from docs.grit.io
Output: docs/web-scraped/gritql/

GritQL is a query language for structural code search and transformation
from grit.io. This scraper downloads the official documentation from
the public docs site.
"""

import requests
import json
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse
import time
from typing import Optional

# Configuration
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "gritql"
BASE_URL = "https://docs.grit.io"

# Key documentation pages to scrape (from sitemap)
DOCUMENTATION_PAGES = [
    "/",
    "/cli/quickstart",
    "/cli/reference",
    "/patterns",
    "/guides/config",
    "/language/overview",
    "/tutorials/gritql",
    "/language/patterns",
    "/language/conditions",
    "/language/modifiers",
    "/language/target-languages",
    "/language/bubble",
    "/guides/patterns",
    "/language/functions",
    "/language/idioms",
    "/language/syntax",
    "/guides/testing",
    "/guides/ci",
    "/guides/authoring",
    "/guides/imports",
    "/guides/vscode",
    "/guides/sharing",
    "/blog",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def clean_url(url: str) -> str:
    """Remove query parameters and fragments from URL."""
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"


def extract_markdown_from_html(html: str, title: str = "") -> str:
    """
    Extract markdown content from HTML page.
    Uses basic HTML to markdown conversion with readability improvements.
    """
    markdown = ""

    # Add source header
    markdown += f"# Source: {BASE_URL}\n\n"

    # Add title
    if title:
        markdown += f"# {title}\n\n"

    # Remove script and style elements
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)

    # Extract main content
    # Look for common content containers
    main_patterns = [
        r'<main[^>]*>(.*?)</main>',
        r'<article[^>]*>(.*?)</article>',
        r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>',
        r'<div[^>]*id="[^"]*content[^"]*"[^>]*>(.*?)</div>',
    ]

    content_html = html
    for pattern in main_patterns:
        match = re.search(pattern, html, flags=re.DOTALL | re.IGNORECASE)
        if match:
            content_html = match.group(1)
            break

    # Basic HTML to markdown conversion
    # Headings
    content_html = re.sub(r'<h1[^>]*>([^<]+)</h1>', r'\n# \1\n', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'<h2[^>]*>([^<]+)</h2>', r'\n## \1\n', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'<h3[^>]*>([^<]+)</h3>', r'\n### \1\n', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'<h4[^>]*>([^<]+)</h4>', r'\n#### \1\n', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'<h5[^>]*>([^<]+)</h5>', r'\n##### \1\n', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'<h6[^>]*>([^<]+)</h6>', r'\n###### \1\n', content_html, flags=re.IGNORECASE)

    # Code blocks
    content_html = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', content_html, flags=re.DOTALL | re.IGNORECASE)
    content_html = re.sub(r'<code[^>]*>([^<]+)</code>', r'`\1`', content_html, flags=re.IGNORECASE)

    # Inline code (but not already converted)
    content_html = re.sub(r'<code[^>]*>([^<]+)</code>', r'`\1`', content_html, flags=re.IGNORECASE)

    # Lists
    content_html = re.sub(r'<ul[^>]*>', '', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'</ul>', '', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'<li[^>]*>', '- ', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'</li>', '\n', content_html, flags=re.IGNORECASE)

    content_html = re.sub(r'<ol[^>]*>', '', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'</ol>', '', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'<li[^>]*>', '1. ', content_html, flags=re.IGNORECASE)

    # Paragraphs and breaks
    content_html = re.sub(r'</p>', '\n', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'<p[^>]*>', '', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'<br\s*/?>', '\n', content_html, flags=re.IGNORECASE)

    # Links
    content_html = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>([^<]+)</a>', r'[\2](\1)', content_html, flags=re.IGNORECASE)

    # Strong and emphasis
    content_html = re.sub(r'<strong[^>]*>([^<]+)</strong>', r'**\1**', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'<b[^>]*>([^<]+)</b>', r'**\1**', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'<em[^>]*>([^<]+)</em>', r'*\1*', content_html, flags=re.IGNORECASE)
    content_html = re.sub(r'<i[^>]*>([^<]+)</i>', r'*\1*', content_html, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    content_html = re.sub(r'<[^>]+>', '', content_html)

    # Clean up HTML entities
    content_html = content_html.replace('&nbsp;', ' ')
    content_html = content_html.replace('&lt;', '<')
    content_html = content_html.replace('&gt;', '>')
    content_html = content_html.replace('&amp;', '&')
    content_html = content_html.replace('&quot;', '"')
    content_html = content_html.replace('&#39;', "'")

    # Clean up whitespace
    content_html = re.sub(r'\n\s*\n\s*\n+', '\n\n', content_html)
    content_html = content_html.strip()

    markdown += content_html
    return markdown


def get_page_title(html: str, url: str) -> str:
    """Extract page title from HTML."""
    # Try title tag
    match = re.search(r'<title[^>]*>([^<]+)</title>', html, flags=re.IGNORECASE)
    if match:
        title = match.group(1).strip()
        # Remove site name suffix
        title = re.sub(r'\s*[\|-]\s*(Grit|GritQL).*$', '', title)
        if title:
            return title

    # Try og:title meta tag
    match = re.search(r'<meta\s+property="og:title"\s+content="([^"]+)"', html, flags=re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # Try h1 tag
    match = re.search(r'<h1[^>]*>([^<]+)</h1>', html, flags=re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # Fallback to URL path
    path = urlparse(url).path.strip('/')
    if path:
        return ' '.join(p.replace('-', ' ').title() for p in path.split('/'))

    return "GritQL Documentation"


def fetch_page(url: str) -> Optional[str]:
    """Fetch a page and return HTML content."""
    try:
        print(f"  Fetching: {url}", flush=True)
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"  Error fetching {url}: {e}", flush=True)
        return None


def save_markdown(filename: str, content: str) -> None:
    """Save markdown content to file."""
    filepath = OUTPUT_DIR / filename
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(content, encoding='utf-8')
    print(f"  Saved: {filename} ({len(content)} bytes)", flush=True)


def scrape_documentation() -> None:
    """Scrape GritQL documentation from docs.grit.io"""

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Scraping GritQL documentation from {BASE_URL}...")
    print(f"Output directory: {OUTPUT_DIR}\n")

    successful = 0
    failed = 0

    for page_path in DOCUMENTATION_PAGES:
        url = urljoin(BASE_URL, page_path)

        # Convert page path to filename
        if page_path == "/" or page_path == "":
            filename = "index.md"
        else:
            # e.g., /language/overview -> language_overview.md
            filename = page_path.strip('/').replace('/', '_') + ".md"

        html = fetch_page(url)
        if html:
            title = get_page_title(html, url)
            markdown = extract_markdown_from_html(html, title)

            if markdown and len(markdown) > 200:  # Ensure reasonable content
                save_markdown(filename, markdown)
                successful += 1
            else:
                print(f"  Skipped {filename}: Insufficient content", flush=True)
                failed += 1
        else:
            print(f"  Failed to fetch {filename}", flush=True)
            failed += 1

        # Rate limiting
        time.sleep(0.5)

    print(f"\n{'='*60}")
    print(f"Scraping complete: {successful} successful, {failed} failed")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Total files: {len(list(OUTPUT_DIR.glob('*.md')))}")


if __name__ == '__main__':
    scrape_documentation()
