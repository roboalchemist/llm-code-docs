#!/usr/bin/env python3
"""
AWS CLI Documentation Scraper

Downloads AWS CLI User Guide documentation from llms.txt index and converts to markdown.
AWS llms.txt format links to HTML pages, not .md files, so we need to fetch and convert.

Usage:
    python3 aws-cli-docs.py
"""

import re
import subprocess
import sys
import time
from pathlib import Path

import requests

# Configuration
LLMS_TXT_URL = "https://docs.aws.amazon.com/cli/latest/userguide/llms.txt"
BASE_URL = "https://docs.aws.amazon.com/cli/latest/userguide/"

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
OUTPUT_DIR = REPO_ROOT / "docs" / "llms-txt" / "aws-cli"


def parse_llms_txt(content: str) -> list[tuple[str, str, str]]:
    """Parse llms.txt and extract URLs with titles and descriptions.

    Returns list of (url, title, description) tuples.
    """
    pages = []

    # Match markdown links in the format: - [Title](URL): Description
    # or: - [Title](URL)
    pattern = r'-\s*\[([^\]]+)\]\(([^)]+)\)(?::\s*(.+))?'

    for match in re.finditer(pattern, content):
        title = match.group(1).strip()
        url = match.group(2).strip()
        description = match.group(3).strip() if match.group(3) else ""

        # Only include AWS CLI userguide pages
        if 'docs.aws.amazon.com/cli/' in url:
            pages.append((url, title, description))

    return pages


def html_to_markdown(html_content: str, url: str, title: str, description: str) -> str:
    """Convert AWS documentation HTML to markdown."""

    # Try to extract main content - AWS docs use specific classes
    # Main content is usually in <main> or <div id="main-content">
    main_match = re.search(
        r'<main[^>]*id="main"[^>]*>(.*?)</main>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if main_match:
        html_content = main_match.group(1)
    else:
        # Try alternate selectors
        content_match = re.search(
            r'<div[^>]*id="main-content"[^>]*>(.*?)</div>\s*</div>\s*<awsdocs',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if content_match:
            html_content = content_match.group(1)
        else:
            # Try body content, removing nav/header/footer
            body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, flags=re.DOTALL | re.IGNORECASE)
            if body_match:
                html_content = body_match.group(1)

    # Remove navigation, sidebar, and footer elements
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<aside[^>]*>.*?</aside>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<awsdocs-[^>]*>.*?</awsdocs-[^>]*>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Try pandoc for high-quality conversion
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

            # Add header with metadata
            header = f"# {title}\n\n"
            if description:
                header += f"> {description}\n\n"
            header += f"**Source:** {url}\n\n---\n\n"

            return header + markdown
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: basic HTML to text extraction
    # Convert common HTML elements to markdown
    for i in range(6, 0, -1):
        html_content = re.sub(
            rf'<h{i}[^>]*>(.*?)</h{i}>',
            r'\n' + '#' * i + r' \1\n',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )

    # Code blocks
    html_content = re.sub(
        r'<pre[^>]*><code[^>]*>(.*?)</code></pre>',
        r'\n```\n\1\n```\n',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )
    html_content = re.sub(
        r'<code[^>]*>(.*?)</code>',
        r'`\1`',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    # Links
    html_content = re.sub(
        r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
        r'[\2](\1)',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    # Bold and italic
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)

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

    # Clean up whitespace
    html_content = re.sub(r'\n\s*\n\s*\n', '\n\n', html_content)
    html_content = html_content.strip()

    # Add header
    header = f"# {title}\n\n"
    if description:
        header += f"> {description}\n\n"
    header += f"**Source:** {url}\n\n---\n\n"

    return header + html_content


def url_to_filename(url: str) -> str:
    """Convert URL to a safe filename."""
    # Extract the page name from URL
    # e.g., https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html -> cli-chap-welcome.md
    path = url.split('/')[-1]

    # Remove .html extension and add .md
    if path.endswith('.html'):
        path = path[:-5]

    # Handle index pages
    if not path or path == 'userguide':
        path = 'index'

    return path + '.md'


def download_page(url: str, title: str, description: str, output_path: Path) -> bool:
    """Download and convert a single page."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        markdown = html_to_markdown(response.text, url, title, description)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding='utf-8')

        return True
    except requests.exceptions.RequestException as e:
        print(f"    Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"    Error processing {url}: {e}")
        return False


def main():
    """Main function to download all AWS CLI documentation."""
    print("=" * 70)
    print("AWS CLI Documentation Scraper")
    print("=" * 70)
    print(f"llms.txt URL: {LLMS_TXT_URL}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Fetch llms.txt
    print("Fetching llms.txt index...")
    try:
        response = requests.get(LLMS_TXT_URL, timeout=30)
        response.raise_for_status()
        llms_content = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching llms.txt: {e}")
        sys.exit(1)

    # Also save the llms.txt itself as the index
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "llms.txt").write_text(llms_content, encoding='utf-8')
    print(f"  Saved: llms.txt")

    # Parse pages
    pages = parse_llms_txt(llms_content)
    print(f"Found {len(pages)} documentation pages")
    print()

    # Download each page
    successful = 0
    failed = 0
    start_time = time.time()

    for i, (url, title, description) in enumerate(pages, 1):
        filename = url_to_filename(url)
        output_path = OUTPUT_DIR / filename

        print(f"[{i:2d}/{len(pages)}] {title}")
        print(f"    URL: {url}")

        if download_page(url, title, description, output_path):
            size_kb = output_path.stat().st_size / 1024
            print(f"    -> Saved: {filename} ({size_kb:.1f} KB)")
            successful += 1
        else:
            failed += 1

        # Rate limiting
        time.sleep(0.3)

    elapsed = time.time() - start_time

    print()
    print("=" * 70)
    print("Download Summary")
    print("=" * 70)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {OUTPUT_DIR}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in OUTPUT_DIR.glob("*.md"))
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
