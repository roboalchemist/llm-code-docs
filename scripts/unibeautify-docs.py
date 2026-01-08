#!/usr/bin/env python3
"""
Unibeautify Documentation Scraper
Downloads Unibeautify documentation from unibeautify.com
Unibeautify is a universal beautifier supporting TypeScript, JSX and other languages.
"""

import os
import sys
import requests
from pathlib import Path
import time
from html2text import html2text
from urllib.parse import urljoin
import re

# Base URL for Unibeautify documentation
BASE_URL = "https://unibeautify.com"

# Documentation pages to scrape
DOCS_PAGES = [
    "/docs/about",
    "/docs/getting-started",
    "/docs/cli",
    "/docs/config-file",
    "/docs/options-for-languages",
    "/docs/language-html",
    "/docs/language-css",
    "/docs/language-javascript",
    "/docs/language-typescript",
    "/docs/language-jsx",
    "/docs/language-vue",
    "/docs/language-cpp",
    "/docs/language-go",
    "/docs/language-objective-c",
    "/docs/language-java",
    "/docs/language-python",
    "/docs/language-php",
    "/docs/language-graphql",
    "/docs/language-markdown",
    "/docs/contributing-examples",
    "/docs/credits",
]

REQUEST_DELAY = 0.5  # seconds between requests


def sanitize_filename(path):
    """Convert path to safe filename."""
    # Remove leading/trailing slashes
    path = path.strip("/")

    # Remove the 'docs/' prefix if present
    if path.startswith("docs/"):
        path = path[5:]

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
    """Extract main documentation content from HTML."""
    try:
        # Try to extract from main content area
        # Look for common doc site patterns

        # Try main tag first
        match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL)
        if match:
            return match.group(1)

        # Try article tag
        match = re.search(r'<article[^>]*>(.*?)</article>', html_content, re.DOTALL)
        if match:
            return match.group(1)

        # Try div with class containing 'content'
        match = re.search(r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>',
                         html_content, re.DOTALL | re.IGNORECASE)
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
    """Download a documentation page."""
    try:
        # Build full URL
        url = urljoin(BASE_URL, page_path)

        # Sanitize the filename
        filename = sanitize_filename(page_path)

        print(f"  Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        html_content = response.text

        # Extract main content
        main_content = extract_main_content(html_content)

        # Convert to markdown
        markdown_content = html_to_markdown(main_content)

        # Add metadata header
        header = f"""# Unibeautify Documentation
# Source: {url}

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
    """Main function to download Unibeautify documentation."""
    print("=" * 60)
    print("Unibeautify Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "unibeautify"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Download all pages
    print("Downloading documentation pages...")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, page_path in enumerate(DOCS_PAGES, 1):
        print(f"[{idx:2d}/{len(DOCS_PAGES)}] ", end="")

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
