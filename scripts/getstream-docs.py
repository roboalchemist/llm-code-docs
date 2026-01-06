#!/usr/bin/env python3
"""
Stream.io (GetStream) Documentation Scraper

Stream.io provides activity feed, chat, and video APIs for building social features.
This scraper extracts documentation from their docs site and converts to markdown.

Source: https://getstream.io/chat/docs/
Output: docs/web-scraped/getstream/
"""

import os
import sys
import requests
from pathlib import Path
import time
from urllib.parse import urljoin, urlparse
import re
from bs4 import BeautifulSoup

# Base URL for Stream.io documentation
BASE_URL = "https://getstream.io/chat/docs/"
ACTIVITY_BASE = "https://getstream.io/activity-feeds/docs/"
MODERATION_BASE = "https://getstream.io/moderation/docs/"

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "getstream"

# Session for making requests
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

# Documentation pages to extract
DOCS_PAGES = [
    # Chat SDK Documentation
    ("https://getstream.io/chat/docs/", "index.md"),
    ("https://getstream.io/chat/docs/sdk/", "sdk-overview.md"),
    ("https://getstream.io/chat/docs/sdk/javascript/", "sdk-javascript.md"),
    ("https://getstream.io/chat/docs/sdk/react/", "sdk-react.md"),
    ("https://getstream.io/chat/docs/sdk/android/", "sdk-android.md"),
    ("https://getstream.io/chat/docs/sdk/ios/", "sdk-ios.md"),
    ("https://getstream.io/chat/docs/sdk/flutter/", "sdk-flutter.md"),
    ("https://getstream.io/chat/docs/sdk/react-native/", "sdk-react-native.md"),

    # Getting Started
    ("https://getstream.io/chat/docs/getting-started/", "getting-started.md"),
    ("https://getstream.io/chat/docs/setup-nodejs/", "setup-nodejs.md"),
    ("https://getstream.io/chat/docs/setup-python/", "setup-python.md"),
    ("https://getstream.io/chat/docs/setup-ruby/", "setup-ruby.md"),
    ("https://getstream.io/chat/docs/setup-go/", "setup-go.md"),
    ("https://getstream.io/chat/docs/setup-java/", "setup-java.md"),
    ("https://getstream.io/chat/docs/setup-dotnet/", "setup-dotnet.md"),
    ("https://getstream.io/chat/docs/setup-php/", "setup-php.md"),

    # Core Concepts
    ("https://getstream.io/chat/docs/channels/", "channels.md"),
    ("https://getstream.io/chat/docs/messages/", "messages.md"),
    ("https://getstream.io/chat/docs/users/", "users.md"),
    ("https://getstream.io/chat/docs/permissions/", "permissions.md"),
    ("https://getstream.io/chat/docs/moderation/", "moderation.md"),
    ("https://getstream.io/chat/docs/search/", "search.md"),
    ("https://getstream.io/chat/docs/file_uploads/", "file-uploads.md"),

    # React Specific
    ("https://getstream.io/chat/docs/sdk/react/guides/", "react-guides.md"),
    ("https://getstream.io/chat/docs/sdk/react/guides/ai-integrations/", "react-ai-integrations.md"),
    ("https://getstream.io/chat/docs/sdk/react/customization/", "react-customization.md"),

    # API Reference
    ("https://getstream.io/chat/docs/api_overview/", "api-overview.md"),
    ("https://getstream.io/chat/docs/users_overview/", "users-api.md"),
    ("https://getstream.io/chat/docs/channels_overview/", "channels-api.md"),
    ("https://getstream.io/chat/docs/messages_overview/", "messages-api.md"),

    # Moderation
    ("https://getstream.io/moderation/docs/", "moderation-overview.md"),
    ("https://getstream.io/moderation/docs/engines/", "moderation-engines.md"),
    ("https://getstream.io/moderation/docs/engines/ai-llm-text/", "moderation-ai-text.md"),

    # Activity Feeds
    ("https://getstream.io/activity-feeds/docs/", "activity-feeds-overview.md"),
]

def fetch_page(url):
    """Fetch a page and return its content."""
    try:
        print(f"  Fetching: {url}")
        response = session.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"  Error fetching {url}: {e}")
        return None

def extract_main_content(html, url):
    """Extract main content from HTML page."""
    if not html:
        return None

    soup = BeautifulSoup(html, 'html.parser')

    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Try to find main content areas
    main_content = None

    # Look for common content containers
    for selector in [
        'main',
        'article',
        '[role="main"]',
        '.markdown-body',
        '.content',
        '.page-content',
        '.docs-content',
    ]:
        main_content = soup.select_one(selector)
        if main_content:
            break

    # If no main content found, use body
    if not main_content:
        main_content = soup.find('body')

    if not main_content:
        return None

    # Convert to markdown
    try:
        # Try markdownify first
        from markdownify import markdownify
        markdown_content = markdownify(str(main_content))
    except (ImportError, NameError):
        # Fall back to html2text
        from html2text import html2text
        markdown_content = html2text(str(main_content))

    # Clean up the markdown
    lines = markdown_content.split('\n')
    cleaned_lines = []

    for line in lines:
        # Skip empty lines at the start
        if not cleaned_lines and not line.strip():
            continue
        # Skip lines with only special characters (navigation elements)
        if line.strip() and all(c in '|-*#' for c in line.strip() if c != ' '):
            continue
        cleaned_lines.append(line)

    markdown_content = '\n'.join(cleaned_lines).strip()

    return markdown_content

def sanitize_markdown(content):
    """Sanitize markdown content for better readability."""
    if not content:
        return content

    # Remove excessive blank lines
    content = re.sub(r'\n\n\n+', '\n\n', content)

    # Remove markdown links without text
    content = re.sub(r'\[\]\([^)]+\)', '', content)

    # Remove inline javascript
    content = re.sub(r'javascript:[^\s)]+', '', content)

    return content

def add_source_header(content, url):
    """Add source information to the beginning of the content."""
    header = f"""# Stream.io Documentation
# Source: {url}

"""
    return header + content

def download_docs():
    """Download Stream.io documentation."""

    print(f"\nDownloading Stream.io documentation...")
    print(f"Output directory: {OUTPUT_DIR}")

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    successful = 0
    failed = 0

    for url, filename in DOCS_PAGES:
        filepath = OUTPUT_DIR / filename

        # Skip if file already exists
        if filepath.exists():
            print(f"  Skipping {filename} (already exists)")
            continue

        html = fetch_page(url)
        if not html:
            print(f"  Failed to fetch {filename}")
            failed += 1
            continue

        content = extract_main_content(html, url)
        if not content:
            print(f"  No content extracted from {filename}")
            failed += 1
            continue

        # Add source header
        content = add_source_header(content, url)

        # Sanitize content
        content = sanitize_markdown(content)

        # Write to file
        try:
            filepath.write_text(content, encoding='utf-8')
            file_size = filepath.stat().st_size / 1024
            print(f"  Saved {filename} ({file_size:.1f} KB)")
            successful += 1
        except Exception as e:
            print(f"  Error writing {filename}: {e}")
            failed += 1

        # Rate limiting to be respectful to the server
        time.sleep(1)

    # Summary
    print(f"\nDownload complete!")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Total files: {len(list(OUTPUT_DIR.glob('*.md')))}")

    total_size = sum(f.stat().st_size for f in OUTPUT_DIR.glob('*.md'))
    print(f"  Total size: {total_size / 1024 / 1024:.2f} MB")

    return successful > 0

if __name__ == "__main__":
    try:
        success = download_docs()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\nDownload interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
