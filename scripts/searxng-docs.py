#!/usr/bin/env python3
"""
SearXNG Documentation Scraper
Downloads SearXNG documentation from the searxng/searxng GitHub repository.
SearXNG is a privacy-respecting, hackable metasearch engine that aggregates results
from various search services and databases.
"""

import os
import sys
import requests
from pathlib import Path
import time
import re

# Base URLs
GITHUB_API_BASE = "https://api.github.com/repos/searxng/searxng/contents"
RAW_BASE_URL = "https://raw.githubusercontent.com/searxng/searxng/master"

# Documentation sections to download (directories to recursively scrape)
DOCS_SECTIONS = [
    "docs/admin",
    "docs/dev",
    "docs/user",
    "docs/build-templates",
    "docs/utils",
]

# Also grab the main README
MAIN_FILES = [
    "README.rst",
]

# Rate limiting
REQUEST_DELAY = 0.5  # seconds between requests


def sanitize_filename(path):
    """Convert path to safe filename."""
    # Replace path separators with dashes
    safe = path.replace("/", "-").replace("\\", "-")
    # Remove leading/trailing dashes
    safe = safe.strip("-")
    return safe


def download_file(repo_path, output_dir):
    """Download a single file from GitHub repository."""
    try:
        raw_url = f"{RAW_BASE_URL}/{repo_path}"

        print(f"  Downloading: {repo_path}")

        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# SearXNG Documentation
# Source: {raw_url}
# Path: {repo_path}

"""
        content = header + content

        # Create output filename
        # Extract just the filename part
        filename = repo_path.split('/')[-1]

        # Convert .rst files to .md extension for consistency
        if filename.endswith('.rst'):
            filename = filename[:-4] + '.md'
        elif not filename.endswith('.md'):
            filename = filename + '.md'

        # Use the full path structure to avoid name collisions
        safe_path = sanitize_filename(repo_path)
        if safe_path.endswith('.rst'):
            safe_path = safe_path[:-4] + '.md'
        elif not safe_path.endswith('.md'):
            safe_path = safe_path + '.md'

        output_path = output_dir / safe_path

        # Create output file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {output_path.name}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {repo_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {repo_path}: {e}")
        return False


def list_directory_contents(repo_path):
    """List contents of a directory in the GitHub repository."""
    try:
        api_url = f"{GITHUB_API_BASE}/{repo_path}"

        response = requests.get(api_url, timeout=15)
        response.raise_for_status()

        contents = response.json()

        files = []
        dirs = []

        for item in contents:
            if item['type'] == 'file':
                # Include markdown and RST files
                if item['name'].endswith('.md') or item['name'].endswith('.rst') or item['name'].endswith('.mdx'):
                    files.append(item['path'])
            elif item['type'] == 'dir':
                dirs.append(item['path'])

        return files, dirs

    except Exception as e:
        print(f"    -> Error listing {repo_path}: {e}")
        return [], []


def download_directory_recursive(repo_path, output_dir, max_depth=5, current_depth=0):
    """Recursively download all documentation files from a directory."""
    if current_depth >= max_depth:
        print(f"  Skipping {repo_path} (max depth reached)")
        return 0, 0

    print(f"\n{'  ' * current_depth}Exploring: {repo_path}")

    files, dirs = list_directory_contents(repo_path)
    time.sleep(REQUEST_DELAY)

    successful = 0
    failed = 0

    # Download all documentation files in current directory
    for file_path in files:
        if download_file(file_path, output_dir):
            successful += 1
        else:
            failed += 1
        time.sleep(REQUEST_DELAY)

    # Recursively download subdirectories
    for dir_path in dirs:
        sub_success, sub_failed = download_directory_recursive(
            dir_path, output_dir, max_depth, current_depth + 1
        )
        successful += sub_success
        failed += sub_failed

    return successful, failed


def main():
    """Main function to download all SearXNG documentation."""
    print("=" * 60)
    print("SearXNG Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "searxng"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    start_time = time.time()
    total_successful = 0
    total_failed = 0

    # Download main README
    print("Downloading main README...")
    for main_file in MAIN_FILES:
        if download_file(main_file, output_dir):
            total_successful += 1
        else:
            total_failed += 1
        time.sleep(REQUEST_DELAY)

    # Download each documentation section recursively
    print(f"\nDownloading {len(DOCS_SECTIONS)} documentation sections...")
    for section in DOCS_SECTIONS:
        successful, failed = download_directory_recursive(section, output_dir)
        total_successful += successful
        total_failed += failed

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {total_successful}")
    print(f"Failed: {total_failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.rglob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if total_failed > 0:
        print(f"Warning: {total_failed} files failed to download")
        sys.exit(1)
    else:
        print("All documentation downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
