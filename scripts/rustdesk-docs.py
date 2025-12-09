#!/usr/bin/env python3
"""
RustDesk Documentation Scraper
Downloads all RustDesk documentation pages and converts to markdown.
RustDesk is an open-source remote desktop software.
"""

import re
import subprocess
import sys
import time
from pathlib import Path

import requests

# RustDesk documentation pages extracted from sidebar
RUSTDESK_DOC_PAGES = [
    "/docs/en/",
    "/docs/en/client/",
    "/docs/en/client/android/",
    "/docs/en/client/linux/",
    "/docs/en/client/mac/",
    "/docs/en/client/windows/",
    "/docs/en/client/windows/msi/",
    "/docs/en/client/windows/windows-portable-elevation/",
    "/docs/en/dev/",
    "/docs/en/dev/build/",
    "/docs/en/dev/build/faq/",
    "/docs/en/dev/build/linux/",
    "/docs/en/dev/build/osx/",
    "/docs/en/dev/build/windows/",
    "/docs/en/self-host/",
    "/docs/en/self-host/client-configuration/",
    "/docs/en/self-host/client-configuration/advanced-settings/",
    "/docs/en/self-host/client-deployment/",
    "/docs/en/self-host/nat-loopback-issues/",
    "/docs/en/self-host/rustdesk-server-oss/",
    "/docs/en/self-host/rustdesk-server-oss/docker/",
    "/docs/en/self-host/rustdesk-server-oss/install/",
    "/docs/en/self-host/rustdesk-server-oss/synology/",
    "/docs/en/self-host/rustdesk-server-oss/synology/dsm-6/",
    "/docs/en/self-host/rustdesk-server-oss/synology/dsm-7/",
    "/docs/en/self-host/rustdesk-server-oss/windows/",
    "/docs/en/self-host/rustdesk-server-pro/",
    "/docs/en/self-host/rustdesk-server-pro/2fa/",
    "/docs/en/self-host/rustdesk-server-pro/console/",
    "/docs/en/self-host/rustdesk-server-pro/faq/",
    "/docs/en/self-host/rustdesk-server-pro/installscript/",
    "/docs/en/self-host/rustdesk-server-pro/installscript/docker/",
    "/docs/en/self-host/rustdesk-server-pro/installscript/script/",
    "/docs/en/self-host/rustdesk-server-pro/installscript/windows/",
    "/docs/en/self-host/rustdesk-server-pro/ldap/",
    "/docs/en/self-host/rustdesk-server-pro/license/",
    "/docs/en/self-host/rustdesk-server-pro/oidc/",
    "/docs/en/self-host/rustdesk-server-pro/oidc/azure/",
    "/docs/en/self-host/rustdesk-server-pro/permissions/",
    "/docs/en/self-host/rustdesk-server-pro/relay/",
    "/docs/en/self-host/rustdesk-server-pro/smtp/",
    "/docs/en/self-host/rustdesk-server-pro/strategy/",
    "/docs/en/videos/",
]

BASE_URL = "https://rustdesk.com"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # RustDesk uses Hugo/Hextra - look for main content area
    # Try to find the main content section
    main_match = re.search(
        r'<main[^>]*>(.*?)</main>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if main_match:
        html_content = main_match.group(1)
    else:
        # Try article tag
        article_match = re.search(
            r'<article[^>]*>(.*?)</article>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if article_match:
            html_content = article_match.group(1)

    # Remove navigation, sidebar, and footer elements
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<aside[^>]*>.*?</aside>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Try pandoc first for high-quality conversion
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
    # Remove /docs/en/ prefix and trailing slash
    clean_path = path.replace("/docs/en/", "").strip("/")

    if clean_path == "" or clean_path == "/":
        return "index.md"

    # Handle nested paths: client/windows/msi -> client-windows-msi.md
    if "/" in clean_path:
        return clean_path.replace("/", "-") + ".md"

    return clean_path + ".md"


def main():
    """Main function to download all RustDesk documentation."""
    print("=" * 60)
    print("RustDesk Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(RUSTDESK_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "rustdesk"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(RUSTDESK_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(RUSTDESK_DOC_PAGES)}] ", end="")

        if download_page(url, output_path):
            successful += 1
        else:
            failed += 1

        # Rate limiting
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
