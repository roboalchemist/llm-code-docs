#!/usr/bin/env python3
"""
Helix Editor Documentation Scraper
Downloads user documentation from docs.helix-editor.com
Helix is a post-modern text editor with built-in language server support.
"""

import os
import sys
import requests
from pathlib import Path
import time
from urllib.parse import urljoin, urlparse
import re

# Base URL
BASE_URL = "https://docs.helix-editor.com"

# Main documentation pages to scrape
DOCS_PAGES = [
    "/",  # Index/home
    "/usage.html",
    "/keymap.html",
    "/configuration.html",
    "/install.html",
    "/lang-support.html",
    "/themes.html",
]

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "helix-editor"

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests


def sanitize_filename(path):
    """Convert URL path to safe filename."""
    # Remove .html extension
    safe = path.rstrip("/").replace(".html", "")
    # Remove leading slash
    safe = safe.lstrip("/")
    # If empty, use 'index'
    if not safe:
        safe = "index"
    # Replace slashes with dashes
    safe = safe.replace("/", "-")
    # Add .md extension
    safe = safe + ".md"
    return safe


def fetch_and_parse_page(url):
    """Fetch HTML page and extract content."""
    try:
        print(f"  Fetching: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Try to import BeautifulSoup for HTML parsing
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            print(f"    Warning: BeautifulSoup not available")
            # Return plain text extraction
            return extract_text_basic(response.text), url

        soup = BeautifulSoup(response.content, 'html.parser')

        # Remove script and style elements
        for script in soup(["script", "style", "nav", ".sidebar"]):
            script.decompose()

        # Find main content - look for common patterns
        content = None
        for selector in ['main', '[role="main"]', '.content', '.main-content', '#content', 'article']:
            element = soup.select_one(selector)
            if element:
                content = element
                break

        if content is None:
            # Fall back to body if no main content found
            content = soup.find('body')
            if content:
                # Remove nav elements
                for nav in content.find_all(['nav', 'header', 'footer']):
                    nav.decompose()

        if content is None:
            return extract_text_basic(response.text), url

        # Extract text and basic structure
        text = extract_structure_text(content)
        return text, url

    except requests.exceptions.RequestException as e:
        print(f"    Error fetching {url}: {e}")
        return None, url
    except Exception as e:
        print(f"    Error processing {url}: {e}")
        return None, url


def extract_text_basic(html_text):
    """Basic text extraction from HTML."""
    # Remove script and style elements
    html_text = re.sub(r'<script[^>]*>.*?</script>', '', html_text, flags=re.DOTALL | re.IGNORECASE)
    html_text = re.sub(r'<style[^>]*>.*?</style>', '', html_text, flags=re.DOTALL | re.IGNORECASE)

    # Convert HTML entities
    html_text = html_text.replace('&nbsp;', ' ')
    html_text = html_text.replace('&lt;', '<')
    html_text = html_text.replace('&gt;', '>')
    html_text = html_text.replace('&quot;', '"')
    html_text = html_text.replace('&amp;', '&')

    # Remove HTML tags
    html_text = re.sub(r'<[^>]+>', '\n', html_text)

    # Clean up whitespace
    lines = [line.strip() for line in html_text.split('\n')]
    lines = [line for line in lines if line]

    return '\n\n'.join(lines)


def extract_structure_text(element):
    """Extract text with basic structure from BeautifulSoup element."""
    result = []

    for child in element.children:
        if isinstance(child, str):
            text = child.strip()
            if text and text not in ['\n', '\r', '\t', ' ']:
                result.append(text)
        elif hasattr(child, 'name'):
            tag = child.name

            if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                # Extract heading level from tag name
                level = int(tag[1])
                heading_text = child.get_text(strip=True)
                if heading_text:
                    result.append('\n' + '#' * level + ' ' + heading_text + '\n')

            elif tag == 'p':
                text = child.get_text(strip=True)
                if text:
                    result.append(text)

            elif tag == 'li':
                text = child.get_text(strip=True)
                if text:
                    result.append('- ' + text)

            elif tag in ['ul', 'ol']:
                items = []
                for li in child.find_all('li', recursive=False):
                    li_text = li.get_text(strip=True)
                    if li_text:
                        items.append('- ' + li_text)
                if items:
                    result.extend(items)

            elif tag == 'code':
                text = child.get_text(strip=True)
                if text:
                    result.append('`' + text + '`')

            elif tag == 'pre':
                text = child.get_text(strip=True)
                if text:
                    result.append('\n```\n' + text + '\n```\n')

            elif tag == 'blockquote':
                text = child.get_text(strip=True)
                if text:
                    result.append('> ' + text)

            elif tag in ['div', 'section', 'article']:
                # Recursively process container elements
                sub_text = extract_structure_text(child)
                if sub_text:
                    result.append(sub_text)

            else:
                # For other tags, try to extract text
                text = child.get_text(strip=True)
                if text:
                    result.append(text)

    # Join results and clean up
    output = '\n'.join(result)

    # Remove excessive whitespace
    output = re.sub(r'\n\n\n+', '\n\n', output)
    output = re.sub(r' +', ' ', output)

    return output.strip()


def download_docs():
    """Download all documentation pages."""
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Downloading Helix Editor documentation from {BASE_URL}")
    print(f"Output directory: {OUTPUT_DIR}\n")

    downloaded = 0
    failed = 0

    for page_path in DOCS_PAGES:
        url = urljoin(BASE_URL, page_path)

        content, source_url = fetch_and_parse_page(url)

        if content is None:
            failed += 1
            continue

        # Create output filename
        filename = sanitize_filename(page_path)
        output_path = OUTPUT_DIR / filename

        # Add source header
        header = f"""# Source: {source_url}

"""
        full_content = header + content

        # Write file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"    -> Saved: {output_path.name}")
        downloaded += 1

        # Rate limiting
        time.sleep(REQUEST_DELAY)

    print(f"\nDownload complete!")
    print(f"  Downloaded: {downloaded} pages")
    if failed > 0:
        print(f"  Failed: {failed} pages")

    # Verify output
    files = list(OUTPUT_DIR.glob('*.md'))
    total_size = sum(f.stat().st_size for f in files)
    print(f"\nVerification:")
    print(f"  Total files: {len(files)}")
    print(f"  Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    return downloaded > 0


if __name__ == "__main__":
    success = download_docs()
    sys.exit(0 if success else 1)
