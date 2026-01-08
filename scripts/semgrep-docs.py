#!/usr/bin/env python3
"""
Scraper for Semgrep documentation.
Fetches from https://semgrep.dev/docs/ and converts to markdown.
Output: docs/web-scraped/semgrep/
"""

import requests
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser

# Configuration
BASE_URL = "https://semgrep.dev/docs/"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "semgrep"
SESSION = requests.Session()
SESSION.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
})

# Track visited URLs to avoid duplicates
VISITED_URLS = set()
MAX_PAGES = 100


class DocLinkExtractor(HTMLParser):
    """Extract documentation links from HTML."""

    def __init__(self):
        super().__init__()
        self.links = set()
        self.in_sidebar = False
        self.in_article = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'aside':
            self.in_sidebar = True
        elif tag == 'article':
            self.in_article = True
        elif tag == 'a' and 'href' in attrs_dict:
            href = attrs_dict['href']
            if href.startswith('/docs/') and not href.endswith('.xml'):
                # Normalize URLs
                full_url = urljoin(BASE_URL, href)
                self.links.add(full_url)

    def handle_endtag(self, tag):
        if tag == 'aside':
            self.in_sidebar = False
        elif tag == 'article':
            self.in_article = False


def extract_content_from_html(html_content):
    """Extract main content from HTML page."""
    # Look for article content
    article_match = re.search(r'<article[^>]*>(.*?)</article>', html_content, re.DOTALL)
    if article_match:
        content = article_match.group(1)
    else:
        # Fallback: look for main content div
        main_match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL)
        content = main_match.group(1) if main_match else html_content

    # Remove script and style tags
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)

    # Extract title
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    title = title_match.group(1) if title_match else "Documentation"
    title = re.sub(r'<[^>]+>', '', title).strip()

    # Basic HTML to Markdown conversion
    # Convert headers
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', content, flags=re.DOTALL)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h5[^>]*>(.*?)</h5>', r'##### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h6[^>]*>(.*?)</h6>', r'###### \1', content, flags=re.DOTALL)

    # Convert paragraphs
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL)

    # Convert links
    content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.DOTALL)

    # Convert code blocks
    content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```', content, flags=re.DOTALL)
    content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', content, flags=re.DOTALL)

    # Convert lists
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', content, flags=re.DOTALL)

    # Convert bold and italic
    content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.DOTALL)

    # Remove remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Clean up whitespace
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    content = content.strip()

    return title, content


def fetch_url(url):
    """Fetch a single URL and return the content."""
    try:
        response = SESSION.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def get_url_slug(url):
    """Convert URL to a filename slug."""
    path = urlparse(url).path
    # Remove /docs/ prefix
    path = path.replace('/docs/', '').rstrip('/')
    if not path or path == '':
        path = 'index'
    # Replace slashes with dashes
    path = path.replace('/', '-')
    return path


def scrape_docs():
    """Main scraping function."""
    print("Semgrep Documentation Scraper")
    print("=" * 70)
    print(f"Base URL: {BASE_URL}")
    print(f"Output directory: {OUTPUT_DIR}")
    print("=" * 70)

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Start with the main docs page
    to_visit = [BASE_URL]
    pages_scraped = 0

    while to_visit and pages_scraped < MAX_PAGES:
        current_url = to_visit.pop(0)

        if current_url in VISITED_URLS:
            continue

        VISITED_URLS.add(current_url)
        pages_scraped += 1

        print(f"\n[{pages_scraped}/{MAX_PAGES}] Fetching: {current_url}")

        html_content = fetch_url(current_url)
        if not html_content:
            continue

        # Extract title and content
        try:
            title, markdown_content = extract_content_from_html(html_content)
        except Exception as e:
            print(f"  Error extracting content: {e}")
            continue

        # Save to file
        slug = get_url_slug(current_url)
        if not slug:
            slug = 'index'

        filename = OUTPUT_DIR / f"{slug}.md"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"Source: {current_url}\n\n")
                f.write(markdown_content)
            print(f"  Saved: {filename.name}")
        except Exception as e:
            print(f"  Error saving file: {e}")
            continue

        # Extract links from this page
        extractor = DocLinkExtractor()
        try:
            extractor.feed(html_content)
        except Exception as e:
            print(f"  Error extracting links: {e}")

        # Add new links to visit queue
        for link in extractor.links:
            if link not in VISITED_URLS and len(to_visit) < 200:
                to_visit.append(link)

    print("\n" + "=" * 70)
    print(f"Scraping completed!")
    print(f"Pages scraped: {pages_scraped}")
    print(f"Files saved to: {OUTPUT_DIR}")
    print("=" * 70)

    # Print sample of saved files
    markdown_files = list(OUTPUT_DIR.glob("*.md"))
    if markdown_files:
        print(f"\nSaved {len(markdown_files)} documentation files:")
        for f in sorted(markdown_files)[:10]:
            size = f.stat().st_size
            print(f"  - {f.name} ({size:,} bytes)")
        if len(markdown_files) > 10:
            print(f"  ... and {len(markdown_files) - 10} more files")


if __name__ == "__main__":
    scrape_docs()
