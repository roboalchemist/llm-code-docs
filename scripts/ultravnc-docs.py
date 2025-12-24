#!/usr/bin/env python3
"""
UltraVNC Documentation Scraper
Downloads all UltraVNC documentation pages and converts to markdown.
UltraVNC is an open source remote PC access software.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse, urljoin
import time
import re
import subprocess
from bs4 import BeautifulSoup

# UltraVNC documentation base URL
BASE_URL = "https://uvnc.com"
DOCS_URL = "https://uvnc.com/docs/"

# Known documentation pages (will be expanded by crawling)
ULTRAVNC_DOC_PAGES = [
    "/docs/documentation.html",
    "/docs/general-knowledge.html",
    "/docs/ultravnc-server.html",
    "/docs/ultravnc-server/48-ultravnc-installation.html",
    "/docs/ultravnc-server/49-ultravnc-server-configuration.html",
    "/docs/ultravnc-viewer.html",
    "/docs/ultravnc-viewer/52-ultravnc-viewer-commandline-parameters.html",
    "/docs/ultravnc-repeater.html",
    "/docs/documentation/132-ultravnc-connections.html",
    "/docs/documentation/134-ultravnc-virtual-displays.html",
    "/docs/ultravnc-sc.html",
    "/docs/pchelpware.html",
]


def discover_doc_pages(start_url, max_pages=100):
    """Crawl the documentation to discover all pages."""
    discovered = set()
    to_visit = {start_url}
    visited = set()

    print("Discovering documentation pages...")

    while to_visit and len(discovered) < max_pages:
        url = to_visit.pop()
        if url in visited:
            continue

        visited.add(url)

        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()

            # Parse HTML to find links
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all links in the documentation
            for link in soup.find_all('a', href=True):
                href = link['href']

                # Convert to absolute URL
                absolute_url = urljoin(url, href)
                parsed = urlparse(absolute_url)

                # Only include uvnc.com/docs/ URLs
                if parsed.netloc == 'uvnc.com' and parsed.path.startswith('/docs/'):
                    # Remove fragments and queries
                    clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

                    # Skip non-HTML files
                    if not any(clean_url.endswith(ext) for ext in ['.pdf', '.zip', '.exe', '.jpg', '.png', '.gif']):
                        discovered.add(parsed.path)
                        if clean_url not in visited:
                            to_visit.add(clean_url)

            time.sleep(0.3)  # Be respectful

        except Exception as e:
            print(f"  Error crawling {url}: {e}")
            continue

    print(f"Discovered {len(discovered)} documentation pages")
    return sorted(discovered)


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script, style, nav, header, footer elements
    for element in soup.find_all(['script', 'style', 'nav', 'header', 'footer', 'iframe']):
        element.decompose()

    # Try to find main content area
    # UltraVNC uses various content divs
    main_content = None
    for selector in [
        {'class': 'item-page'},
        {'class': 'article-content'},
        {'id': 'content'},
        {'class': 'content'},
        {'role': 'main'},
    ]:
        main_content = soup.find('div', selector)
        if main_content:
            break

    if main_content:
        html_content = str(main_content)
    else:
        # Fallback: use body content
        body = soup.find('body')
        if body:
            html_content = str(body)
        else:
            html_content = str(soup)

    # Try pandoc conversion
    try:
        result = subprocess.run(
            ['pandoc', '-f', 'html', '-t', 'markdown', '--wrap=none'],
            input=html_content,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            markdown = result.stdout
            # Clean up pandoc artifacts
            markdown = re.sub(r'^::+.*$', '', markdown, flags=re.MULTILINE)
            markdown = re.sub(r'\{[^}]*\}', '', markdown)
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)
            markdown = markdown.strip()
            return f"# Source: {url}\n\n{markdown}"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: basic HTML to text conversion
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove remaining unwanted elements
    for element in soup.find_all(['script', 'style', 'nav', 'aside', 'form']):
        element.decompose()

    # Convert to text
    text = soup.get_text(separator='\n')

    # Clean up whitespace
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(line for line in lines if line)
    text = re.sub(r'\n{3,}', '\n\n', text)

    return f"# Source: {url}\n\n{text}"


def download_page(url, output_path):
    """Download a page and convert to markdown."""
    try:
        print(f"Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Convert HTML to markdown
        markdown = html_to_markdown(response.text, url)

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def path_to_filename(path):
    """Convert URL path to filename."""
    if path == "/" or path == "" or path == "/docs/" or path == "/docs":
        return "index.md"

    # Remove leading /docs/ and trailing slashes
    clean_path = path.replace('/docs/', '').strip('/')

    # Replace slashes with hyphens and ensure .md extension
    if clean_path.endswith('.html'):
        clean_path = clean_path[:-5]

    filename = clean_path.replace('/', '-')

    if not filename:
        return "index.md"

    if not filename.endswith('.md'):
        filename += '.md'

    return filename


def main():
    """Main function to download all UltraVNC documentation."""
    print("=" * 60)
    print("UltraVNC Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print()

    # Discover all documentation pages
    doc_pages = discover_doc_pages(DOCS_URL, max_pages=150)

    # Combine with known pages
    all_pages = sorted(set(ULTRAVNC_DOC_PAGES + doc_pages))

    print(f"Total pages to download: {len(all_pages)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "ultravnc"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(all_pages, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(all_pages)}] ", end="")

        if download_page(url, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.5)

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} pages failed to download")
        sys.exit(1)
    else:
        print("All pages downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
