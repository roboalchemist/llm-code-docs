#!/usr/bin/env python3
"""
Cloudflare API documentation scraper.
Fetches API reference documentation from https://developers.cloudflare.com/api/
"""

import os
import sys
import re
import json
from pathlib import Path
from urllib.parse import urljoin, urlparse
from collections import defaultdict
import time
from html.parser import HTMLParser
from io import StringIO

# Try to import requests, fall back to urllib if not available
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    import urllib.request
    HAS_REQUESTS = False

# Configuration
BASE_URL = "https://developers.cloudflare.com/api"
TARGET_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "cloudflare-api"
MAX_PAGES = 150
REQUEST_TIMEOUT = 15
RATE_LIMIT_DELAY = 0.3  # seconds between requests

# Create target directory if it doesn't exist
TARGET_DIR.mkdir(parents=True, exist_ok=True)

class HTMLToMarkdown(HTMLParser):
    """Simple HTML to Markdown converter."""

    def __init__(self):
        super().__init__()
        self.output = StringIO()
        self.tag_stack = []
        self.in_code = False
        self.in_pre = False

    def handle_starttag(self, tag, attrs):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            self.output.write('\n' + '#' * level + ' ')
        elif tag == 'p':
            self.output.write('\n')
        elif tag == 'br':
            self.output.write('\n')
        elif tag in ['strong', 'b']:
            self.output.write('**')
        elif tag in ['em', 'i']:
            self.output.write('*')
        elif tag == 'code':
            self.output.write('`')
            self.in_code = True
        elif tag == 'pre':
            self.output.write('\n```\n')
            self.in_pre = True
        elif tag == 'a':
            self.output.write('[')
        elif tag == 'li':
            self.output.write('\n- ')
        elif tag == 'ul':
            self.output.write('\n')
        elif tag == 'ol':
            self.output.write('\n')
        elif tag == 'blockquote':
            self.output.write('\n> ')
        elif tag in ['table', 'tbody', 'tr', 'td', 'th']:
            pass  # Simplified - skip tables
        self.tag_stack.append(tag)

    def handle_endtag(self, tag):
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()

        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.output.write('\n')
        elif tag == 'p':
            self.output.write('\n')
        elif tag in ['strong', 'b']:
            self.output.write('**')
        elif tag in ['em', 'i']:
            self.output.write('*')
        elif tag == 'code':
            self.output.write('`')
            self.in_code = False
        elif tag == 'pre':
            self.output.write('\n```\n')
            self.in_pre = False
        elif tag == 'a':
            self.output.write(']')
        elif tag in ['ul', 'ol']:
            self.output.write('\n')
        elif tag == 'blockquote':
            self.output.write('\n')

    def handle_data(self, data):
        # Skip script and style content
        if self.tag_stack and self.tag_stack[-1] in ['script', 'style']:
            return
        self.output.write(data)

    def get_markdown(self):
        return self.output.getvalue()

def get_page(url):
    """Fetch a page with retry logic."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; LLM-Code-Docs/1.0)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }

    try:
        if HAS_REQUESTS:
            response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            return response.text
        else:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as response:
                return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None

def extract_api_content(html, url):
    """Extract main content from HTML page."""
    # Try to find main content area
    patterns = [
        r'<main[^>]*>(.*?)</main>',
        r'<article[^>]*>(.*?)</article>',
        r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>',
    ]

    content = None
    for pattern in patterns:
        match = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
        if match:
            content = match.group(1)
            break

    if not content:
        # Fallback to body
        match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)
        if match:
            content = match.group(1)
        else:
            return None

    # Remove navigation, script, style tags
    content = re.sub(r'<nav[^>]*>.*?</nav>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<footer[^>]*>.*?</footer>', '', content, flags=re.DOTALL | re.IGNORECASE)

    return content

def html_to_markdown(html_content):
    """Convert HTML to markdown."""
    if not html_content:
        return ""

    # Remove HTML comments
    html_content = re.sub(r'<!--.*?-->', '', html_content, flags=re.DOTALL)

    # Convert line breaks
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)

    # Remove tags we don't want to convert
    html_content = re.sub(r'<svg[^>]*>.*?</svg>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<button[^>]*>.*?</button>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Use the HTML parser
    parser = HTMLToMarkdown()
    try:
        parser.feed(html_content)
    except Exception as e:
        print(f"Warning: HTML parsing error: {e}", file=sys.stderr)
        return ""

    markdown = parser.get_markdown()

    # Clean up markdown
    # Remove excessive blank lines
    markdown = re.sub(r'\n\n\n+', '\n\n', markdown)
    # Remove trailing whitespace on lines
    markdown = '\n'.join(line.rstrip() for line in markdown.split('\n'))

    return markdown.strip()

def get_title_from_html(html):
    """Extract page title from HTML."""
    # Try to find title tag
    match = re.search(r'<title[^>]*>([^<]+)</title>', html, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # Try to find h1
    match = re.search(r'<h1[^>]*>([^<]+)</h1>', html, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    return ""

def sanitize_filename(url):
    """Generate filename from URL."""
    path = urlparse(url).path.replace('/api/', '').rstrip('/')

    if not path or path == 'api':
        return 'index.md'

    # Convert path to filename
    filename = path.replace('/', '_')
    # Remove invalid characters
    filename = re.sub(r'[^\w_-]', '', filename)
    # Limit length
    filename = filename[:100]

    return f"{filename}.md"

def scrape_api_reference():
    """Main scraping function."""
    print(f"Starting Cloudflare API documentation scrape...")
    print(f"Target: {TARGET_DIR}")
    print()

    visited = set()
    to_visit = [f"{BASE_URL}/"]
    pages_saved = 0
    failed = 0

    while to_visit and pages_saved < MAX_PAGES:
        url = to_visit.pop(0)

        if url in visited:
            continue

        visited.add(url)

        # Only process URLs under the API domain
        if not url.startswith(BASE_URL):
            continue

        # Skip non-content URLs
        if any(skip in url for skip in ['.xml', '.css', '.js', '.svg', '._astro', '.woff', '.woff2']):
            continue

        print(f"[{pages_saved}] Fetching: {url}")
        html = get_page(url)

        if not html:
            failed += 1
            continue

        # Extract title
        title = get_title_from_html(html)

        # Extract markdown
        content_html = extract_api_content(html, url)
        if content_html:
            markdown_content = html_to_markdown(content_html)
        else:
            markdown_content = ""

        if markdown_content and len(markdown_content) > 50:
            # Generate filename
            filename = sanitize_filename(url)
            filepath = TARGET_DIR / filename

            # Prepend source and title
            full_content = f"# {title}\n\nSource: {url}\n\n{markdown_content}"

            # Write to file
            filepath.write_text(full_content, encoding='utf-8')
            pages_saved += 1
            size_kb = len(full_content) / 1024
            print(f"  -> {filename} ({size_kb:.1f} KB)")

        # Find new links to visit
        links = re.findall(r'href=[\'"]((?:/api/[^\'"]*)[\'"])>', html)
        for href in links:
            href = href.strip('"\'')
            absolute_url = urljoin(BASE_URL, href)

            # Only follow API documentation links
            if absolute_url.startswith(BASE_URL) and absolute_url not in visited:
                # Remove fragments
                absolute_url = absolute_url.split('#')[0]
                if absolute_url not in to_visit and len(to_visit) < 500:
                    to_visit.append(absolute_url)

        time.sleep(RATE_LIMIT_DELAY)

    print()
    print(f"Scrape complete!")
    print(f"Pages saved: {pages_saved}")
    print(f"Failed: {failed}")
    print(f"Visited: {len(visited)}")

    return pages_saved

if __name__ == '__main__':
    try:
        count = scrape_api_reference()
        sys.exit(0 if count > 0 else 1)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
