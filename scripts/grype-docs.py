#!/usr/bin/env python3
"""
Grype Documentation Scraper

Downloads and converts Grype vulnerability scanner documentation from oss.anchore.com.
Grype is made by Anchore and scans container images and filesystems for CVEs.

Source: https://oss.anchore.com/docs/
Output: docs/web-scraped/grype/
"""

import os
import sys
import requests
import json
from pathlib import Path
from urllib.parse import urljoin, urlparse
import re
from html.parser import HTMLParser
import time

# Base configuration
BASE_URL = "https://oss.anchore.com"
DOCS_BASE = f"{BASE_URL}/docs"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "grype"

# Rate limiting
REQUEST_DELAY = 0.3  # seconds between requests
REQUEST_TIMEOUT = 15  # seconds

# Documentation sections to scrape (these are the main sections)
DOC_SECTIONS = {
    "installation": "/docs/installation/grype/",
    "getting-started": "/docs/guides/vulnerability/getting-started/",
    "scan-targets": "/docs/guides/vulnerability/scan-targets/",
    "ecosystems": "/docs/guides/vulnerability/ecosystems/",
    "interpreting-results": "/docs/guides/vulnerability/interpreting-results/",
    "json": "/docs/guides/vulnerability/json/",
    "filter-results": "/docs/guides/vulnerability/filter-results/",
    "database": "/docs/guides/vulnerability/database/",
    "cli": "/docs/reference/grype/cli/",
    "configuration": "/docs/reference/grype/configuration/",
}

# Try to fetch from API to find linked pages
API_ENDPOINT = "https://api.github.com/repos/anchore/grype/contents"


class MarkdownConverter:
    """Simple HTML to Markdown converter for documentation."""

    def __init__(self):
        self.text = []
        self.in_code = False
        self.in_pre = False

    def handle_data(self, data):
        """Handle text data."""
        if data.strip():
            self.text.append(data)

    def convert(self, html_content):
        """Convert HTML to basic markdown."""
        # Remove script and style tags
        html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL)

        # Convert headers
        html_content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n', html_content, flags=re.DOTALL)

        # Convert code blocks
        html_content = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```\n', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL)

        # Convert lists
        html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.DOTALL)

        # Convert links
        html_content = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL)

        # Convert bold and italic
        html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.DOTALL)

        # Remove remaining HTML tags
        html_content = re.sub(r'<[^>]+>', '', html_content)

        # Clean up multiple blank lines
        html_content = re.sub(r'\n\n\n+', '\n\n', html_content)

        return html_content.strip()


def fetch_page_content(url):
    """Fetch HTML content from a URL and convert to markdown."""
    try:
        print(f"  Fetching: {url}")

        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        # Convert HTML to markdown
        converter = MarkdownConverter()
        content = converter.convert(response.text)

        if content:
            print(f"    -> Success ({len(content)} bytes)")
            return content
        else:
            print(f"    -> Warning: Empty content")
            return None

    except requests.exceptions.RequestException as e:
        print(f"    -> Error: {e}")
        return None
    except Exception as e:
        print(f"    -> Error processing: {e}")
        return None


def sanitize_filename(path):
    """Convert URL path to safe filename."""
    # Remove leading/trailing slashes
    path = path.strip('/')

    # Replace slashes with dashes for the filename
    safe = path.replace('/', '-')

    # Remove any remaining special characters
    safe = re.sub(r'[^a-zA-Z0-9\-_]', '', safe)

    return safe or "index"


def save_markdown_file(content, filename, url):
    """Save markdown content to file with metadata header."""
    try:
        # Create output directory
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Add source header
        header = f"""# Source: {url}

"""
        full_content = header + content

        # Ensure filename ends with .md
        if not filename.endswith('.md'):
            filename = filename + '.md'

        output_path = OUTPUT_DIR / filename

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"    -> Saved: {filename} ({len(full_content)} bytes)")
        return True

    except Exception as e:
        print(f"    -> Error saving file: {e}")
        return False


def scrape_documentation():
    """Scrape all grype documentation from oss.anchore.com."""
    try:
        print("Grype Documentation Scraper")
        print("=" * 60)
        print(f"Base URL: {DOCS_BASE}")
        print(f"Output: {OUTPUT_DIR}")
        print()

        # Clear output directory
        if OUTPUT_DIR.exists():
            import shutil
            print(f"Clearing existing output directory...")
            shutil.rmtree(OUTPUT_DIR)

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        files_saved = 0
        total_size = 0

        # Scrape each documentation section
        print(f"Scraping {len(DOC_SECTIONS)} documentation sections:")
        print()

        for section_name, section_path in DOC_SECTIONS.items():
            full_url = urljoin(BASE_URL, section_path)

            print(f"Section: {section_name}")
            content = fetch_page_content(full_url)

            if content:
                filename = sanitize_filename(section_path)
                if save_markdown_file(content, filename, full_url):
                    files_saved += 1
                    total_size += len(content)

            # Rate limiting
            time.sleep(REQUEST_DELAY)

        print()
        print("=" * 60)
        print(f"Scraping complete!")
        print(f"Files saved: {files_saved}")
        print(f"Total size: {total_size / 1024:.2f} KB")
        print(f"Location: {OUTPUT_DIR}")

        return True if files_saved > 0 else False

    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    """Main entry point."""
    try:
        success = scrape_documentation()
        return 0 if success else 1
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        return 1
    except Exception as e:
        print(f"Fatal error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
