#!/usr/bin/env python3
"""
AnyDesk Documentation Scraper
Downloads all AnyDesk documentation pages and converts to markdown.
AnyDesk is a remote desktop software solution.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# AnyDesk documentation pages from support site
ANYDESK_DOC_PAGES = [
    # Getting Started
    "/docs/getting-started",
    "/docs/quick-start-guide",
    "/docs/install-anydesk",
    "/docs/download-anydesk",

    # User Guides
    "/docs/user-guides",
    "/docs/using-anydesk",
    "/docs/features",
    "/docs/settings",

    # Client Platforms
    "/docs/anydesk-for-android",
    "/docs/anydesk-for-ios",
    "/docs/anydesk-for-windows",
    "/docs/anydesk-for-macos",
    "/docs/anydesk-for-linux",
    "/docs/anydesk-for-chromeos",
    "/docs/anydesk-for-raspberry-pi",
    "/docs/anydesk-for-freebsd",

    # Command Line Interface
    "/docs/command-line-interface-for-windows",
    "/docs/command-line-interface-for-linux",
    "/docs/command-line-interface-for-macos",

    # Licensing & Billing
    "/docs/licenses-billing",
    "/docs/anydesk-licenses",
    "/docs/license-types",
    "/docs/activate-license",
    "/docs/manage-licenses",
    "/docs/subscription-management",

    # myAnyDesk Portal
    "/docs/myanydesk-portal",
    "/docs/portal-getting-started",
    "/docs/address-book",
    "/docs/session-monitoring",
    "/docs/device-management",
    "/docs/custom-client",

    # Administration
    "/docs/administration",
    "/docs/organization-management",
    "/docs/user-management",
    "/docs/role-management",
    "/docs/permissions",
    "/docs/custom-client-generator",
    "/docs/deployment",
    "/docs/unattended-access",

    # Security
    "/docs/security",
    "/docs/security-settings",
    "/docs/access-control",
    "/docs/permission-profiles",
    "/docs/two-factor-authentication",
    "/docs/gdpr-compliance",
    "/docs/encryption",

    # Features
    "/docs/file-transfer",
    "/docs/session-recording",
    "/docs/remote-printing",
    "/docs/clipboard-synchronization",
    "/docs/audio-transmission",
    "/docs/remote-restart",
    "/docs/tcp-tunneling",
    "/docs/url-handler",

    # Integrations
    "/docs/anydesk-for-freshworks",
    "/docs/integrations",

    # Troubleshooting & FAQ
    "/docs/faq",
    "/docs/troubleshooting",
    "/docs/connection-issues",
    "/docs/performance-optimization",

    # API & Advanced
    "/docs/api",
    "/docs/advanced-settings",
    "/docs/registry-settings",
    "/docs/trace-files",
]

BASE_URL = "https://support.anydesk.com"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # Extract main content area (AnyDesk uses main tag or article)
    # Try to find the main content container
    article_patterns = [
        r'<main[^>]*>(.*?)</main>',
        r'<article[^>]*>(.*?)</article>',
        r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>',
        r'<div[^>]*class="[^"]*documentation[^"]*"[^>]*>(.*?)</div>',
    ]

    extracted = False
    for pattern in article_patterns:
        match = re.search(pattern, html_content, flags=re.DOTALL | re.IGNORECASE)
        if match:
            html_content = match.group(1)
            extracted = True
            break

    # Remove navigation, headers, footers
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Try pandoc first for better conversion
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

    # Fallback: basic HTML to text conversion
    # Convert headers
    for i in range(6, 0, -1):
        html_content = re.sub(
            rf'<h{i}[^>]*>(.*?)</h{i}>',
            r'\n' + '#' * i + r' \1\n',
            html_content,
            flags=re.DOTALL | re.IGNORECASE
        )

    # Code blocks
    html_content = re.sub(
        r'<pre[^>]*><code[^>]*>(.*?)</code></pre>',
        r'\n```\n\1\n```\n',
        html_content,
        flags=re.DOTALL | re.IGNORECASE
    )
    html_content = re.sub(
        r'<code[^>]*>(.*?)</code>',
        r'`\1`',
        html_content,
        flags=re.DOTALL | re.IGNORECASE
    )

    # Links
    html_content = re.sub(
        r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
        r'[\2](\1)',
        html_content,
        flags=re.DOTALL | re.IGNORECASE
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

    # Remove leading/trailing slashes and /docs/ prefix
    clean_path = path.strip("/").replace("docs/", "")

    # Handle nested paths
    if "/" in clean_path:
        return clean_path.replace("/", "-") + ".md"

    return clean_path + ".md"


def main():
    """Main function to download all AnyDesk documentation."""
    print("=" * 60)
    print("AnyDesk Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(ANYDESK_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "anydesk"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(ANYDESK_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(ANYDESK_DOC_PAGES)}] ", end="")

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
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md") if f.is_file())
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
