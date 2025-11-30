#!/usr/bin/env python3
"""
Mozilla Data Collective Documentation Scraper
Downloads API documentation and Python library docs.
MDC provides programmatic access to community-driven datasets.
"""

import os
import sys
import requests
from pathlib import Path
import time
import re
import subprocess

# GitHub raw files for Python library documentation
PYTHON_LIB_DOCS = [
    "README.md",
    "docs/api.md",
    "docs/index.md",
    "docs/release.md",
    "src/datacollective/dataset_loading_scripts/README.md",
]

PYTHON_LIB_RAW = "https://raw.githubusercontent.com/Mozilla-Data-Collective/datacollective-python/main"

# Web pages to scrape from the main site
WEB_PAGES = [
    ("https://datacollective.mozillafoundation.org/api-reference", "api-reference.md"),
    ("https://datacollective.mozillafoundation.org/api-reference/docs", "api-docs.md"),
]


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content."""
    # Try pandoc first
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

    # Fallback: basic HTML to text extraction
    # Remove script and style elements
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Convert common HTML elements to markdown
    # Headers
    for i in range(6, 0, -1):
        html_content = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', r'\n' + '#' * i + r' \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Code blocks
    html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Links
    html_content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Bold and italic
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Lists
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<[ou]l[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</[ou]l>', '\n', html_content, flags=re.IGNORECASE)

    # Paragraphs and line breaks
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</div>', '\n', html_content, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Decode HTML entities
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&quot;', '"')
    html_content = html_content.replace('&#39;', "'")
    html_content = html_content.replace('&#x27;', "'")

    # Clean up whitespace
    html_content = re.sub(r'\n\s*\n\s*\n', '\n\n', html_content)
    html_content = html_content.strip()

    return f"# Source: {url}\n\n{html_content}"


def download_github_file(url, output_path):
    """Download a file from GitHub and add source header."""
    try:
        print(f"Downloading: {url}")
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add source header
        content = f"# Source: {url}\n\n{content}"

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def download_web_page(url, output_path):
    """Download a web page and convert to markdown."""
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


def path_to_filename(path, prefix=""):
    """Convert path to flat filename."""
    if prefix:
        path = f"{prefix}-{path}"

    # Remove leading slashes
    path = path.lstrip("/")

    # Convert slashes to dashes for flat structure
    filename = path.replace("/", "-")

    # Ensure .md extension
    if not filename.endswith(".md"):
        filename += ".md"

    return filename


def main():
    """Main function to download all Mozilla Data Collective documentation."""
    print("=" * 60)
    print("Mozilla Data Collective Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "llms-txt" / "mozilla-data-collective"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    # First, save the llms.txt file
    print("=" * 60)
    print("Downloading llms.txt...")
    print("=" * 60)
    try:
        response = requests.get("https://datacollective.mozillafoundation.org/llms.txt", timeout=15)
        response.raise_for_status()
        llms_path = output_dir / "llms.txt"
        with open(llms_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"  -> Saved: {llms_path}")
        successful += 1
    except Exception as e:
        print(f"  -> Error: {e}")
        failed += 1

    # Download web pages (API docs)
    print()
    print("=" * 60)
    print("Downloading API documentation pages...")
    print("=" * 60)

    for url, filename in WEB_PAGES:
        output_path = output_dir / filename

        if download_web_page(url, output_path):
            successful += 1
        else:
            failed += 1

        time.sleep(0.3)

    # Download Python library docs from GitHub
    print()
    print("=" * 60)
    print("Downloading Python library documentation...")
    print("=" * 60)

    for file_path in PYTHON_LIB_DOCS:
        url = f"{PYTHON_LIB_RAW}/{file_path}"
        filename = path_to_filename(file_path, prefix="python")
        output_path = output_dir / filename

        if download_github_file(url, output_path):
            successful += 1
        else:
            failed += 1

        time.sleep(0.3)

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
    total_size = sum(f.stat().st_size for f in output_dir.glob("*") if f.is_file())
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} files failed to download")
        sys.exit(1)
    else:
        print("All files downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
