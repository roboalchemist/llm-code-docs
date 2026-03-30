#!/usr/bin/env python3
"""
Aethir Documentation Scraper
Scrapes comprehensive documentation from docs.aethir.com for the Aethir decentralized GPU cloud platform.

Aethir is a distributed cloud compute infrastructure aggregating enterprise-grade GPU resources
into a global network serving AI, gaming, and virtualized compute markets.

Features covered:
- API reference and developer guides
- GPU-as-a-Service (GaaS) platform
- Container management and deployment
- Checker nodes for network validation
- Cloud hosting (CPU/GPU infrastructure)
- Tokenomics and staking
- Enterprise features
- Network architecture (Containers, Checkers, Indexers)
"""

import requests
import time
import sys
from pathlib import Path
from html2text import HTML2Text
from urllib.parse import urljoin, urlparse
from collections import deque

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "aethir"

# Base URL for Aethir documentation
BASE_URL = "https://docs.aethir.com"

# URLs to scrape - comprehensive documentation structure
DOCUMENTATION_URLS = [
    # Executive Summary and Introduction
    "/",
    "/aethir-introduction",
    "/aethir-introduction/key-features",
    "/aethir-introduction/faq",

    # Network Architecture
    "/aethir-network",
    "/aethir-network/the-container",
    "/aethir-network/the-checker",
    "/aethir-network/the-checker/proof-of-capacity-and-delivery",
    "/aethir-network/the-indexer",

    # Aethir Cloud Platform
    "/aethir-cloud",

    # Cloud Host Documentation (GPU/CPU providers)
    "/aethir-cloud/aethir-cloud-host",
    "/aethir-cloud/aethir-cloud-host/cloud-host-portal-guide",
    "/aethir-cloud/aethir-cloud-host/cloud-host-portal-guide/get-started",
    "/aethir-cloud/aethir-cloud-host/cloud-host-portal-guide/manage-your-wallet",
    "/aethir-cloud/aethir-cloud-host/cloud-host-portal-guide/register-a-machine",
    "/aethir-cloud/aethir-cloud-host/cloud-host-portal-guide/manage-your-machine",
    "/aethir-cloud/aethir-cloud-host/rewards-and-service-fees-for-cloud-hosts",
    "/aethir-cloud/aethir-cloud-host/rewards-and-service-fees-for-cloud-hosts/rewards-for-cloud-host",
    "/aethir-cloud/aethir-cloud-host/rewards-and-service-fees-for-cloud-hosts/service-fees",

    # Cloud Customer Documentation (GPU/compute users)
    "/aethir-cloud/aethir-cloud-customer",
    "/aethir-cloud/aethir-cloud-customer/cloud-customer-portal-guide",
    "/aethir-cloud/aethir-cloud-customer/cloud-customer-portal-guide/get-started",
    "/aethir-cloud/aethir-cloud-customer/cloud-customer-portal-guide/how-to-create-a-container",
    "/aethir-cloud/aethir-cloud-customer/cloud-customer-portal-guide/how-to-submit-a-request",
    "/aethir-cloud/aethir-cloud-customer/cloud-customer-portal-guide/manage-your-wallet",
    "/aethir-cloud/aethir-cloud-customer/rewards-for-cloud-customers",
    "/aethir-cloud/aethir-cloud-customer/pricing",

    # Tokenomics and Staking
    "/aethir-token",
    "/aethir-token/tokenomics",
    "/aethir-token/staking",

    # Whitepaper
    "/whitepaper",
]

# Headers to avoid blocking
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': BASE_URL,
}


def clean_html_to_markdown(html_content):
    """Convert HTML content to clean markdown."""
    h = HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # Disable line wrapping
    h.unicode_snob = True

    # Convert HTML to markdown
    markdown = h.handle(html_content)

    # Clean up excessive whitespace
    lines = markdown.split('\n')
    cleaned_lines = []
    prev_blank = False

    for line in lines:
        is_blank = line.strip() == ''
        if is_blank:
            if not prev_blank:
                cleaned_lines.append('')
            prev_blank = True
        else:
            cleaned_lines.append(line)
            prev_blank = False

    # Join and remove trailing whitespace
    result = '\n'.join(cleaned_lines).strip()
    return result


def fetch_page(url, max_retries=3):
    """Fetch a single page with retries."""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=15)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 2
                print(f"    -> Retry {attempt + 1}/{max_retries} for {url} (waiting {wait_time}s): {e}")
                time.sleep(wait_time)
            else:
                print(f"    -> Failed to fetch {url}: {e}")
                return None


def scrape_documentation():
    """Scrape all documentation from Aethir."""
    print("=" * 70)
    print("Aethir Documentation Scraper")
    print("=" * 70)
    print()
    print(f"Base URL: {BASE_URL}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    successfully_scraped = []
    failed_urls = []

    print("Scraping documentation pages...")
    print()

    for i, path in enumerate(DOCUMENTATION_URLS, 1):
        url = urljoin(BASE_URL, path)
        print(f"[{i}/{len(DOCUMENTATION_URLS)}] Fetching: {url}")

        # Fetch the page
        html_content = fetch_page(url)
        if not html_content:
            failed_urls.append(url)
            continue

        # Convert to markdown
        try:
            markdown_content = clean_html_to_markdown(html_content)
        except Exception as e:
            print(f"    -> Error converting HTML to markdown: {e}")
            failed_urls.append(url)
            continue

        # Determine output filename
        if path == "/":
            filename = "index.md"
        else:
            # Convert path to filename (e.g., /aethir-network/the-container -> aethir-network_the-container.md)
            filename = path.strip('/').replace('/', '_') + '.md'

        output_file = OUTPUT_DIR / filename

        # Add source header
        source_header = f"# Source: {url}\n\n"
        full_content = source_header + markdown_content

        # Write to file
        try:
            output_file.write_text(full_content, encoding='utf-8')
            successfully_scraped.append((path, output_file.name))
            print(f"    -> Saved: {filename} ({len(full_content)} bytes)")
        except Exception as e:
            print(f"    -> Error saving file: {e}")
            failed_urls.append(url)
            continue

        # Rate limiting - be polite
        time.sleep(1.5)

    print()
    print("=" * 70)
    print("Scraping Summary")
    print("=" * 70)
    print()

    print(f"Successfully scraped: {len(successfully_scraped)} pages")
    print(f"Failed: {len(failed_urls)} pages")

    if successfully_scraped:
        print()
        print("Scraped pages:")
        for path, filename in successfully_scraped[:15]:
            print(f"  - {path} -> {filename}")
        if len(successfully_scraped) > 15:
            print(f"  ... and {len(successfully_scraped) - 15} more")

    if failed_urls:
        print()
        print("Failed URLs:")
        for url in failed_urls[:10]:
            print(f"  - {url}")
        if len(failed_urls) > 10:
            print(f"  ... and {len(failed_urls) - 10} more")

    # Verify extraction
    print()
    print("Verification:")

    all_files = list(OUTPUT_DIR.glob("*.md"))
    total_size = sum(f.stat().st_size for f in all_files)

    print(f"  Total files: {len(all_files)}")
    print(f"  Total size: {total_size:,} bytes ({total_size / 1024 / 1024:.2f} MB)")

    if len(all_files) > 0:
        print()
        print("  Sample files:")
        for file in sorted(all_files)[:5]:
            file_size = file.stat().st_size
            print(f"    - {file.name} ({file_size:,} bytes)")
        if len(all_files) > 5:
            print(f"    ... and {len(all_files) - 5} more")

    print()
    print("=" * 70)
    print("Extraction Complete")
    print("=" * 70)
    print(f"Output: {OUTPUT_DIR}")
    print()

    return len(successfully_scraped) > 0


if __name__ == "__main__":
    try:
        success = scrape_documentation()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
