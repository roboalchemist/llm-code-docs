#!/usr/bin/env python3
"""
Pillow Documentation Scraper
Downloads Pillow (Python Imaging Library) documentation from ReadTheDocs and converts to markdown.
Pillow is a Python image processing library for opening, manipulating, and saving images.
"""

import os
import sys
import requests
from pathlib import Path
import time
from html2text import html2text
from urllib.parse import urljoin, urlparse
import re

# Base URL for Pillow documentation
BASE_URL = "https://pillow.readthedocs.io/en/latest/"

# Manual list of documentation pages to scrape
DOCS_PAGES = [
    "",  # Index/main page
    "about.html",
    "installation/index.html",
    "installation/basic-installation.html",
    "installation/python-support.html",
    "installation/platform-support.html",
    "installation/building-from-source.html",
    "handbook/index.html",
    "handbook/overview.html",
    "handbook/tutorial.html",
    "handbook/concepts.html",
    "handbook/appendices.html",
    "handbook/image-file-formats.html",
    "handbook/text-anchors.html",
    "handbook/third-party-plugins.html",
    "handbook/writing-your-own-image-plugin.html",
    "reference/index.html",
    "reference/Image.html",
    "reference/ImageChops.html",
    "reference/ImageCms.html",
    "reference/ImageColor.html",
    "reference/ImageDraw.html",
    "reference/ImageEnhance.html",
    "reference/ImageFile.html",
    "reference/ImageFilter.html",
    "reference/ImageFont.html",
    "reference/ImageGrab.html",
    "reference/ImageMath.html",
    "reference/ImageMorph.html",
    "reference/ImageOps.html",
    "reference/ImagePalette.html",
    "reference/ImagePath.html",
    "reference/ImageSequence.html",
    "reference/ImageStat.html",
    "reference/ImageTk.html",
    "reference/ImageTransform.html",
    "reference/ImageWin.html",
    "reference/PSDraw.html",
    "reference/features.html",
    "reference/plugins.html",
    "reference/internal-PIL-core.html",
    "reference/internal-PIL-tkinter-support.html",
    "reference/internal-PIL-display-image-in-tkinter.html",
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

    # Remove .html extension
    if safe.endswith('.html'):
        safe = safe[:-5]

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
    """Extract main documentation content from ReadTheDocs HTML."""
    try:
        # Find content between specific markers
        # ReadTheDocs uses role="main" or specific class selectors

        # Try to extract from role="main"
        match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL)
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
    """Download a documentation page from ReadTheDocs."""
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
        header = f"""# Pillow Documentation
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
    """Main function to download Pillow documentation."""
    print("=" * 60)
    print("Pillow Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "pillow"
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
    total_size = sum(f.stat().st_size for f in output_dir.glob("**/*.md"))
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
