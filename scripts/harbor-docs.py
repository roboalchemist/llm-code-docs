#!/usr/bin/env python3
"""
Harbor documentation scraper
Extracts comprehensive Harbor documentation from https://goharbor.io/docs/

Output: docs/web-scraped/harbor/
"""

import os
import re
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from typing import Set, Optional

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Configuration
BASE_URL = "https://goharbor.io"
DOCS_BASE = f"{BASE_URL}/docs/latest"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "harbor"

# Session with timeout and headers
SESSION = requests.Session()
SESSION.headers.update({
    'User-Agent': 'Mozilla/5.0 (compatible; LLM-Documentation-Bot/1.0)'
})
REQUEST_TIMEOUT = 10

# Track visited URLs to avoid duplicates
visited_urls: Set[str] = set()
failed_urls: Set[str] = set()

def normalize_url(url: str) -> str:
    """Normalize URL for comparison and tracking."""
    # Remove fragment and query params
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

def is_valid_harbor_url(url: str) -> bool:
    """Check if URL is within Harbor documentation scope."""
    if not url:
        return False

    url = url.strip()

    # Handle relative URLs
    if url.startswith('/'):
        return True

    if url.startswith('http'):
        parsed = urlparse(url)
        # Accept goharbor.io and github.com/goharbor URLs
        return 'goharbor.io' in parsed.netloc or 'github.com/goharbor' in parsed.netloc

    return False

def resolve_url(base: str, url: str) -> Optional[str]:
    """Resolve relative URLs to absolute URLs."""
    if not url or not is_valid_harbor_url(url):
        return None

    if url.startswith('http'):
        return url

    if url.startswith('/'):
        return urljoin(BASE_URL, url)

    return urljoin(base, url)

def extract_markdown_from_page(url: str, content: str) -> Optional[tuple[str, str]]:
    """Extract title and markdown content from HTML page."""
    try:
        soup = BeautifulSoup(content, 'html.parser')

        # Remove script and style tags
        for tag in soup(['script', 'style', 'nav', 'footer']):
            tag.decompose()

        # Try to find title
        title = None
        if soup.find('h1'):
            title = soup.find('h1').get_text(strip=True)
        elif soup.find('title'):
            title = soup.find('title').get_text(strip=True)
            # Clean up title
            if ' - ' in title:
                title = title.split(' - ')[0].strip()

        if not title:
            title = urlparse(url).path.split('/')[-1] or 'Harbor Documentation'

        # Find main content - usually in main, article, or .content class
        main_content = soup.find('main') or soup.find('article') or soup.find(class_='content')
        if not main_content:
            # Fallback to body
            main_content = soup.find('body')

        if not main_content:
            return None

        # Convert to markdown
        markdown = md(str(main_content), heading_style="atx")

        # Clean up markdown
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)  # Remove excessive newlines
        markdown = markdown.strip()

        if not markdown or len(markdown) < 100:
            return None

        return title, markdown

    except Exception as e:
        print(f"Error extracting markdown from {url}: {e}")
        return None

def fetch_and_save_page(url: str, depth: int = 0, max_depth: int = 3) -> list:
    """
    Fetch a page and save it, then recursively fetch linked pages.
    Returns list of new URLs found.
    """
    if depth > max_depth:
        return []

    # Normalize and check if already visited
    norm_url = normalize_url(url)
    if norm_url in visited_urls:
        return []

    visited_urls.add(norm_url)

    # Don't fetch non-HTML URLs
    if any(url.lower().endswith(ext) for ext in ['.pdf', '.png', '.jpg', '.gif', '.zip']):
        return []

    print(f"{'  ' * depth}Fetching: {url}")

    try:
        response = SESSION.get(url, timeout=REQUEST_TIMEOUT, allow_redirects=True)
        response.raise_for_status()

        # Check if content is HTML
        if 'text/html' not in response.headers.get('content-type', ''):
            return []

        # Extract markdown
        result = extract_markdown_from_page(url, response.text)
        if not result:
            failed_urls.add(url)
            return []

        title, markdown = result

        # Save to file
        rel_path = urlparse(url).path.strip('/').replace('/', '_')
        if not rel_path:
            rel_path = 'index'
        filename = f"{rel_path}.md"

        file_path = OUTPUT_DIR / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Add source URL as comment at top
        content = f"# {title}\n\n"
        content += f"**Source:** {url}\n\n"
        content += markdown

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"{'  ' * depth}✓ Saved: {filename}")

        # Extract links from HTML for recursive fetching
        new_urls = []
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link.get('href', '')
            resolved = resolve_url(url, href)

            if resolved and normalize_url(resolved) not in visited_urls:
                # Only follow docs links at depth 0, be selective deeper
                if depth == 0 or '/docs/' in resolved:
                    new_urls.append(resolved)

        return new_urls

    except requests.RequestException as e:
        print(f"{'  ' * depth}✗ Error fetching {url}: {e}")
        failed_urls.add(url)
        return []

    except Exception as e:
        print(f"{'  ' * depth}✗ Unexpected error: {e}")
        failed_urls.add(url)
        return []

    finally:
        time.sleep(0.5)  # Be respectful to the server

def scrape_harbor_docs():
    """Main scraper function."""
    print("Harbor Documentation Scraper")
    print(f"Starting from: {DOCS_BASE}")
    print(f"Output directory: {OUTPUT_DIR}\n")

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Start with the main docs page and install-config
    urls_to_visit = [
        DOCS_BASE,
        f"{DOCS_BASE}/install-config",
        f"{DOCS_BASE}/administration",
        f"{DOCS_BASE}/working-with-projects",
        f"{DOCS_BASE}/working-with-images",
        f"{DOCS_BASE}/manage-users",
        f"{DOCS_BASE}/harbor-api",
    ]

    processed = 0
    while urls_to_visit and processed < 100:
        url = urls_to_visit.pop(0)
        new_urls = fetch_and_save_page(url, depth=0, max_depth=2)
        urls_to_visit.extend(new_urls)
        processed += 1

    # Create README
    readme_content = """# Harbor Documentation

Harbor is an open-source cloud native registry that stores, signs, and scans content.

## Overview

This documentation contains comprehensive information about Harbor, including:

- Installation and configuration
- Project management and administration
- Image management and replication
- User and role management
- API documentation
- Vulnerability scanning and compliance
- Robot accounts and webhooks
- High availability and disaster recovery

## Key Features

- **Registry Management**: Store and manage container images
- **Replication**: Replicate images across multiple registries
- **Vulnerability Scanning**: Scan images for security vulnerabilities
- **RBAC**: Role-based access control for fine-grained permissions
- **Robot Accounts**: Create service accounts for automation
- **Webhooks**: Integrate with external systems via event notifications
- **Artifact Management**: Support for OCI artifacts beyond container images
- **P2P Distribution**: Leverage P2P technology for efficient distribution

## Quick Links

- Official Website: https://goharbor.io
- GitHub Repository: https://github.com/goharbor/harbor
- Project: Harbor is a CNCF graduated project

## Documentation Structure

The documentation is organized by major topics:

- **Installation & Configuration** - Setup, deployment, and configuration options
- **Administration** - User management, security settings, system configuration
- **Projects & Users** - Creating and managing projects, user roles
- **Images & Artifacts** - Working with container images and OCI artifacts
- **Advanced Topics** - Replication, scanning, webhooks, API usage

For more information, visit: https://goharbor.io/docs/
"""

    with open(OUTPUT_DIR / "README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"\n\nScraping complete!")
    print(f"Total visited: {len(visited_urls)}")
    print(f"Failed URLs: {len(failed_urls)}")
    print(f"Output directory: {OUTPUT_DIR}")

    # List generated files
    files = list(OUTPUT_DIR.glob("*.md"))
    print(f"Generated {len(files)} documentation files:")
    for f in sorted(files)[:10]:
        print(f"  - {f.name}")
    if len(files) > 10:
        print(f"  ... and {len(files) - 10} more")

if __name__ == "__main__":
    scrape_harbor_docs()
