#!/usr/bin/env python3
"""
Google Cloud Platform Documentation Scraper
Downloads Google Cloud Platform documentation from docs.cloud.google.com.
Focuses on key product documentation pages to provide comprehensive GCP reference.
"""

import os
import sys
import requests
from pathlib import Path
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import html2text

# Base URL for Google Cloud documentation
BASE_URL = "https://docs.cloud.google.com"

# Key documentation pages to scrape
DOCS_PAGES = [
    "/docs",  # Main docs hub
    "/docs/overview",  # Overview
    "/compute/docs",  # Compute Engine
    "/storage/docs",  # Cloud Storage
    "/sql/docs",  # Cloud SQL
    "/bigquery/docs",  # BigQuery
    "/kubernetes-engine/docs",  # GKE
    "/run/docs",  # Cloud Run
    "/functions/docs",  # Cloud Functions
    "/appengine/docs",  # App Engine
    "/pubsub/docs",  # Pub/Sub
    "/firestore/docs",  # Firestore
    "/datastore/docs",  # Datastore
    "/spanner/docs",  # Cloud Spanner
    "/bigtable/docs",  # Cloud Bigtable
    "/monitoring/docs",  # Cloud Monitoring
    "/logging/docs",  # Cloud Logging
    "/trace/docs",  # Cloud Trace
    "/iam/docs",  # IAM
    "/vpc/docs",  # VPC
    "/load-balancing/docs",  # Load Balancing
    "/dns/docs",  # Cloud DNS
    "/cdn/docs",  # Cloud CDN
    "/armor/docs",  # Cloud Armor
    "/ai-platform/docs",  # AI Platform
    "/vertex-ai/docs",  # Vertex AI
    "/speech-to-text/docs",  # Speech-to-Text
    "/text-to-speech/docs",  # Text-to-Speech
    "/vision/docs",  # Vision API
    "/natural-language/docs",  # Natural Language API
    "/translate/docs",  # Translation API
]


def html_to_markdown(html_content, url):
    """Convert HTML content to markdown."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # Don't wrap text

    try:
        markdown = h.handle(html_content)
        return markdown
    except Exception as e:
        print(f"    -> Warning: Error converting HTML to markdown: {e}")
        return html_content


def extract_main_content(soup):
    """Extract the main content from the page, excluding navigation and headers."""
    # Try to find the main content area
    main_content = None

    # Common selectors for main content
    selectors = [
        'main',
        'article',
        '[role="main"]',
        '.devsite-article-body',
        '#gc-wrapper',
    ]

    for selector in selectors:
        main_content = soup.select_one(selector)
        if main_content:
            break

    if not main_content:
        # Fallback to body
        main_content = soup.find('body')

    return str(main_content) if main_content else str(soup)


def download_page(page_path, output_path):
    """Download a documentation page and convert to markdown."""
    try:
        url = urljoin(BASE_URL, page_path)

        print(f"  Downloading: {url}")

        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; Documentation Scraper/1.0)'
        }

        response = requests.get(url, timeout=30, headers=headers)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title
        title = soup.find('title')
        title_text = title.get_text().strip() if title else "Google Cloud Documentation"

        # Extract main content
        main_content_html = extract_main_content(soup)

        # Convert to markdown
        markdown_content = html_to_markdown(main_content_html, url)

        # Add metadata header
        header = f"""# {title_text}
# Source: {url}
# Path: {page_path}

"""
        content = header + markdown_content

        # Create output file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {page_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {page_path}: {e}")
        return False


def main():
    """Main function to download all Google Cloud documentation."""
    print("=" * 60)
    print("Google Cloud Platform Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "google-cloud"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()
    print(f"Downloading {len(DOCS_PAGES)} key documentation pages...")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, page_path in enumerate(DOCS_PAGES, 1):
        print(f"[{idx:2d}/{len(DOCS_PAGES)}] ", end="")

        # Create output filename from path
        # /compute/docs -> compute-docs.md
        # /docs -> main-docs.md
        if page_path == "/docs":
            output_filename = "main-docs.md"
        else:
            output_filename = page_path.strip('/').replace('/', '-') + '.md'

        output_path = output_dir / output_filename

        if download_page(page_path, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(1)

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
        print(f"Warning: {failed} files failed to download")
        sys.exit(1)
    else:
        print("All documentation downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
