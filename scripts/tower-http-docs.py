#!/usr/bin/env python3
"""
Tower-HTTP Documentation Scraper
Downloads Tower-HTTP documentation from docs.rs and converts to markdown.
Tower-HTTP is a collection of HTTP-specific Tower middleware for Rust, including CORS, compression, and tracing.
"""

import os
import sys
import requests
from pathlib import Path
import time
from html2text import html2text
from urllib.parse import urljoin, urlparse
import re

# Base URL for Tower-HTTP documentation on docs.rs
BASE_URL = "https://docs.rs/tower-http/latest/tower_http/"

# Main modules to document
MODULES = [
    "",  # Index/main page
    "cors/",
    "compression/",
    "decompression/",
    "trace/",
    "follow_redirect/",
    "timeout/",
    "request_id/",
    "sensitive_headers/",
    "propagate_header/",
]

REQUEST_DELAY = 0.5  # seconds between requests


def sanitize_filename(path):
    """Convert path to safe filename."""
    # Remove trailing slashes
    path = path.rstrip("/")

    # If empty, use 'index'
    if not path:
        return "index.md"

    # Replace slashes with dashes
    safe = path.replace("/", "-")

    # Ensure .md extension
    if not safe.endswith('.md'):
        safe = safe + '.md'

    return safe


def html_to_markdown(html_content):
    """Convert HTML content to markdown."""
    try:
        # Use html2text for conversion
        markdown = html2text(html_content)
        return markdown
    except Exception as e:
        print(f"    Warning: Could not convert HTML to markdown: {e}")
        # Fallback: return raw content
        return html_content


def extract_main_content(html_content):
    """Extract main documentation content from docs.rs HTML."""
    try:
        # docs.rs uses specific class selectors for content
        # Try to extract from rustdoc content
        match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL)
        if match:
            return match.group(1)

        # Try section.main-content
        match = re.search(r'<section[^>]*class="[^"]*main-content[^"]*"[^>]*>(.*?)</section>', html_content, re.DOTALL)
        if match:
            return match.group(1)

        # Try body content
        match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL)
        if match:
            return match.group(1)

        # Fallback: return original
        return html_content
    except Exception as e:
        print(f"    Warning: Could not extract main content: {e}")
        return html_content


def download_page(page_path, output_dir):
    """Download a documentation page from docs.rs."""
    try:
        # Build full URL
        if page_path:
            url = urljoin(BASE_URL, page_path)
        else:
            url = BASE_URL

        # Sanitize the filename
        if page_path:
            filename = sanitize_filename(page_path)
        else:
            filename = "index.md"

        print(f"  Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        html_content = response.text

        # Extract main content
        main_content = extract_main_content(html_content)

        # Convert to markdown
        markdown_content = html_to_markdown(main_content)

        # Add metadata header
        header = f"""# Tower-HTTP Documentation
# Source: {url}
# Path: {page_path if page_path else 'index'}

"""
        content = header + markdown_content

        # Save to file
        output_path = output_dir / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {page_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {page_path}: {e}")
        return False


def main():
    """Main function to download Tower-HTTP documentation."""
    print("=" * 60)
    print("Tower-HTTP Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "tower-http"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Download all pages
    print("Downloading documentation pages...")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, page_path in enumerate(MODULES, 1):
        print(f"[{idx:2d}/{len(MODULES)}] ", end="")

        if download_page(page_path, output_dir):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(REQUEST_DELAY)

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
