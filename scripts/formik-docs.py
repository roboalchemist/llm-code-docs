#!/usr/bin/env python3
"""
Formik Documentation Scraper
Downloads Formik documentation from formik.org.
Formik is the world's most popular open source form library for React and React Native.
"""

import os
import sys
import requests
from pathlib import Path
import time
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import re

# Base URL for Formik documentation
BASE_URL = "https://formik.org"
DOCS_BASE = "https://formik.org/docs"

# Documentation pages to scrape
DOCS_PAGES = [
    # Overview & Getting Started
    "/docs/overview",
    "/docs/tutorial",

    # Guides
    "/docs/guides/validation",
    "/docs/guides/form-submission",
    "/docs/guides/arrays",
    "/docs/guides/typescript",
    "/docs/guides/react-native",

    # API Reference - Components
    "/docs/api/formik",
    "/docs/api/form",
    "/docs/api/field",
    "/docs/api/fastfield",
    "/docs/api/fieldarray",
    "/docs/api/errormessage",
    "/docs/api/connect",

    # API Reference - Hooks
    "/docs/api/useformik",
    "/docs/api/usefield",
    "/docs/api/useformikcontext",

    # API Reference - HOC
    "/docs/api/withformik",

    # Examples
    "/docs/examples/basic",
    "/docs/examples/checkboxes",
    "/docs/examples/radio-group",
    "/docs/examples/field-arrays",
    "/docs/examples/async-submission",
    "/docs/examples/dependent-fields",
    "/docs/examples/dependent-fields-async-api-request",
    "/docs/examples/instant-feedback",
    "/docs/examples/typescript",
    "/docs/examples/with-material-ui",

    # Integration & Migration
    "/docs/3rd-party-bindings",
    "/docs/migrating-v2",
    "/docs/resources",
]

# Rate limiting
REQUEST_DELAY = 1  # seconds between requests
REQUEST_TIMEOUT = 15


def extract_markdown_from_page(html_content, page_url):
    """Extract markdown-like content from HTML page."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script and style tags
    for script in soup(["script", "style"]):
        script.decompose()

    # Try to find the main content area
    # Formik.org uses various content container classes
    main_content = None
    for selector in ['main', '[role="main"]', '.main-content', '.content', 'article']:
        main_content = soup.find(selector)
        if main_content:
            break

    if not main_content:
        # Fall back to body
        main_content = soup.find('body')

    if not main_content:
        return None

    # Extract text content
    text_parts = []

    # Get all paragraphs, headers, code blocks, lists
    for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'code', 'pre']):
        if element.name.startswith('h'):
            text_parts.append(f"\n{'#' * int(element.name[1])} {element.get_text(strip=True)}\n")
        elif element.name == 'p':
            text = element.get_text(strip=True)
            if text:
                text_parts.append(text)
                text_parts.append("")
        elif element.name == 'li':
            text = element.get_text(strip=True)
            if text:
                text_parts.append(f"- {text}")
        elif element.name == 'code':
            text = element.get_text(strip=True)
            if text and len(text) < 100:  # Inline code
                text_parts.append(f"`{text}`")
        elif element.name == 'pre':
            # Code block
            code_text = element.get_text(strip=True)
            if code_text:
                text_parts.append(f"\n```\n{code_text}\n```\n")

    content = "\n".join(text_parts)

    # Clean up excessive whitespace
    content = re.sub(r'\n\n+', '\n\n', content)

    return content.strip()


def download_page(page_path):
    """Download a single page from Formik docs."""
    try:
        url = urljoin(BASE_URL, page_path)

        print(f"  Downloading: {page_path}")

        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        # Extract markdown-style content
        content = extract_markdown_from_page(response.text, url)

        if not content:
            print(f"    -> Error: Could not extract content from {page_path}")
            return None

        # Add metadata header
        header = f"""# Formik Documentation
# Source: {url}
# Path: {page_path}

"""
        content = header + content

        return content

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {page_path}: {e}")
        return None
    except Exception as e:
        print(f"    -> Error processing {page_path}: {e}")
        return None


def sanitize_filename(page_path):
    """Convert page path to safe filename."""
    # Remove leading/trailing slashes
    path = page_path.strip('/')
    # Remove /docs prefix
    if path.startswith('docs/'):
        path = path[5:]
    # Replace slashes with dashes
    path = path.replace('/', '-')
    # Ensure .md extension
    if not path.endswith('.md'):
        path = f"{path}.md"
    return path


def main():
    """Main function to download all Formik documentation."""
    print("=" * 60)
    print("Formik Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "formik"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print(f"Scraping {len(DOCS_PAGES)} documentation pages...")
    print()

    start_time = time.time()
    successful = 0
    failed = 0

    for idx, page_path in enumerate(DOCS_PAGES, 1):
        print(f"[{idx:2d}/{len(DOCS_PAGES)}] ", end="")

        content = download_page(page_path)

        if content:
            # Create output filename
            output_filename = sanitize_filename(page_path)
            output_path = output_dir / output_filename

            # Create output file
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"✓ Saved: {output_filename}")
            successful += 1
        else:
            print(f"✗ Failed: {page_path}")
            failed += 1

        # Rate limiting
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
    total_size = sum(f.stat().st_size for f in output_dir.rglob("*.md"))
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
