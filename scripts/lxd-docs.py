#!/usr/bin/env python3
"""
LXD Documentation Scraper
Downloads all LXD documentation pages from documentation.ubuntu.com and converts to markdown.
LXD is a modern, secure and powerful system container and virtual machine manager.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urljoin, urlparse
import time
import re
import subprocess
from bs4 import BeautifulSoup

# LXD documentation base URL
BASE_URL = "https://documentation.ubuntu.com/lxd/en/latest/"

# Key documentation sections based on Sphinx structure
# These are the main navigation items
LXD_DOC_SECTIONS = [
    "",  # Main index
    "tutorial/first_steps/",
    "tutorial/instances/",
    "tutorial/projects/",
    "tutorial/storage/",
    "tutorial/networks/",
    "tutorial/security/",
    "howto/",
    "howto/instances_create/",
    "howto/instances_configure/",
    "howto/instances_manage/",
    "howto/instances_snapshots/",
    "howto/instances_backup/",
    "howto/instances_access_files/",
    "howto/instances_console/",
    "howto/instances_troubleshoot/",
    "howto/images_manage/",
    "howto/images_remote/",
    "howto/storage_pools/",
    "howto/storage_volumes/",
    "howto/storage_buckets/",
    "howto/network_create/",
    "howto/network_configure/",
    "howto/network_acls/",
    "howto/network_forwards/",
    "howto/network_zones/",
    "howto/network_load_balancers/",
    "howto/network_ovn_setup/",
    "howto/projects_work/",
    "howto/projects_confine/",
    "howto/cluster_form/",
    "howto/cluster_manage/",
    "howto/cluster_config_storage/",
    "howto/cluster_config_networks/",
    "howto/cluster_groups/",
    "howto/server_expose/",
    "howto/server_configure/",
    "howto/troubleshoot/",
    "explanation/",
    "explanation/instances/",
    "explanation/containers_and_vms/",
    "explanation/instance_config/",
    "explanation/image_handling/",
    "explanation/storage/",
    "explanation/networks/",
    "explanation/projects/",
    "explanation/clustering/",
    "explanation/security/",
    "reference/",
    "reference/devices/",
    "reference/network/",
    "reference/storage/",
    "reference/projects/",
    "reference/instance_options/",
    "reference/instance_units/",
    "reference/storage_drivers/",
    "reference/network_drivers/",
    "reference/manpages/",
    "reference/api/",
    "reference/provided_metrics/",
    "reference/requirements/",
    "reference/performance_tuning/",
]


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # Try pandoc first for best quality
    try:
        # Extract just the main article content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Sphinx uses <article role="main">
        article = soup.find('article', role='main')
        if not article:
            # Try alternate selectors
            article = soup.find('div', class_='document')

        if article:
            html_content = str(article)

        # Use pandoc for conversion
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

    # Fallback: basic HTML to text extraction using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove unwanted elements
    for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
        element.decompose()

    # Try to find main content
    main_content = soup.find('article', role='main')
    if not main_content:
        main_content = soup.find('div', class_='document')
    if not main_content:
        main_content = soup.find('main')

    if main_content:
        soup = main_content

    # Convert to text with basic markdown
    text = []

    # Process headings
    for i in range(1, 7):
        for heading in soup.find_all(f'h{i}'):
            heading.string = f"\n{'#' * i} {heading.get_text()}\n"

    # Process code blocks
    for pre in soup.find_all('pre'):
        code = pre.find('code')
        if code:
            pre.string = f"\n```\n{code.get_text()}\n```\n"

    # Process inline code
    for code in soup.find_all('code'):
        if code.parent.name != 'pre':
            code.string = f"`{code.get_text()}`"

    # Process links
    for link in soup.find_all('a'):
        href = link.get('href', '')
        text_content = link.get_text()
        link.string = f"[{text_content}]({href})"

    # Process bold
    for bold in soup.find_all(['strong', 'b']):
        bold.string = f"**{bold.get_text()}**"

    # Process italic
    for italic in soup.find_all(['em', 'i']):
        italic.string = f"*{italic.get_text()}*"

    # Process lists
    for ul in soup.find_all('ul'):
        for li in ul.find_all('li', recursive=False):
            li.string = f"- {li.get_text()}\n"

    for ol in soup.find_all('ol'):
        for idx, li in enumerate(ol.find_all('li', recursive=False), 1):
            li.string = f"{idx}. {li.get_text()}\n"

    # Get final text
    markdown = soup.get_text()

    # Clean up whitespace
    markdown = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown)
    markdown = markdown.strip()

    return f"# Source: {url}\n\n{markdown}"


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
    if path == "" or path == "/":
        return "index.md"

    # Remove leading/trailing slashes
    clean_path = path.strip("/")

    # Handle nested paths like howto/instances_create/
    if "/" in clean_path:
        # Convert to flat filename: howto/instances_create -> howto-instances_create.md
        return clean_path.replace("/", "-") + ".md"

    return clean_path + ".md"


def main():
    """Main function to download all LXD documentation."""
    print("=" * 60)
    print("LXD Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Sections to download: {len(LXD_DOC_SECTIONS)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "lxd"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, section_path in enumerate(LXD_DOC_SECTIONS, 1):
        url = urljoin(BASE_URL, section_path)
        filename = path_to_filename(section_path)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(LXD_DOC_SECTIONS)}] ", end="")

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
