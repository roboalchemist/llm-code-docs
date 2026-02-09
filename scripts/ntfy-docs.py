#!/usr/bin/env python3
"""
Scraper for ntfy documentation.
Output: docs/web-scraped/ntfy/

ntfy is a simple HTTP-based pub-sub notification service.
Fetches markdown documentation from the GitHub repository.
Source: https://github.com/binwiederhier/ntfy
"""

import requests
from pathlib import Path
import sys
from urllib.parse import urljoin

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "ntfy"

# Raw GitHub URLs for documentation pages
DOCS_BASE_URL = "https://raw.githubusercontent.com/binwiederhier/ntfy/main/docs"

# Documentation pages from MkDocs navigation
DOC_PAGES = [
    ("index.md", "Home"),
    ("publish.md", "Publishing"),
    ("subscribe/index.md", "Subscribing"),
    ("subscribe/phone.md", "Phone"),
    ("subscribe/web.md", "Web App"),
    ("subscribe/api.md", "API"),
    ("subscribe/cli.md", "Command Line"),
    ("subscribe/desktop.md", "Desktop/PWA"),
    ("install.md", "Self-hosting"),
    ("config.md", "Configuration"),
    ("auth.md", "Authentication"),
    ("encryption.md", "Encryption"),
    ("integrations.md", "Integrations"),
    ("examples.md", "Examples"),
    ("faq.md", "FAQ"),
    ("troubleshooting.md", "Troubleshooting"),
    ("develop.md", "Development"),
    ("releases.md", "Releases"),
]


def fetch_markdown_file(relative_path, description):
    """Fetch a single markdown file from GitHub raw content."""
    try:
        url = f"{DOCS_BASE_URL}/{relative_path}"
        print(f"  Fetching: {description} ({relative_path})")

        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            print(f"    -> Not found (404)")
            return None

        response.raise_for_status()

        content = response.text

        if not content or len(content.strip()) < 100:
            print(f"    -> Content too small or empty")
            return None

        print(f"    -> Success ({len(content)} bytes)")
        return content

    except requests.exceptions.RequestException as e:
        print(f"    -> Error: {e}")
        return None


def add_source_header(content, page_path):
    """Add a source header to the content."""
    source_url = f"https://github.com/binwiederhier/ntfy/blob/main/docs/{page_path}"
    header = f"# Source: {source_url}\n\n"
    return header + content


def main():
    """Main scraper function."""
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("ntfy Documentation Scraper")
    print("=" * 70)
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    print("Fetching documentation pages...")
    print()

    success_count = 0
    fail_count = 0

    for page_path, description in DOC_PAGES:
        content = fetch_markdown_file(page_path, description)

        if content:
            # Add source header
            content_with_source = add_source_header(content, page_path)

            # Determine output filename
            if page_path.endswith('/index.md'):
                # For subscribe/index.md -> subscribe.md
                output_filename = page_path.replace('/index.md', '.md')
            else:
                output_filename = page_path

            output_path = OUTPUT_DIR / output_filename
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(content_with_source, encoding='utf-8')
            success_count += 1
        else:
            fail_count += 1

    print()
    print("=" * 70)
    print("Extraction Complete")
    print("=" * 70)

    # Verify extraction
    markdown_files = list(OUTPUT_DIR.glob("**/*.md"))
    total_size = sum(f.stat().st_size for f in markdown_files)

    print(f"Successfully fetched: {success_count} pages")
    print(f"Failed to fetch: {fail_count} pages")
    print(f"Total markdown files: {len(markdown_files)}")
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    if len(markdown_files) > 0:
        print()
        print("Files created:")
        for md_file in sorted(markdown_files)[:15]:
            file_size = md_file.stat().st_size
            print(f"  - {md_file.relative_to(OUTPUT_DIR)} ({file_size:,} bytes)")

        if len(markdown_files) > 15:
            print(f"  ... and {len(markdown_files) - 15} more files")

    print()
    print(f"Output: {OUTPUT_DIR}")
    print()

    if success_count == 0:
        print("Error: No documentation files were fetched successfully")
        sys.exit(1)


if __name__ == "__main__":
    main()
