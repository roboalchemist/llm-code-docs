#!/usr/bin/env python3
"""
GPT4All Documentation Scraper
Downloads GPT4All documentation from https://docs.gpt4all.io/ and converts to markdown.
GPT4All is an ecosystem for running large language models locally on consumer hardware.
"""

import os
import sys
import requests
from pathlib import Path
import time
from html2text import html2text
from urllib.parse import urljoin, urlparse
import re

# Base URL for GPT4All documentation
BASE_URL = "https://docs.gpt4all.io"

# Manual list of documentation pages to scrape
DOCS_PAGES = [
    "/",  # Index/main page
    "/gpt4all_desktop/quickstart.html",
    "/gpt4all_desktop/models.html",
    "/gpt4all_desktop/chats.html",
    "/gpt4all_desktop/localdocs.html",
    "/gpt4all_desktop/settings.html",
    "/gpt4all_desktop/chat_templates.html",
    "/gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-Obsidian.html",
    "/gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-google-drive.html",
    "/gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-One-Drive.html",
    "/gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-microsoft-excel.html",
    "/gpt4all_python/home.html",
    "/gpt4all_python/ref.html",
    "/gpt4all_python/monitoring.html",
    "/gpt4all_api_server/home.html",
    "/gpt4all_help/faq.html",
    "/gpt4all_help/troubleshooting.html",
]

REQUEST_DELAY = 1.0  # seconds between requests


def sanitize_filename(path):
    """Convert path to safe filename."""
    # Remove leading/trailing slashes
    path = path.strip("/")

    # If empty, use 'index'
    if not path:
        return "index.md"

    # Remove .html extension if present
    if path.endswith('.html'):
        path = path[:-5]

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
        # Try to extract from <main> tag
        match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL)
        if match:
            return match.group(1)

        # Try to extract from article tag
        match = re.search(r'<article[^>]*>(.*?)</article>', html_content, re.DOTALL)
        if match:
            return match.group(1)

        # Try role="main" attribute
        match = re.search(r'<div[^>]*role="main"[^>]*>(.*?)</div>', html_content, re.DOTALL)
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
    """Download a documentation page from GPT4All."""
    try:
        # Build full URL
        if page_path == "/":
            url = BASE_URL
        else:
            url = urljoin(BASE_URL, page_path)

        # Sanitize the filename
        if page_path == "/":
            filename = "index.md"
        else:
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
        header = f"""# GPT4All Documentation

Source: {url}

---

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
    """Main function to download GPT4All documentation."""
    print("=" * 70)
    print("GPT4All Documentation Scraper")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "gpt4all"
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
    print("=" * 70)
    print("Download Summary")
    print("=" * 70)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("**/*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} files failed to download")
        return 1
    else:
        print("All documentation downloaded successfully!")
        return 0


if __name__ == "__main__":
    sys.exit(main())
