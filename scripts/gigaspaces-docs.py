#!/usr/bin/env python3
"""
Scraper for GigaSpaces documentation.
Downloads pages from their llms.txt index and converts to Markdown.
Output: docs/web-scraped/gigaspaces/
"""
import requests
from pathlib import Path
from urllib.parse import urlparse
import html2text
import time
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "gigaspaces"
LLMS_TXT_URL = "https://gigaspaces.com/llms.txt"

# Headers to avoid being blocked
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def ensure_output_dir():
    """Create output directory if it doesn't exist."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")

def extract_urls_from_llms_txt():
    """Extract URLs from GigaSpaces llms.txt."""
    try:
        response = requests.get(LLMS_TXT_URL, timeout=10, headers=HEADERS)
        response.raise_for_status()

        # Extract URLs from markdown links
        urls = re.findall(r'\(https?://[^\)]+\)', response.text)
        urls = [url[1:-1] for url in urls]  # Remove parentheses

        # Remove duplicates while preserving order
        seen = set()
        unique_urls = []
        for url in urls:
            if url not in seen:
                seen.add(url)
                unique_urls.append(url)

        print(f"Found {len(unique_urls)} unique URLs in llms.txt")
        return unique_urls
    except Exception as e:
        print(f"Error fetching llms.txt: {e}")
        return []

def sanitize_filename(url):
    """Convert URL to safe filename."""
    parsed = urlparse(url)
    # Remove domain and create path-based filename
    path = parsed.path.strip('/')
    if parsed.query:
        path += '_' + parsed.query.replace('=', '_').replace('&', '_')

    # Keep it readable - truncate if too long
    filename = path.replace('/', '_').replace('?', '_')
    # Remove any remaining special characters
    filename = re.sub(r'[^a-zA-Z0-9_-]', '', filename)

    if not filename:
        filename = 'index'

    # Truncate to reasonable length but keep it meaningful
    if len(filename) > 100:
        filename = filename[:100]

    return f"{filename}.md"

def download_and_convert(url):
    """Download a page and convert to Markdown."""
    try:
        response = requests.get(url, timeout=10, headers=HEADERS)
        response.raise_for_status()

        # Skip if not HTML
        if 'text/html' not in response.headers.get('content-type', ''):
            return None

        # Convert HTML to Markdown
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.body_width = 0
        markdown_content = h.handle(response.text)

        # Add source header
        markdown_with_source = f"# Source: {url}\n\n{markdown_content}"

        filename = sanitize_filename(url)
        filepath = OUTPUT_DIR / filename

        # Write to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_with_source)

        print(f"  Downloaded: {filename}")
        return filepath

    except Exception as e:
        print(f"  Error downloading {url}: {e}")
        return None

def scrape_documentation():
    """Main scraping function."""
    print("GigaSpaces Documentation Scraper")
    print("=" * 60)

    ensure_output_dir()

    # Extract URLs from llms.txt
    urls = extract_urls_from_llms_txt()

    if not urls:
        print("No URLs found to scrape")
        return

    # Filter URLs to only GigaSpaces domain
    gigaspaces_urls = [url for url in urls if 'gigaspaces.com' in url]
    print(f"Found {len(gigaspaces_urls)} GigaSpaces URLs to process")

    # Limit to reasonable number to avoid excessive downloads
    gigaspaces_urls = gigaspaces_urls[:50]

    print(f"\nDownloading {len(gigaspaces_urls)} pages...")
    print("=" * 60)

    successful = 0
    failed = 0

    # Use threading for parallel downloads
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(download_and_convert, url): url for url in gigaspaces_urls}

        for future in as_completed(futures):
            result = future.result()
            if result:
                successful += 1
            else:
                failed += 1
            # Rate limiting
            time.sleep(0.5)

    print("\n" + "=" * 60)
    print(f"Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total files in {OUTPUT_DIR}: {len(list(OUTPUT_DIR.glob('*.md')))}")
    print("\nDone!")

if __name__ == "__main__":
    scrape_documentation()
