#!/usr/bin/env python3
"""
Comprehensive scraper for Zenoh documentation from zenoh.io.
Zenoh is a pub/sub/query protocol for IoT, robotics, and distributed systems.

Output: docs/web-scraped/zenoh/

Sources:
- https://zenoh.io/docs/
- https://zenoh.io/docs/overview/
- https://zenoh.io/docs/getting-started/
- https://zenoh.io/docs/manual/
- https://zenoh.io/docs/apis/
- https://zenoh.io/docs/migration_1.0/
"""

import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import re
from typing import Set, Dict, List, Optional
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "zenoh"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Session for connection pooling
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

visited_urls: Set[str] = set()
documents: Dict[str, str] = {}
page_count = 0

# Base URL for zenoh documentation
BASE_URLS = [
    "https://zenoh.io/docs/",
]

def normalize_url(url: str) -> str:
    """Normalize URL for comparison."""
    parsed = urlparse(url)
    path = parsed.path.rstrip('/').rstrip('.html')
    return f"{parsed.scheme}://{parsed.netloc}{path}"

def is_valid_doc_url(url: str) -> bool:
    """Check if URL is a valid documentation page."""
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ('http', 'https'):
            return False

        # Must be from zenoh.io/docs
        if not ('zenoh.io' in parsed.netloc and '/docs/' in parsed.path):
            return False

        # Exclude certain patterns
        skip_patterns = ['#', 'mailto:', 'javascript:', '.pdf', '.zip']
        if any(x in url for x in skip_patterns):
            return False

        return True
    except:
        return False

def html_to_markdown(html_content: str, url: str = "") -> str:
    """Convert HTML to markdown-formatted text."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script, style, nav, footer and other non-content elements
    for element in soup(["script", "style", "nav", "footer", ".navbar", ".toc-sidebar", ".breadcrumb"]):
        element.decompose()

    markdown_lines = []

    # Add source header
    if url:
        markdown_lines.append(f"# Source: {url}\n")

    # Try to find main content area
    main_content = None
    for selector in ['main', '.ato-body', '.main-content', 'article', '.content', '.container']:
        main_content = soup.select_one(selector)
        if main_content:
            break

    if not main_content:
        main_content = soup.body if soup.body else soup

    # Process content - include more element types
    for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'pre', 'code', 'ul', 'ol', 'blockquote', 'a', 'span', 'div', 'section', 'article']):
        if element.get('class') and any('toc' in str(c) for c in element.get('class', [])):
            continue

        # Skip if this element has been processed as part of parent
        if element.parent and element.parent.name in ['p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            continue

        if element.name.startswith('h'):
            level = int(element.name[1])
            text = element.get_text(strip=True)
            if text and len(text) > 0:
                markdown_lines.append("\n" + "#" * level + " " + text + "\n")
        elif element.name == 'p':
            text = element.get_text(strip=True)
            if text and len(text) > 2:
                markdown_lines.append(text + "\n")
        elif element.name == 'li':
            text = element.get_text(strip=True)
            if text:
                markdown_lines.append("- " + text + "\n")
        elif element.name == 'pre':
            text = element.get_text(strip=False)
            if text:
                # Check if it has a language class
                code_class = element.get('class', [])
                lang = ''
                for c in code_class:
                    if 'language-' in c:
                        lang = c.replace('language-', '')
                        break
                if lang:
                    markdown_lines.append(f"```{lang}\n{text}```\n\n")
                else:
                    markdown_lines.append(f"```\n{text}```\n\n")
        elif element.name == 'blockquote':
            text = element.get_text(strip=True)
            if text:
                markdown_lines.append("> " + text + "\n")
        elif element.name in ['div', 'section', 'article']:
            # Only process if it has substantial text content
            text = element.get_text(strip=True)
            if text and len(text) > 50 and element.find(['p', 'h1', 'h2', 'h3', 'li', 'pre']):
                # Has substantial content with structure
                pass  # Let children be processed

    content = "".join(markdown_lines)

    # Clean up excess whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.strip()

    return content

def fetch_and_parse(url: str) -> Optional[tuple[str, str]]:
    """Fetch a URL and extract its content. Returns (title, content) or None."""
    global page_count

    normalized = normalize_url(url)

    if normalized in visited_urls:
        return None

    visited_urls.add(normalized)

    try:
        logger.info(f"Fetching: {url}")
        response = session.get(url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title
        title = ""
        if soup.title:
            title = soup.title.get_text(strip=True)
        else:
            h1 = soup.find('h1')
            if h1:
                title = h1.get_text(strip=True)

        if not title:
            return None

        # Convert to markdown
        content = html_to_markdown(response.text, url)

        if not content or len(content) < 50:
            logger.warning(f"  Content too short ({len(content)} bytes), skipping")
            return None

        page_count += 1
        return (title, content)

    except requests.exceptions.Timeout:
        logger.error(f"  Timeout: {url}")
        return None
    except requests.exceptions.RequestException as e:
        logger.error(f"  Error: {e}")
        return None
    except Exception as e:
        logger.error(f"  Parse error: {e}")
        return None

def extract_links(html_content: str, base_url: str) -> List[str]:
    """Extract all valid documentation links from HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = set()

    for link in soup.find_all('a', href=True):
        url = urljoin(base_url, link['href'])

        # Remove fragments
        if '#' in url:
            url = url.split('#')[0]

        if is_valid_doc_url(url):
            links.add(normalize_url(url))

    return list(links)

def crawl_documentation(start_url: str, max_pages: int = 500):
    """Crawl the documentation starting from the given URL."""
    global page_count

    to_visit = [start_url]
    visited = set()

    logger.info(f"Starting crawl from: {start_url}")
    logger.info(f"Maximum pages: {max_pages}")
    logger.info("")

    while to_visit and page_count < max_pages:
        url = to_visit.pop(0)

        if url in visited:
            continue
        visited.add(url)

        result = fetch_and_parse(url)
        if result:
            title, content = result
            logger.info(f"  -> Saved: {title} ({len(content)} bytes)")

            # Save to file
            filename = f"page_{page_count:04d}_{urlparse(url).path.split('/')[-1] or 'index'}.md"
            if not filename.endswith('.md'):
                filename += '.md'

            file_path = OUTPUT_DIR / filename
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"Source: {url}\n\n")
                f.write(content)

            # Extract new links
            try:
                response = session.get(url, timeout=15)
                new_links = extract_links(response.text, url)
                for link in new_links:
                    if link not in visited and link not in to_visit:
                        to_visit.append(link)
            except:
                pass

        time.sleep(0.5)  # Be respectful

    return page_count

def create_index_file():
    """Create an index file listing all documentation pages."""
    index_path = OUTPUT_DIR / "INDEX.md"

    markdown_files = sorted(OUTPUT_DIR.glob("*.md"))

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# Zenoh Documentation Index\n\n")
        f.write("This is a complete scrape of the Zenoh documentation from https://zenoh.io/docs/\n\n")
        f.write("## Pages\n\n")

        for md_file in markdown_files:
            if md_file.name != "INDEX.md":
                f.write(f"- [{md_file.name}](./{md_file.name})\n")

def main():
    """Main function to download and process Zenoh documentation."""
    print("=" * 70)
    print("Zenoh Documentation Scraper")
    print("=" * 70)
    print()

    start_time = time.time()

    # Start crawling from the main docs page
    pages_crawled = crawl_documentation("https://zenoh.io/docs/", max_pages=200)

    # Create index
    create_index_file()

    elapsed = time.time() - start_time

    print()
    print("=" * 70)
    print("Scrape Summary")
    print("=" * 70)
    print(f"Pages crawled: {pages_crawled}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Calculate total size
    total_size = sum(f.stat().st_size for f in OUTPUT_DIR.glob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")

    # List sample files
    sample_files = sorted(OUTPUT_DIR.glob("*.md"))[:5]
    if sample_files:
        print(f"\nSample files:")
        for f in sample_files:
            print(f"  - {f.name}")

    print()
    if pages_crawled > 0:
        print("Documentation scraped successfully!")
        return 0
    else:
        print("Warning: No pages were successfully scraped")
        return 1

if __name__ == "__main__":
    exit(main())
