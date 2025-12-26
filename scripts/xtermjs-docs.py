#!/usr/bin/env python3
"""
xterm.js Documentation Scraper
Downloads all xterm.js documentation pages and converts to markdown.
xterm.js is a terminal emulator library for the web.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# xterm.js documentation pages
XTERMJS_DOC_PAGES = [
    # Main docs page
    "/docs/",

    # Guides
    "/docs/guides/download/",
    "/docs/guides/encoding/",
    "/docs/guides/flowcontrol/",
    "/docs/guides/hooks/",
    "/docs/guides/import/",
    "/docs/guides/link-handling/",
    "/docs/guides/security/",
    "/docs/guides/using-addons/",

    # API Reference
    "/docs/api/vtfeatures/",
    "/docs/api/terminal/modules/xterm/",
    "/docs/api/terminal/classes/terminal/",

    # Interfaces
    "/docs/api/terminal/interfaces/ibuffer/",
    "/docs/api/terminal/interfaces/ibuffercell/",
    "/docs/api/terminal/interfaces/ibuffercellposition/",
    "/docs/api/terminal/interfaces/ibufferelementprovider/",
    "/docs/api/terminal/interfaces/ibufferline/",
    "/docs/api/terminal/interfaces/ibuffernamespace/",
    "/docs/api/terminal/interfaces/ibufferrange/",
    "/docs/api/terminal/interfaces/idecoration/",
    "/docs/api/terminal/interfaces/idecorationoptions/",
    "/docs/api/terminal/interfaces/idecorationoverviewruleroptions/",
    "/docs/api/terminal/interfaces/idisposable/",
    "/docs/api/terminal/interfaces/idisposablewithevent/",
    "/docs/api/terminal/interfaces/ievent/",
    "/docs/api/terminal/interfaces/ifunctionidentifier/",
    "/docs/api/terminal/interfaces/ilink/",
    "/docs/api/terminal/interfaces/ilinkdecorations/",
    "/docs/api/terminal/interfaces/ilinkhandler/",
    "/docs/api/terminal/interfaces/ilinkprovider/",
    "/docs/api/terminal/interfaces/ilocalizablestrings/",
    "/docs/api/terminal/interfaces/ilogger/",
    "/docs/api/terminal/interfaces/imarker/",
    "/docs/api/terminal/interfaces/imodes/",
    "/docs/api/terminal/interfaces/iparser/",
    "/docs/api/terminal/interfaces/iterminaladdon/",
    "/docs/api/terminal/interfaces/iterminalinitonlyoptions/",
    "/docs/api/terminal/interfaces/iterminaloptions/",
    "/docs/api/terminal/interfaces/itheme/",
    "/docs/api/terminal/interfaces/iunicodehandling/",
    "/docs/api/terminal/interfaces/iunicodeversionprovider/",
    "/docs/api/terminal/interfaces/iviewportrange/",
    "/docs/api/terminal/interfaces/iwindowoptions/",
]

BASE_URL = "https://xtermjs.org"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # First, extract just the main content area
    # xterm.js docs use <div class="container"> for main content
    container_match = re.search(
        r'<div[^>]*class="[^"]*container[^"]*"[^>]*>(.*?)</div>\s*<footer',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if container_match:
        html_content = container_match.group(1)
    else:
        # Try alternate selector - look for main content area
        main_match = re.search(
            r'<main[^>]*>(.*?)</main>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if main_match:
            html_content = main_match.group(1)

    # Try pandoc on cleaned content
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
            markdown = re.sub(r'^::+.*$', '', markdown, flags=re.MULTILINE)  # Remove ::: div markers
            markdown = re.sub(r'\{[^}]*\}', '', markdown)  # Remove {.class} attributes
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)  # Normalize whitespace
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

    return f"# Source: {url}\n\n{html_content}"


def download_page(url, output_path):
    """Download a page and convert to markdown."""
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


def path_to_filename(path):
    """Convert URL path to filename."""
    if path == "/" or path == "":
        return "index.md"

    # Remove leading/trailing slashes and convert to filename
    clean_path = path.strip("/")

    # Handle nested paths like /docs/guides/download/
    if "/" in clean_path:
        # Convert to flat filename: docs/guides/download -> docs-guides-download.md
        return clean_path.replace("/", "-") + ".md"

    return clean_path + ".md"


def main():
    """Main function to download all xterm.js documentation."""
    print("=" * 60)
    print("xterm.js Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(XTERMJS_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "xtermjs"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(XTERMJS_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(XTERMJS_DOC_PAGES)}] ", end="")

        if download_page(url, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.5)

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
        print(f"Warning: {failed} pages failed to download")
        sys.exit(1)
    else:
        print("All pages downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
