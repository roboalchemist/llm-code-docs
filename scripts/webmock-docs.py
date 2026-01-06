#!/usr/bin/env python3
"""
WebMock Documentation Scraper
Downloads WebMock Ruby gem documentation from GitHub and official docs site.
WebMock is a Ruby library for stubbing and setting expectations on HTTP requests.
"""

import os
import sys
import requests
from pathlib import Path
import time
from urllib.parse import urljoin, urlparse
import re

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "webmock"

# Documentation sources
GITHUB_README = "https://raw.githubusercontent.com/bblimke/webmock/master/README.md"
GITHUB_CHANGELOG = "https://raw.githubusercontent.com/bblimke/webmock/master/CHANGELOG.md"
GITHUB_LICENSE = "https://raw.githubusercontent.com/bblimke/webmock/master/LICENSE"

# Additional documentation from webmock.github.io (old docs)
DOCS_SITE_PAGES = [
    "http://webmock.github.io/docs/",  # Main docs
]

REQUEST_DELAY = 0.5  # seconds between requests
REQUEST_TIMEOUT = 10


def ensure_output_dir():
    """Create output directory if it doesn't exist."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")


def fetch_url(url, timeout=REQUEST_TIMEOUT):
    """Fetch content from URL with error handling."""
    try:
        print(f"  Fetching: {url}")
        response = requests.get(url, timeout=timeout, allow_redirects=True)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"    Error: {e}")
        return None


def sanitize_filename(filename):
    """Convert filename to safe format."""
    filename = re.sub(r'[^a-z0-9._-]', '-', filename.lower())
    filename = re.sub(r'-+', '-', filename)
    return filename.strip('-')


def html_to_markdown_simple(html_content):
    """
    Simple HTML to Markdown converter for YARD documentation.
    Handles basic HTML tags and preserves code blocks.
    """
    # Remove script and style tags
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Remove HTML comments
    html_content = re.sub(r'<!--.*?-->', '', html_content, flags=re.DOTALL)

    # Convert pre/code blocks
    html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Convert headings
    html_content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<h5[^>]*>(.*?)</h5>', r'##### \1\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<h6[^>]*>(.*?)</h6>', r'###### \1\n', html_content, flags=re.IGNORECASE)

    # Convert bold and italic
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.IGNORECASE)

    # Convert links
    html_content = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.IGNORECASE)

    # Convert lists
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<ul[^>]*>(.*?)</ul>', r'\1', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<ol[^>]*>(.*?)</ol>', r'\1', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Convert paragraphs
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', html_content, flags=re.IGNORECASE)

    # Convert line breaks
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<hr\s*/?>', '\n---\n', html_content, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Decode HTML entities
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&quot;', '"')
    html_content = html_content.replace('&apos;', "'")

    # Clean up whitespace
    lines = html_content.split('\n')
    lines = [line.rstrip() for line in lines]
    html_content = '\n'.join(lines)

    # Remove excessive blank lines
    html_content = re.sub(r'\n\n\n+', '\n\n', html_content)

    return html_content.strip()


def save_markdown(filename, content):
    """Save content as markdown file with source header."""
    output_file = OUTPUT_DIR / filename

    # Ensure content is markdown
    if not filename.endswith('.md'):
        filename = filename + '.md'
        output_file = OUTPUT_DIR / filename

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Saved: {output_file}")
    return output_file


def scrape_github_files():
    """Scrape README and CHANGELOG from GitHub."""
    print("\nScraping GitHub files...")

    files_to_fetch = [
        (GITHUB_README, "README.md"),
        (GITHUB_CHANGELOG, "CHANGELOG.md"),
        (GITHUB_LICENSE, "LICENSE.md"),
    ]

    for url, filename in files_to_fetch:
        content = fetch_url(url)
        if content:
            # Add source header
            content = f"# Source: {url}\n\n{content}"
            save_markdown(filename, content)
            time.sleep(REQUEST_DELAY)
        else:
            print(f"  Skipped: {filename}")


def scrape_docs_site():
    """Scrape documentation from webmock.github.io."""
    print("\nScraping webmock.github.io documentation site...")

    for page_url in DOCS_SITE_PAGES:
        html_content = fetch_url(page_url)
        if not html_content:
            continue

        # Extract main content (look for common content selectors)
        # Try to find main content areas
        content_match = re.search(
            r'<(?:main|article|div[^>]*(?:class="[^"]*(?:content|main|body)[^"]*")[^>]*)>(.*?)</(?:main|article|div)>',
            html_content,
            re.DOTALL | re.IGNORECASE
        )

        if content_match:
            content = content_match.group(1)
        else:
            # Fallback: take everything in body
            body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL | re.IGNORECASE)
            content = body_match.group(1) if body_match else html_content

        # Convert HTML to Markdown
        markdown = html_to_markdown_simple(content)

        # Create filename from URL
        parsed = urlparse(page_url)
        path = parsed.path.strip('/').split('/')[-1] or 'index'
        filename = sanitize_filename(path) + '.md'

        # Add source header
        markdown = f"# Source: {page_url}\n\n{markdown}"

        save_markdown(filename, markdown)
        time.sleep(REQUEST_DELAY)


def create_index():
    """Create index.md file listing all documentation."""
    print("\nCreating index file...")

    index_content = """# WebMock Ruby Gem Documentation

WebMock is a Ruby library for stubbing and setting expectations on HTTP requests.

It allows you to:
- Stub HTTP requests at the HTTP client library level
- Set expectations on HTTP requests
- Match requests based on method, URI, headers, and body
- Perform smart matching of URIs in different representations
- Work with popular testing frameworks (RSpec, Test::Unit, MiniTest)

## Features

- Low-level HTTP request stubbing (no need to change tests when switching HTTP libraries)
- Request expectation setting and verification
- Flexible request matching (method, URI, headers, body)
- Smart URI matching (handles encoding variations)
- Smart header matching
- Support for multiple testing frameworks and HTTP libraries

## Supported HTTP Libraries

- Async::HTTP::Client
- Curb
- EM-HTTP-Request
- Excon
- HTTPClient
- HTTP Gem (http.rb)
- httpx
- Manticore
- Net::HTTP and derivatives (HTTParty, REST Client)
- Patron
- Typhoeus

## Documentation Files

- **README.md** - Main documentation and installation guide
- **CHANGELOG.md** - Version history and changes
- **LICENSE.md** - License information
- **index.md** - Archived documentation from webmock.github.io

## Installation

```bash
gem install webmock
```

Or add to your Gemfile:

```ruby
group :test do
  gem "webmock"
end
```

## Key Resources

- GitHub Repository: https://github.com/bblimke/webmock
- RubyGems: https://rubygems.org/gems/webmock
- RubyDoc: https://www.rubydoc.info/gems/webmock
"""

    save_markdown("00-index.md", index_content)


def main():
    """Main scraper entry point."""
    print("WebMock Documentation Scraper")
    print("=" * 50)

    ensure_output_dir()

    # Scrape sources
    scrape_github_files()
    scrape_docs_site()

    # Create index
    create_index()

    # List generated files
    print("\n" + "=" * 50)
    print(f"Documentation saved to: {OUTPUT_DIR}")

    files = list(OUTPUT_DIR.glob("*.md"))
    print(f"Total files generated: {len(files)}")
    for f in sorted(files):
        size = f.stat().st_size
        print(f"  - {f.name} ({size:,} bytes)")

    total_size = sum(f.stat().st_size for f in files)
    print(f"\nTotal size: {total_size:,} bytes")


if __name__ == "__main__":
    main()
