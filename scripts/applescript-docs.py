#!/usr/bin/env python3
"""
Comprehensive scraper for AppleScript official documentation from Apple Developer.
Scrapes the AppleScript Language Guide and Mac Automation Scripting Guide from archived Apple docs.

Output: docs/web-scraped/applescript/

Sources:
- https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/
- https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/
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

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "applescript"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Session for connection pooling
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
})

visited_urls: Set[str] = set()
documents: Dict[str, str] = {}
page_count = 0

def normalize_url(url: str) -> str:
    """Normalize URL for comparison."""
    parsed = urlparse(url)
    path = parsed.path.rstrip('/').rstrip('.html')
    return f"{parsed.scheme}://{parsed.netloc}{path}"

def is_valid_doc_url(url: str, base_urls: List[str]) -> bool:
    """Check if URL is a valid documentation page."""
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ('http', 'https'):
            return False

        # Must match one of the base URLs
        url_matches = any(base in parsed.netloc + parsed.path for base in base_urls)
        if not url_matches:
            return False

        # Exclude PDFs and external links
        if url.endswith(('.pdf', '.zip', '.dmg')):
            return False

        # Skip certain patterns
        skip_patterns = ['release', 'whatsnew', 'rss', 'feedback', 'sitemap', 'search', 'browse']
        if any(x in url.lower() for x in skip_patterns):
            return False

        return True
    except:
        return False

def html_to_markdown(html_content: str) -> str:
    """Convert HTML to markdown-formatted text."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script, style, and navigation elements
    for element in soup(["script", "style", "nav", ".sidenav", ".toc", "footer", ".breadcrumb"]):
        element.decompose()

    markdown_lines = []

    # Try to find main content area
    main_content = None
    for selector in ['#main-content', '.content', 'main', 'article', '.documentation']:
        main_content = soup.select_one(selector)
        if main_content:
            break

    if not main_content:
        main_content = soup.body if soup.body else soup

    # Process headings and paragraphs
    for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'pre', 'code', 'ul', 'ol', 'blockquote']):
        if element.name.startswith('h'):
            level = int(element.name[1])
            text = element.get_text(strip=True)
            if text:
                markdown_lines.append("\n" + "#" * level + " " + text + "\n")
        elif element.name == 'p':
            text = element.get_text(strip=True)
            if text and len(text) > 3:
                markdown_lines.append(text + "\n")
        elif element.name == 'li':
            text = element.get_text(strip=True)
            if text:
                markdown_lines.append("- " + text + "\n")
        elif element.name == 'pre':
            text = element.get_text(strip=False)
            if text:
                markdown_lines.append("```\n" + text + "```\n")
        elif element.name == 'blockquote':
            text = element.get_text(strip=True)
            if text:
                markdown_lines.append("> " + text + "\n")

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
            title = f"Page {page_count + 1}"

        # Extract content
        content = html_to_markdown(response.text)

        if not content or len(content.strip()) < 100:
            logger.info(f"  -> Content too short, skipping")
            return None

        page_count += 1
        logger.info(f"  -> OK ({len(content)} chars)")
        time.sleep(1)  # Be respectful to Apple's servers

        return title, content

    except requests.RequestException as e:
        logger.info(f"  -> Error: {e}")
        return None
    except Exception as e:
        logger.info(f"  -> Parse error: {e}")
        return None

def extract_page_links(url: str, base_urls: List[str]) -> Set[str]:
    """Extract all valid documentation links from a page."""
    links_found = set()

    try:
        response = session.get(url, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href and not href.startswith('#'):
                try:
                    full_url = urljoin(url, href)
                    if is_valid_doc_url(full_url, base_urls):
                        normalized = normalize_url(full_url)
                        if normalized not in visited_urls:
                            links_found.add(full_url)
                except:
                    pass

        time.sleep(0.5)

    except Exception as e:
        logger.warning(f"Error extracting links from {url}: {e}")

    return links_found

def scrape_guide(base_url: str, guide_name: str, base_urls: List[str], max_pages: int = 150) -> int:
    """Scrape a documentation guide and all its linked pages."""
    logger.info(f"\n{'='*70}")
    logger.info(f"Scraping: {guide_name}")
    logger.info(f"Base URL: {base_url}")
    logger.info(f"{'='*70}")

    pages_collected = 0
    urls_to_process = [base_url]
    processed = set()

    while urls_to_process and pages_collected < max_pages:
        current_url = urls_to_process.pop(0)

        if normalize_url(current_url) in processed:
            continue

        processed.add(normalize_url(current_url))

        # Fetch and parse
        result = fetch_and_parse(current_url)
        if result:
            title, content = result
            documents[title] = content
            pages_collected += 1

            # Extract links for next batch
            new_links = extract_page_links(current_url, base_urls)
            for link in new_links:
                if normalize_url(link) not in processed and len(urls_to_process) < 50:
                    urls_to_process.append(link)

    logger.info(f"Collected {pages_collected} pages from {guide_name}")
    return pages_collected

def save_documents():
    """Save all collected documents to files."""
    logger.info(f"\n{'='*70}")
    logger.info(f"Saving {len(documents)} documents")
    logger.info(f"{'='*70}")

    if not documents:
        logger.error("No documents collected!")
        return

    # Save individual files
    for i, (title, content) in enumerate(documents.items(), 1):
        # Create safe filename from title
        safe_title = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
        safe_title = safe_title[:75]
        filepath = OUTPUT_DIR / f"{i:03d}-{safe_title}.md"

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(content)
            logger.info(f"  [{i:3d}] {filepath.name}")
        except Exception as e:
            logger.error(f"  Error saving {filepath}: {e}")

    # Save comprehensive index
    index_file = OUTPUT_DIR / "INDEX.md"
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write("# AppleScript Official Documentation\n\n")
        f.write("Comprehensive AppleScript language reference from Apple Developer.\n\n")
        f.write("## Documentation Sources\n\n")
        f.write("- [AppleScript Language Guide](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/)\n")
        f.write("- [Mac Automation Scripting Guide](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/)\n\n")
        f.write("## Table of Contents\n\n")
        for i, title in enumerate(documents.keys(), 1):
            safe_title = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:75]
            safe_title = safe_title[:75]
            f.write(f"{i}. [{title}](/docs/web-scraped/applescript/{i:03d}-{safe_title}.md)\n")

    logger.info(f"Index saved: {index_file}")

def main():
    """Main scraper entry point."""
    logger.info("AppleScript Official Documentation Scraper")
    logger.info("==========================================\n")

    # Define base URLs for filtering
    applescript_base_urls = [
        'developer.apple.com/library/archive/documentation/AppleScript',
        'developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide'
    ]

    # AppleScript Language Guide
    lang_guide_url = "https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/"
    collected_lang = scrape_guide(
        lang_guide_url,
        "AppleScript Language Guide",
        applescript_base_urls,
        max_pages=100
    )

    # Mac Automation Scripting Guide
    automation_guide_url = "https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/"
    collected_automation = scrape_guide(
        automation_guide_url,
        "Mac Automation Scripting Guide",
        applescript_base_urls,
        max_pages=100
    )

    # Save all documents
    save_documents()

    logger.info(f"\n{'='*70}")
    logger.info(f"Scraping complete!")
    logger.info(f"Total documents collected: {len(documents)}")
    logger.info(f"  - AppleScript Language Guide: {collected_lang}")
    logger.info(f"  - Mac Automation Scripting Guide: {collected_automation}")
    logger.info(f"Output directory: {OUTPUT_DIR}")
    logger.info(f"{'='*70}")

if __name__ == "__main__":
    main()
