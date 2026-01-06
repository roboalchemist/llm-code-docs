#!/usr/bin/env python3
"""
AionUi Wiki Scraper
Scrapes documentation from the AionUi GitHub wiki pages.
Extracts all wiki pages to markdown files.
"""

import os
import sys
from pathlib import Path
import subprocess
from html.parser import HTMLParser
import urllib.request
import urllib.error
import json

# Wiki pages to scrape
WIKI_PAGES = [
    ("Home", "Home"),
    ("Getting-Started", "Getting-Started"),
    ("Configuration-Guides", "Configuration-Guides"),
    ("LLM-Configuration", "LLM-Configuration"),
    ("AionUi-Image-Generation-Tool-Model-Configuration-Guide", "Image-Generation-Configuration"),
    ("ACP-Setup", "ACP-Setup"),
    ("MCP-Configuration-Guide", "MCP-Configuration-Guide"),
    ("WebUI-Configuration-Guide", "WebUI-Configuration-Guide"),
    ("FAQ", "FAQ"),
    ("Use-Cases-Overview", "Use-Cases-Overview"),
]

REPO_OWNER = "iOfficeAI"
REPO_NAME = "AionUi"


def scrape_wiki_page(page_name):
    """Scrape a single wiki page from GitHub."""
    try:
        # Try using git clone for the wiki
        url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}.wiki.git"

        # Use raw GitHub content for wiki
        raw_url = f"https://raw.githubusercontent.com/wiki/{REPO_OWNER}/{REPO_NAME}/{page_name}.md"

        print(f"  Fetching: {page_name}...", end=" ", flush=True)

        try:
            with urllib.request.urlopen(raw_url, timeout=10) as response:
                content = response.read().decode('utf-8')
                print("✓")
                return content
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print("✗ (not found)")
                return None
            raise
        except Exception as e:
            print(f"✗ ({str(e)})")
            return None

    except Exception as e:
        print(f"  Error fetching {page_name}: {e}")
        return None


def main():
    """Main function to scrape AionUi wiki."""
    print("=" * 70)
    print("AionUi Wiki Scraper")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "aionui" / "wiki"

    print(f"Repository: {REPO_OWNER}/{REPO_NAME}")
    print(f"Output directory: {output_dir}")
    print()

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Scraping wiki pages...")
    scraped_count = 0
    failed_count = 0

    for page_name, file_name in WIKI_PAGES:
        content = scrape_wiki_page(page_name)

        if content:
            # Add source header
            source_url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/wiki/{page_name}"
            header = f"""# Source: {source_url}

"""
            final_content = header + content

            # Write to file
            output_file = output_dir / f"{file_name}.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(final_content)

            scraped_count += 1
        else:
            failed_count += 1

    print()
    print("=" * 70)
    print("Wiki Scraping Complete")
    print("=" * 70)
    print(f"Successfully scraped: {scraped_count} pages")
    print(f"Failed: {failed_count} pages")
    print(f"Output directory: {output_dir}")
    print()

    # List scraped files
    if output_dir.exists():
        files = list(output_dir.glob("*.md"))
        print(f"Files created: {len(files)}")
        for f in sorted(files):
            size = f.stat().st_size
            print(f"  - {f.name} ({size:,} bytes)")


if __name__ == "__main__":
    main()
