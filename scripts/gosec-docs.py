#!/usr/bin/env python3
"""
Gosec Documentation Scraper
Downloads gosec documentation from securego.io.
gosec is a Go source code security scanner that detects SQL injection,
weak cryptography, hardcoded credentials, and other security vulnerabilities.
"""

import os
import sys
import requests
from pathlib import Path
import time
import re
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

# Base URL for documentation
BASE_URL = "https://securego.io"

# Documentation pages to scrape
PAGES_TO_SCRAPE = [
    ("/docs/rules/rule-intro", "rules-overview.md"),
    ("/docs/rules/rules", "rules-list.md"),
    ("/docs/tools", "tools.md"),
    ("/help", "help.md"),
    ("/", "README.md"),
]

# Rate limiting
REQUEST_DELAY = 0.5  # seconds between requests


class HTMLToMarkdownParser(HTMLParser):
    """Simple HTML to Markdown converter for documentation pages."""

    def __init__(self):
        super().__init__()
        self.text = []
        self.in_script = False
        self.in_style = False
        self.in_nav = False
        self.in_footer = False
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            self.in_script = True
        elif tag == "style":
            self.in_style = True
        elif tag in ("nav", "header"):
            self.in_nav = True
        elif tag == "footer":
            self.in_footer = True
        elif not (self.in_script or self.in_style or self.in_nav or self.in_footer):
            if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
                level = int(tag[1])
                self.text.append("\n" + "#" * level + " ")
            elif tag == "p":
                self.text.append("\n")
            elif tag == "br":
                self.text.append("\n")
            elif tag in ("li", "tr", "td", "th"):
                self.text.append("\n")
            elif tag == "strong" or tag == "b":
                self.text.append("**")
            elif tag == "em" or tag == "i":
                self.text.append("*")
            elif tag == "code":
                self.text.append("`")
            elif tag == "pre":
                self.text.append("\n```\n")
            elif tag == "a":
                self.text.append("[")
                for attr, value in attrs:
                    if attr == "href":
                        self.current_tag = ("a", value)
            elif tag == "ul":
                self.text.append("\n")
            elif tag == "ol":
                self.text.append("\n")
        self.current_tag = tag

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_script = False
        elif tag == "style":
            self.in_style = False
        elif tag in ("nav", "header"):
            self.in_nav = False
        elif tag == "footer":
            self.in_footer = False
        elif not (self.in_script or self.in_style or self.in_nav or self.in_footer):
            if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
                self.text.append("\n")
            elif tag == "p":
                self.text.append("\n")
            elif tag in ("strong", "b"):
                self.text.append("**")
            elif tag in ("em", "i"):
                self.text.append("*")
            elif tag == "code":
                self.text.append("`")
            elif tag == "pre":
                self.text.append("\n```\n")
            elif tag == "a":
                if self.current_tag and self.current_tag[0] == "a":
                    self.text.append(f"]({self.current_tag[1]})")
                self.current_tag = None

    def handle_data(self, data):
        if not (self.in_script or self.in_style or self.in_nav or self.in_footer):
            # Clean up whitespace
            text = data.strip()
            if text:
                self.text.append(text + " ")


def extract_markdown_from_html(html_content):
    """Convert HTML to basic Markdown."""
    parser = HTMLToMarkdownParser()
    try:
        parser.feed(html_content)
        text = ''.join(parser.text)

        # Clean up extra whitespace
        text = re.sub(r'\n\s*\n+', '\n\n', text)
        text = re.sub(r' +', ' ', text)
        text = text.strip()

        return text
    except Exception as e:
        print(f"    -> Error parsing HTML: {e}")
        return None


def download_page(url_path, output_filename, output_dir):
    """Download a single page from securego.io and convert to Markdown."""
    try:
        full_url = urljoin(BASE_URL, url_path)

        print(f"  Downloading: {url_path}")

        response = requests.get(full_url, timeout=15)
        response.raise_for_status()

        # Extract main content - try to find article or main tag
        html = response.text

        # Simple extraction of main content
        markdown = extract_markdown_from_html(html)

        if not markdown or len(markdown) < 100:
            print(f"    -> Warning: Page might be empty or too small ({len(markdown or '')} bytes)")

        # Add metadata header
        header = f"""# Source: {full_url}

"""
        final_content = header + (markdown or "")

        # Create output file
        output_path = output_dir / output_filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

        print(f"    -> Saved: {output_filename} ({len(final_content)} bytes)")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {url_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {url_path}: {e}")
        return False


def download_github_readme(output_dir):
    """Download README from GitHub repository."""
    try:
        print(f"  Downloading: GitHub README")

        raw_url = "https://raw.githubusercontent.com/securego/gosec/master/README.md"
        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# Source: {raw_url}

"""
        final_content = header + content

        output_path = output_dir / "github-README.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

        print(f"    -> Saved: github-README.md ({len(final_content)} bytes)")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading README: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing README: {e}")
        return False


def main():
    """Main function to download gosec documentation."""
    print("=" * 60)
    print("Gosec Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "gosec"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    start_time = time.time()
    successful = 0
    failed = 0

    # Download each page
    print(f"Downloading {len(PAGES_TO_SCRAPE)} documentation pages from {BASE_URL}...")
    print()

    for url_path, output_filename in PAGES_TO_SCRAPE:
        if download_page(url_path, output_filename, output_dir):
            successful += 1
        else:
            failed += 1
        time.sleep(REQUEST_DELAY)

    # Download README from GitHub
    print()
    if download_github_readme(output_dir):
        successful += 1
    else:
        failed += 1

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
    total_size = sum(f.stat().st_size for f in output_dir.rglob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} files failed to download")
        return False
    else:
        print("All documentation downloaded successfully!")
        return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
