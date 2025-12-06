#!/usr/bin/env python3
"""
Nomic AI Documentation Downloader
Downloads all Nomic platform and API documentation.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urljoin, urlparse
import time
import re
from bs4 import BeautifulSoup

BASE_URL = "https://docs.nomic.ai"

# Known documentation pages from navigation
PLATFORM_PAGES = [
    "/",
    "/platform/quick-start",
    "/platform/datasets/",
    "/platform/datasets/prepare-data-for-atlas",
    "/platform/datasets/storage",
    "/platform/datasets/data-maps/",
    "/platform/datasets/data-maps/controls",
    "/platform/datasets/data-maps/guides/data-curation",
    "/platform/datasets/guides/",
    "/platform/datasets/integrations/",
    "/platform/embeddings-and-retrieval/",
    "/platform/embeddings-and-retrieval/guides/improve-ai-model-performance-with-embedding-visualization-and-evaluation",
    "/platform/files/",
    "/platform/files/parse/overview/",
    "/platform/files/extraction/overview/",
    "/platform/account/dashboard",
    "/platform/release-notes",
]

API_REFERENCE_PAGES = [
    "/reference/getting-started/",
    "/reference/getting-started/rate-limits",
    "/reference/getting-started/programmatic-map-selections",
    "/reference/getting-started/programmatic-tagging",
    "/reference/python-api/datasets-and-maps",
    "/reference/typescript-api/overview",
    "/reference/api/embed-text-v-1-embedding-text-post",
    "/reference/api/query/data-selections",
    "/reference/api/upload-v-1-upload-post",
    "/reference/api/parse-v-1-parse-post",
    "/reference/api/extract-v-1-extract-post",
    "/reference/api/get-job-status-v-1-task-task-id-get",
    "/reference/api/create-api-key-v-1-user-authorization-keys-organization-id-create-post",
]

def extract_additional_links(html_content, base_url):
    """Extract additional documentation links from HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = set()

    # Find all links in navigation, sidebar, or content area
    for link in soup.find_all('a', href=True):
        href = link['href']

        # Skip external links, anchors, and non-doc links
        if href.startswith('#') or href.startswith('http') and not href.startswith(base_url):
            continue

        # Convert to absolute URL
        absolute_url = urljoin(base_url, href)
        parsed = urlparse(absolute_url)

        # Only include docs.nomic.ai links
        if parsed.netloc == 'docs.nomic.ai':
            # Get path without query params or fragments
            path = parsed.path
            if path and path != '/':
                links.add(path)

    return links

def download_page(url, output_path):
    """Download a page and convert to markdown."""
    try:
        print(f"Downloading: {url}")

        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; DocumentationBot/1.0)'
        }
        response = requests.get(url, timeout=15, headers=headers)
        response.raise_for_status()

        # Create directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Extract main content from HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try to find the main content area
        main_content = None
        for selector in ['main', 'article', '[role="main"]', '.content', '#content']:
            main_content = soup.select_one(selector)
            if main_content:
                break

        if not main_content:
            main_content = soup.body if soup.body else soup

        # Remove script, style, nav elements
        for element in main_content.find_all(['script', 'style', 'nav', 'header', 'footer']):
            element.decompose()

        # Convert to markdown-friendly format
        # Extract title
        title = soup.find('h1')
        title_text = title.get_text().strip() if title else "Nomic Documentation"

        # Build markdown content
        markdown = f"# {title_text}\n\n"
        markdown += f"Source: {url}\n\n"

        # Get text content with basic structure preservation
        for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'code', 'ul', 'ol', 'li', 'blockquote', 'table']):
            tag = element.name
            text = element.get_text().strip()

            if not text:
                continue

            if tag == 'h1':
                markdown += f"# {text}\n\n"
            elif tag == 'h2':
                markdown += f"## {text}\n\n"
            elif tag == 'h3':
                markdown += f"### {text}\n\n"
            elif tag == 'h4':
                markdown += f"#### {text}\n\n"
            elif tag == 'h5':
                markdown += f"##### {text}\n\n"
            elif tag == 'h6':
                markdown += f"###### {text}\n\n"
            elif tag in ['pre', 'code']:
                # Check if it's already inside a pre tag
                if element.parent and element.parent.name != 'pre':
                    markdown += f"```\n{text}\n```\n\n"
            elif tag == 'p':
                markdown += f"{text}\n\n"
            elif tag == 'blockquote':
                lines = text.split('\n')
                markdown += '\n'.join(f"> {line}" for line in lines) + "\n\n"
            elif tag == 'li':
                # Simple list item handling
                markdown += f"- {text}\n"

        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  → Saved to: {output_path} ({len(markdown)} bytes)")
        return True, response.text

    except requests.exceptions.RequestException as e:
        print(f"  → Error downloading {url}: {e}")
        return False, None
    except Exception as e:
        print(f"  → Error processing {url}: {e}")
        return False, None

def url_to_filename(url_path):
    """Convert URL path to filesystem path."""
    # Remove leading/trailing slashes
    path = url_path.strip('/')

    # Handle root
    if not path:
        return "index.md"

    # Replace slashes with directory separators
    parts = path.split('/')

    # If the last part looks like a page (no extension), add .md
    if parts[-1] and '.' not in parts[-1]:
        parts[-1] = parts[-1] + '.md'
    elif not parts[-1]:
        # Ends with slash - use index.md
        parts[-1] = 'index.md'

    return Path(*parts)

def discover_links_recursively(start_pages, max_depth=2):
    """Discover additional documentation links by crawling."""
    discovered = set(start_pages)
    to_visit = [(page, 0) for page in start_pages]
    visited = set()

    print(f"🔍 Discovering documentation pages (max depth: {max_depth})...")

    while to_visit:
        page, depth = to_visit.pop(0)

        if page in visited or depth > max_depth:
            continue

        visited.add(page)
        url = urljoin(BASE_URL, page)

        try:
            print(f"  Scanning: {page} (depth {depth})")
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; DocumentationBot/1.0)'
            }
            response = requests.get(url, timeout=15, headers=headers)
            response.raise_for_status()

            new_links = extract_additional_links(response.text, BASE_URL)

            for link in new_links:
                if link not in discovered:
                    discovered.add(link)
                    if depth < max_depth:
                        to_visit.append((link, depth + 1))

            time.sleep(0.5)  # Be respectful

        except Exception as e:
            print(f"  ⚠️  Error scanning {page}: {e}")

    print(f"✅ Discovered {len(discovered)} total pages")
    return list(discovered)

def main():
    """Main function to download all Nomic documentation."""

    print("📚 Nomic AI Documentation Downloader")
    print("=" * 60)
    print()

    # Output directory
    output_dir = Path("docs/web-scraped/nomic")

    # Combine all known pages
    all_pages = PLATFORM_PAGES + API_REFERENCE_PAGES

    # Discover additional pages
    print("Starting with {} known pages".format(len(all_pages)))
    all_pages = discover_links_recursively(all_pages, max_depth=2)

    # Remove duplicates and sort
    all_pages = sorted(set(all_pages))

    print()
    print(f"🎯 Found {len(all_pages)} documentation pages to download")
    print(f"📂 Output directory: {output_dir}")
    print()

    # Download each page
    successful = 0
    failed = 0

    start_time = time.time()

    for i, page_path in enumerate(all_pages, 1):
        url = urljoin(BASE_URL, page_path)
        output_path = output_dir / url_to_filename(page_path)

        print(f"[{i:3d}/{len(all_pages)}] ", end="", flush=True)

        # Add delay between requests
        if i > 1:
            time.sleep(0.5)

        success, html_content = download_page(url, output_path)

        if success:
            successful += 1
        else:
            failed += 1

    # Final summary
    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print(f"📊 Download Summary")
    print("=" * 60)
    print(f"✅ Successful downloads:  {successful}")
    print(f"❌ Failed downloads:      {failed}")
    print(f"⏱️  Total time:            {elapsed:.1f} seconds")
    print(f"📁 Output directory:      {output_dir}")

    # Calculate total size
    if output_dir.exists():
        total_size = sum(f.stat().st_size for f in output_dir.rglob("*.md"))
        print(f"💾 Total documentation:   {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()

    if failed > 0:
        print(f"⚠️  {failed} downloads failed")
        sys.exit(1)
    else:
        print("🎉 All documentation downloaded successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
