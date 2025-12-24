#!/usr/bin/env python3
"""
TigerVNC Documentation Scraper
Downloads TigerVNC man pages and GitHub wiki pages, converting to markdown.
TigerVNC is a high-performance, platform-neutral VNC implementation.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# TigerVNC documentation pages
TIGERVNC_DOC_PAGES = {
    # Main site man pages
    "https://tigervnc.org/doc/vncconfig.html": "vncconfig.md",
    "https://tigervnc.org/doc/vncpasswd.html": "vncpasswd.md",
    "https://tigervnc.org/doc/vncsession.html": "vncsession.md",
    "https://tigervnc.org/doc/vncviewer.html": "vncviewer.md",
    "https://tigervnc.org/doc/x0vncserver.html": "x0vncserver.md",
    "https://tigervnc.org/doc/Xvnc.html": "Xvnc.md",

    # GitHub wiki pages
    "https://github.com/TigerVNC/tigervnc/wiki": "wiki-home.md",
    "https://github.com/TigerVNC/tigervnc/wiki/Setup-TigerVNC-server-(Windows)": "setup-windows-server.md",
    "https://github.com/TigerVNC/tigervnc/wiki/Secure-your-connection": "secure-connection.md",
    "https://github.com/TigerVNC/tigervnc/wiki/Compiling-TigerVNC-for-Windows": "compiling-windows.md",
    "https://github.com/TigerVNC/tigervnc/wiki/Debug-Logs": "debug-logs.md",
    "https://github.com/TigerVNC/tigervnc/wiki/Development": "development.md",
    "https://github.com/TigerVNC/tigervnc/wiki/Development:-DesktopSize": "development-desktop-size.md",
    "https://github.com/TigerVNC/tigervnc/wiki/Development:-Latency": "development-latency.md",
    "https://github.com/TigerVNC/tigervnc/wiki/Development:-Making-a-Release": "development-making-release.md",
    "https://github.com/TigerVNC/tigervnc/wiki/Development:-SetDesktopSize-Cleanup": "development-setdesktopsize-cleanup.md",
    "https://github.com/TigerVNC/tigervnc/wiki/Keyboard-shortcuts": "keyboard-shortcuts.md",
    "https://github.com/TigerVNC/tigervnc/wiki/Systemd-unit-for-x0vncserver": "systemd-x0vncserver.md",
}


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # For GitHub wiki pages, extract the wiki-body content
    if "github.com" in url and "/wiki" in url:
        wiki_match = re.search(
            r'<div[^>]*class="[^"]*markdown-body[^"]*"[^>]*>(.*?)</div>\s*</div>\s*</div>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if wiki_match:
            html_content = wiki_match.group(1)

    # For tigervnc.org man pages, extract the body content
    elif "tigervnc.org" in url:
        body_match = re.search(
            r'<body[^>]*>(.*?)</body>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if body_match:
            html_content = body_match.group(1)

    # Try pandoc for best conversion
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

        # Set user agent to avoid GitHub blocking
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; DocumentationScraper/1.0)'
        }

        response = requests.get(url, timeout=15, headers=headers)
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


def main():
    """Main function to download all TigerVNC documentation."""
    print("=" * 60)
    print("TigerVNC Documentation Scraper")
    print("=" * 60)
    print(f"Pages to download: {len(TIGERVNC_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "tigervnc"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, (url, filename) in enumerate(TIGERVNC_DOC_PAGES.items(), 1):
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(TIGERVNC_DOC_PAGES)}] ", end="")

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
