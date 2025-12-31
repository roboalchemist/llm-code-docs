#!/usr/bin/env python3
"""
hapi Documentation Scraper
Downloads hapi framework documentation from hapi.dev and converts to markdown.
hapi is a simple, secure Node.js web framework.
"""

import os
import sys
import requests
from pathlib import Path
import time
from bs4 import BeautifulSoup
import html2text

# Base URL for hapi.dev
BASE_URL = "https://hapi.dev"

# Tutorial pages to scrape
TUTORIALS = [
    "gettingstarted",
    "expresstohapi",
    "auth",
    "caching",
    "cookies",
    "logging",
    "plugins",
    "routing",
    "servermethods",
    "servingfiles",
    "testing",
    "validation",
    "views",
]

# API versions to include (we'll focus on latest)
API_VERSIONS = [""]  # Empty string for latest


def fetch_page(url):
    """Fetch a page and return BeautifulSoup object."""
    try:
        print(f"  Fetching: {url}")
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"    -> Error fetching {url}: {e}")
        return None


def convert_html_to_markdown(html_content, url):
    """Convert HTML content to markdown."""
    # Initialize html2text converter
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # Don't wrap lines
    h.unicode_snob = True
    h.skip_internal_links = False

    # Convert to markdown
    markdown = h.handle(str(html_content))

    # Add metadata header
    header = f"""# hapi Documentation
# Source: {url}

"""
    return header + markdown


def scrape_tutorial(tutorial_name, output_dir):
    """Scrape a tutorial page."""
    url = f"{BASE_URL}/tutorials/{tutorial_name}/?lang=en_US"

    soup = fetch_page(url)
    if not soup:
        return False

    # Find main content
    # hapi.dev uses a main content area - we'll try to find it
    main_content = soup.find('main') or soup.find('article') or soup.find(class_='content')

    if not main_content:
        # If we can't find specific content, try to find the body
        # but remove nav, header, footer
        for tag in soup(['nav', 'header', 'footer', 'script', 'style']):
            tag.decompose()
        main_content = soup.find('body')

    if not main_content:
        print(f"    -> Could not find main content")
        return False

    # Convert to markdown
    markdown = convert_html_to_markdown(main_content, url)

    # Save to file
    output_file = output_dir / f"tutorial-{tutorial_name}.md"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown)

    print(f"    -> Saved: {output_file}")
    return True


def scrape_api_reference(output_dir):
    """Scrape the API reference page."""
    url = f"{BASE_URL}/api/"

    soup = fetch_page(url)
    if not soup:
        return False

    # Find main content
    main_content = soup.find('main') or soup.find('article') or soup.find(class_='content')

    if not main_content:
        # If we can't find specific content, try to find the body
        # but remove nav, header, footer
        for tag in soup(['nav', 'header', 'footer', 'script', 'style']):
            tag.decompose()
        main_content = soup.find('body')

    if not main_content:
        print(f"    -> Could not find main content")
        return False

    # Convert to markdown
    markdown = convert_html_to_markdown(main_content, url)

    # Save to file
    output_file = output_dir / "api-reference.md"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown)

    print(f"    -> Saved: {output_file}")
    return True


def scrape_plugins_list(output_dir):
    """Scrape the plugins list page."""
    url = f"{BASE_URL}/plugins/"

    soup = fetch_page(url)
    if not soup:
        return False

    # Find main content
    main_content = soup.find('main') or soup.find('article') or soup.find(class_='content')

    if not main_content:
        # If we can't find specific content, try to find the body
        # but remove nav, header, footer
        for tag in soup(['nav', 'header', 'footer', 'script', 'style']):
            tag.decompose()
        main_content = soup.find('body')

    if not main_content:
        print(f"    -> Could not find main content")
        return False

    # Convert to markdown
    markdown = convert_html_to_markdown(main_content, url)

    # Save to file
    output_file = output_dir / "plugins-list.md"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown)

    print(f"    -> Saved: {output_file}")
    return True


def scrape_family_page(output_dir):
    """Scrape the family page (official modules)."""
    url = f"{BASE_URL}/family/"

    soup = fetch_page(url)
    if not soup:
        return False

    # Find main content
    main_content = soup.find('main') or soup.find('article') or soup.find(class_='content')

    if not main_content:
        # If we can't find specific content, try to find the body
        # but remove nav, header, footer
        for tag in soup(['nav', 'header', 'footer', 'script', 'style']):
            tag.decompose()
        main_content = soup.find('body')

    if not main_content:
        print(f"    -> Could not find main content")
        return False

    # Convert to markdown
    markdown = convert_html_to_markdown(main_content, url)

    # Save to file
    output_file = output_dir / "family-modules.md"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown)

    print(f"    -> Saved: {output_file}")
    return True


def main():
    """Main function to download all hapi documentation."""
    print("=" * 60)
    print("hapi Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "hapi"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    # Scrape API reference
    print(f"[1/17] API Reference")
    if scrape_api_reference(output_dir):
        successful += 1
    else:
        failed += 1
    time.sleep(1)

    # Scrape plugins list
    print(f"[2/17] Plugins List")
    if scrape_plugins_list(output_dir):
        successful += 1
    else:
        failed += 1
    time.sleep(1)

    # Scrape family page
    print(f"[3/17] Family Modules")
    if scrape_family_page(output_dir):
        successful += 1
    else:
        failed += 1
    time.sleep(1)

    # Scrape tutorials
    for idx, tutorial in enumerate(TUTORIALS, 4):
        print(f"[{idx}/17] Tutorial: {tutorial}")
        if scrape_tutorial(tutorial, output_dir):
            successful += 1
        else:
            failed += 1
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
    total_size = sum(f.stat().st_size for f in output_dir.glob("*") if f.is_file())
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if successful == 0:
        print("Error: No files downloaded successfully!")
        sys.exit(1)
    elif failed > successful:
        print(f"Warning: More failures ({failed}) than successes ({successful})")
        sys.exit(1)
    else:
        print(f"Documentation downloaded successfully! ({successful} files)")
        sys.exit(0)


if __name__ == "__main__":
    main()
