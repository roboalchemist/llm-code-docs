#!/usr/bin/env python3
"""
iTerm2 Documentation Scraper
Downloads all iTerm2 documentation pages and converts to markdown.
iTerm2 is a macOS terminal emulator with advanced features.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# iTerm2 documentation pages from their documentation page
ITERM2_DOC_PAGES = [
    # Introduction
    "/documentation-highlights.html",
    "/documentation-general-usage.html",
    # User Interface
    "/documentation-menu-items.html",
    "/documentation-preferences.html",
    "/documentation-touch-bar.html",
    "/documentation-copymode.html",
    "/documentation-fonts.html",
    "/documentation-search-syntax.html",
    "/documentation-command-selection.html",
    "/documentation-status-bar.html",
    # Features
    "/documentation-automatic-profile-switching.html",
    "/documentation-badges.html",
    "/documentation-buried-sessions.html",
    "/documentation-captured-output.html",
    "/documentation-coprocesses.html",
    "/documentation-hotkey.html",
    "/documentation-restoration.html",
    "/documentation-shell-integration.html",
    "/documentation-smart-selection.html",
    "/documentation-tmux-integration.html",
    "/documentation-triggers.html",
    "/documentation-utilities.html",
    "/documentation-web.html",
    "/documentation-ai-chat.html",
    # Scripting
    "/documentation-scripting-fundamentals.html",
    "/documentation-variables.html",
    "/documentation-scripting.html",  # AppleScript (deprecated)
    # Advanced
    "/documentation-dynamic-profiles.html",
    "/documentation-images.html",
    "/documentation-escape-codes.html",
    # Additional pages
    "/faq.html",
    "/features.html",
]

BASE_URL = "https://iterm2.com"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # iTerm2 uses Foundation framework, extract the main panel
    main_match = re.search(
        r'<div[^>]*class="[^"]*main panel[^"]*"[^>]*>(.*?)</div>\s*</div>\s*</div>\s*<footer',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if main_match:
        html_content = main_match.group(1)
    else:
        # Try alternate selector - look for main content area
        main_match = re.search(
            r'<div class="main panel">(.*?)</div>\s*</div>\s*</div>\s*<footer',
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
    html_content = re.sub(r'<pre[^>]*>(.*?)</pre>', r'\n```\n\1\n```\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Links - make them absolute
    html_content = re.sub(r'<a[^>]*href="(/[^"]*)"[^>]*>(.*?)</a>', rf'[\2]({BASE_URL}\1)', html_content, flags=re.DOTALL | re.IGNORECASE)
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

        size_kb = len(markdown) / 1024
        print(f"  -> Saved: {output_path.name} ({size_kb:.1f} KB)")
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

    # Remove leading/trailing slashes and .html extension
    clean_path = path.strip("/")
    if clean_path.endswith(".html"):
        clean_path = clean_path[:-5]

    # Remove 'documentation-' prefix for cleaner names
    if clean_path.startswith("documentation-"):
        clean_path = clean_path[14:]

    return clean_path + ".md"


def main():
    """Main function to download all iTerm2 documentation."""
    print("=" * 60)
    print("iTerm2 Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(ITERM2_DOC_PAGES)}")
    print()

    # Output directory - use llms-txt since we're replacing the broken llms.txt content
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "llms-txt" / "iterm2"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Remove the broken llms-full.md file
    broken_file = output_dir / "iterm2-full.md"
    if broken_file.exists():
        broken_file.unlink()
        print(f"Removed broken file: {broken_file}")

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(ITERM2_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(ITERM2_DOC_PAGES)}] ", end="")

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
