#!/usr/bin/env python3
"""
RealVNC Documentation Scraper
Downloads RealVNC help center articles and converts to markdown.
RealVNC provides remote desktop software and documentation at help.realvnc.com.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# RealVNC documentation article URLs
# These are the key documentation pages from help.realvnc.com
REALVNC_DOC_ARTICLES = [
    # Getting Started
    "/hc/en-us/articles/360003474552-How-do-I-get-started-with-RealVNC-Connect-on-Windows",
    "/hc/en-us/articles/12374844842525-How-do-I-get-started-with-RealVNC-Connect-on-Android-and-iOS",

    # Configuration and Parameters
    "/hc/en-us/articles/360002253878-Configuring-RealVNC-Connect-Using-Parameters",
    "/hc/en-us/articles/360002251297-RealVNC-Server-Parameter-Reference",
    "/hc/en-us/articles/360002254618-RealVNC-Viewer-Parameter-Reference",

    # Authentication and Security
    "/hc/en-us/articles/360002250097-Setting-up-System-Authentication",
    "/hc/en-us/articles/360002253278-Setting-up-VNC-Connect-for-Maximum-Security",

    # Features
    "/hc/en-us/articles/360002250477-Transferring-Files-Between-Computers",
    "/hc/en-us/articles/4409166919441-How-do-I-use-the-Session-Recording-feature-in-RealVNC-Connect",
    "/hc/en-us/articles/360005031717-Organizing-RealVNC-Viewer-connections",

    # Deployment
    "/hc/en-us/articles/360002250657-Deploying-and-Licensing-RealVNC-Connect-using-Windows-MSIs",
    "/hc/en-us/articles/6450666419101-Deploying-RealVNC-Server-for-Mobile-using-Microsoft-Intune",
    "/hc/en-us/articles/18100694568733-Deploying-RealVNC-Connect-for-macOS-using-Jamf-Pro",

    # Accounts and Teams
    "/hc/en-us/articles/360002249697-Setting-up-and-Managing-your-RealVNC-Connect-Team",
    "/hc/en-us/articles/360002317777-Do-I-need-more-than-one-team",
    "/hc/en-us/articles/360002249677-Licensing-RealVNC-Connect",
    "/hc/en-us/articles/360029797672-Applying-an-offline-license-to-RealVNC-Connect",

    # Connectivity
    "/hc/en-us/articles/360024750892-What-are-cloud-connections-and-direct-connections",

    # Virtual Mode (Linux)
    "/hc/en-us/articles/360004324217-Beginner-s-guide-to-Virtual-Mode",

    # Raspberry Pi
    "/hc/en-us/articles/360002249917-RealVNC-Connect-and-Raspberry-Pi",

    # Mobile
    "/hc/en-us/articles/5518809415453-RealVNC-Server-for-Mobile-FAQs",

    # API
    "/hc/en-us/articles/6521249110685-API-Access-API-documentation-and-example-scripts",

    # Troubleshooting
    "/hc/en-us/articles/360002254738-RealVNC-Connect-Error-Messages",

    # Reference
    "/hc/en-us/articles/360002310477-vncviewer-man-page",
    "/hc/en-us/articles/360002313518-vncserver-x11-man-page",
    "/hc/en-us/articles/360002253138-Release-Notes-v7-7-13-1-and-earlier",
    "/hc/en-us/articles/360004160417-RealVNC-Product-Lifecycle-Policy",

    # On-Demand Assist
    "/hc/en-us/articles/25799837127325-Getting-Started-with-Helpdesk-On-Demand-Assist-in-v8",

    # Help Center Guide
    "/hc/en-us/articles/360002001838-Using-the-RealVNC-Help-Center",
]

BASE_URL = "https://help.realvnc.com"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main article content only."""
    # Extract the main article content from Zendesk help center
    # Zendesk uses <article> tag for main content
    article_match = re.search(
        r'<article[^>]*>(.*?)</article>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if article_match:
        html_content = article_match.group(1)
    else:
        # Try to find the main content div
        main_match = re.search(
            r'<div[^>]*class="[^"]*article-body[^"]*"[^>]*>(.*?)</div>',
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

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
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
    # Extract article ID and slug from Zendesk URLs like:
    # /hc/en-us/articles/360003474552-How-do-I-get-started-with-RealVNC-Connect-on-Windows

    # Remove /hc/en-us/articles/ prefix
    clean_path = path.replace('/hc/en-us/articles/', '')

    # Split on first hyphen to separate ID from slug
    parts = clean_path.split('-', 1)

    if len(parts) == 2:
        article_id, slug = parts
        # Use slug as filename (more readable than article ID)
        # Clean up the slug
        filename = slug.replace('-', '_') + '.md'
        return filename
    else:
        # Fallback: use the whole path
        return clean_path.replace('/', '-') + '.md'


def main():
    """Main function to download all RealVNC documentation."""
    print("=" * 60)
    print("RealVNC Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Articles to download: {len(REALVNC_DOC_ARTICLES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "realvnc"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, article_path in enumerate(REALVNC_DOC_ARTICLES, 1):
        url = BASE_URL + article_path
        filename = path_to_filename(article_path)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(REALVNC_DOC_ARTICLES)}] ", end="")

        if download_page(url, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(1)

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
        print(f"Warning: {failed} articles failed to download")
        sys.exit(1)
    else:
        print("All articles downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
