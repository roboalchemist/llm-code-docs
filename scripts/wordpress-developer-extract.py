#!/usr/bin/env python3
"""
Scraper for WordPress Developer Documentation from developer.wordpress.org

Extracts comprehensive developer documentation covering:
- Plugin Development Handbook
- Theme Development Handbook
- REST API Reference
- Block Editor / Gutenberg Documentation
- Common APIs
- WP-CLI Documentation
- Code Standards

Output: docs/web-scraped/wordpress-developer/
"""

import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from collections import defaultdict
import requests
from bs4 import BeautifulSoup

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "wordpress-developer"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Base URL and key documentation sections to scrape
BASE_URL = "https://developer.wordpress.org"
TIMEOUT = 10

# Define major handbook and documentation sections with their start URLs
SECTIONS = {
    "plugin-handbook": {
        "url": "https://developer.wordpress.org/plugins/",
        "title": "Plugin Development Handbook",
        "description": "Complete guide to WordPress plugin development"
    },
    "theme-handbook": {
        "url": "https://developer.wordpress.org/themes/",
        "title": "Theme Development Handbook",
        "description": "Complete guide to WordPress theme development"
    },
    "block-editor": {
        "url": "https://developer.wordpress.org/block-editor/",
        "title": "Block Editor Handbook",
        "description": "Gutenberg / Block Editor development guide"
    },
    "rest-api": {
        "url": "https://developer.wordpress.org/rest-api/",
        "title": "REST API Handbook",
        "description": "WordPress REST API reference and guide"
    },
    "apis": {
        "url": "https://developer.wordpress.org/apis/",
        "title": "Common APIs",
        "description": "Core WordPress APIs and hooks"
    },
    "cli": {
        "url": "https://developer.wordpress.org/cli/",
        "title": "WP-CLI Documentation",
        "description": "WordPress Command Line Interface"
    },
    "plugins": {
        "url": "https://developer.wordpress.org/plugins/",
        "title": "Plugins Reference",
        "description": "Plugin development reference"
    }
}

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (compatible; DocumentationBot/1.0)'
})

visited_urls = set()
pages_by_section = defaultdict(list)


def is_developer_url(url: str) -> bool:
    """Check if URL is within developer.wordpress.org domain."""
    try:
        parsed = urlparse(url)
        return parsed.netloc in ['developer.wordpress.org', 'www.developer.wordpress.org']
    except:
        return False


def extract_main_content(html: str, url: str) -> tuple[str, str]:
    """Extract main content and title from page HTML."""
    soup = BeautifulSoup(html, 'html.parser')

    # Try to find the main title
    title = ""
    title_elem = soup.find('h1')
    if title_elem:
        title = title_elem.get_text(strip=True)

    if not title:
        title_elem = soup.find('title')
        if title_elem:
            title = title_elem.get_text(strip=True)
            # Clean up title
            title = re.sub(r'\s*[-|]\s*.*$', '', title).strip()

    # Extract main content - try multiple selectors
    content = None
    for selector in ['main', 'article', '.wp-content', '.content', '.post-content']:
        elem = soup.select_one(selector)
        if elem:
            content = elem
            break

    if not content:
        content = soup.body if soup.body else soup

    # Remove navigation, sidebar, footer
    for elem in content.find_all(['nav', 'aside', '.sidebar', '.navigation']):
        elem.decompose()

    # Get text content
    text = content.get_text(separator='\n', strip=True)

    # Clean up excessive whitespace
    text = re.sub(r'\n\n\n+', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)

    return title, text


def convert_to_markdown(html: str, url: str, title: str = None) -> str:
    """Convert HTML page to Markdown format."""
    soup = BeautifulSoup(html, 'html.parser')

    # Start with title
    if not title:
        title_elem = soup.find('h1')
        title = title_elem.get_text(strip=True) if title_elem else "Document"

    markdown = f"# {title}\n\n"
    markdown += f"**Source:** [{url}]({url})\n\n"

    # Extract main content
    content = None
    for selector in ['main', 'article', '.wp-content', '.content']:
        elem = soup.select_one(selector)
        if elem:
            content = elem
            break

    if not content:
        content = soup.body if soup.body else soup

    # Remove noise elements
    for elem in content.find_all(['nav', 'aside', 'script', 'style', '.sidebar', '.navigation']):
        elem.decompose()

    # Convert key HTML elements to markdown
    markdown += _convert_html_to_markdown(content)

    return markdown


def _convert_html_to_markdown(element) -> str:
    """Recursively convert HTML element to markdown."""
    if isinstance(element, str):
        return element

    markdown = ""

    if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(element.name[1])
        text = element.get_text(strip=True)
        markdown += "#" * level + " " + text + "\n\n"

    elif element.name == 'p':
        text = element.get_text(strip=True)
        if text:
            markdown += text + "\n\n"

    elif element.name in ['ul', 'ol']:
        items = element.find_all('li', recursive=False)
        for li in items:
            text = li.get_text(strip=True)
            marker = "- " if element.name == 'ul' else "1. "
            markdown += marker + text + "\n"
        markdown += "\n"

    elif element.name == 'blockquote':
        text = element.get_text(strip=True)
        markdown += "> " + text + "\n\n"

    elif element.name == 'code':
        text = element.get_text()
        markdown += f"`{text}`"

    elif element.name == 'pre':
        code = element.get_text()
        markdown += f"```\n{code}\n```\n\n"

    elif element.name == 'a':
        text = element.get_text(strip=True)
        href = element.get('href', '#')
        if text:
            markdown += f"[{text}]({href})"

    elif element.name == 'strong' or element.name == 'b':
        text = element.get_text(strip=True)
        markdown += f"**{text}**"

    elif element.name == 'em' or element.name == 'i':
        text = element.get_text(strip=True)
        markdown += f"*{text}*"

    elif element.name in ['br']:
        markdown += "\n"

    elif hasattr(element, 'children'):
        # Recursively process children
        for child in element.children:
            markdown += _convert_html_to_markdown(child)

    return markdown


def fetch_page(url: str) -> str:
    """Fetch a page and return its HTML content."""
    if url in visited_urls:
        return None

    visited_urls.add(url)

    try:
        response = session.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None


def extract_links_from_page(html: str, base_url: str) -> list[str]:
    """Extract all developer.wordpress.org links from a page."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []

    for link in soup.find_all('a', href=True):
        href = link['href']

        # Make absolute URL
        absolute_url = urljoin(base_url, href)

        # Remove fragments
        absolute_url = absolute_url.split('#')[0]

        # Only include developer.wordpress.org URLs
        if is_developer_url(absolute_url) and absolute_url not in visited_urls:
            links.append(absolute_url)

    return links


def scrape_section(section_key: str, section_info: dict, max_pages: int = 50) -> int:
    """Scrape a documentation section using breadth-first crawl."""
    print(f"\nScraping {section_info['title']}...", file=sys.stderr)

    to_visit = [section_info['url']]
    pages_fetched = 0

    while to_visit and pages_fetched < max_pages:
        url = to_visit.pop(0)

        if url in visited_urls:
            continue

        print(f"  Fetching: {url}", file=sys.stderr)

        html = fetch_page(url)
        if not html:
            continue

        # Extract and save content
        title, text = extract_main_content(html, url)

        if text and len(text) > 100:  # Only save meaningful content
            markdown = convert_to_markdown(html, url, title)

            # Create filename from URL
            path = urlparse(url).path.strip('/')
            filename = path.replace('/', '-') or 'index'
            filename = re.sub(r'-+', '-', filename)  # Remove duplicate dashes
            filepath = OUTPUT_DIR / f"{filename}.md"

            filepath.write_text(markdown, encoding='utf-8')
            pages_by_section[section_key].append({
                'url': url,
                'title': title,
                'filepath': filepath.name
            })
            pages_fetched += 1
            print(f"    ✓ Saved: {filepath.name}", file=sys.stderr)

        # Extract and queue new links
        new_links = extract_links_from_page(html, url)
        for link in new_links:
            if link not in to_visit:
                to_visit.append(link)

        # Respectful rate limiting
        time.sleep(0.5)

    print(f"  Fetched {pages_fetched} pages from {section_info['title']}", file=sys.stderr)
    return pages_fetched


def create_index_file():
    """Create an index file listing all scraped content."""
    index = "# WordPress Developer Documentation\n\n"
    index += "**Source:** https://developer.wordpress.org/\n\n"
    index += "This documentation covers core WordPress development APIs, plugin and theme development, REST API, Block Editor (Gutenberg), WP-CLI, and coding standards.\n\n"

    for section_key in SECTIONS.keys():
        pages = pages_by_section.get(section_key, [])
        if not pages:
            continue

        section = SECTIONS[section_key]
        index += f"## {section['title']}\n\n"
        index += f"{section['description']}\n\n"

        for page in sorted(pages, key=lambda p: p['title']):
            index += f"- [{page['title']}]({page['filepath']}) - [{page['url']}]({page['url']})\n"

        index += "\n"

    index_path = OUTPUT_DIR / "INDEX.md"
    index_path.write_text(index, encoding='utf-8')
    print(f"\nCreated index: {index_path}", file=sys.stderr)


def main():
    """Main scraper entry point."""
    print(f"WordPress Developer Documentation Scraper", file=sys.stderr)
    print(f"Output directory: {OUTPUT_DIR}", file=sys.stderr)
    print(f"Base URL: {BASE_URL}\n", file=sys.stderr)

    total_pages = 0

    # Scrape each major section
    for section_key, section_info in SECTIONS.items():
        try:
            pages = scrape_section(section_key, section_info, max_pages=40)
            total_pages += pages
        except Exception as e:
            print(f"Error scraping {section_key}: {e}", file=sys.stderr)
            continue

    # Create index
    create_index_file()

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"Extraction complete: {total_pages} pages saved to {OUTPUT_DIR}", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)


if __name__ == '__main__':
    main()
