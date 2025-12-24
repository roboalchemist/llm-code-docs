#!/usr/bin/env python3
"""
Headscale Documentation Scraper
Downloads all headscale documentation from GitHub repository.
Headscale is an open-source, self-hosted implementation of the Tailscale control server.
"""

import os
import sys
import requests
from pathlib import Path
import time

GITHUB_REPO = "juanfont/headscale"
GITHUB_BRANCH = "main"
DOCS_PATH = "docs"
GITHUB_API_BASE = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{DOCS_PATH}"
GITHUB_RAW_BASE = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{GITHUB_BRANCH}/{DOCS_PATH}"


def get_directory_contents(path=""):
    """Recursively get all markdown files from the docs directory."""
    api_url = f"{GITHUB_API_BASE}/{path}" if path else GITHUB_API_BASE

    try:
        response = requests.get(api_url, timeout=15)
        response.raise_for_status()
        contents = response.json()

        files = []
        for item in contents:
            if item['type'] == 'file' and item['name'].endswith('.md'):
                # Store relative path from docs/
                rel_path = f"{path}/{item['name']}" if path else item['name']
                files.append(rel_path)
            elif item['type'] == 'dir':
                # Recursively get files from subdirectories
                subdir_path = f"{path}/{item['name']}" if path else item['name']
                files.extend(get_directory_contents(subdir_path))

        return files

    except requests.exceptions.RequestException as e:
        print(f"  -> Error fetching directory {path}: {e}")
        return []


def download_file(file_path, output_dir):
    """Download a single markdown file from GitHub."""
    try:
        # Construct raw GitHub URL
        url = f"{GITHUB_RAW_BASE}/{file_path}"

        print(f"Downloading: {file_path}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Get content
        content = response.text

        # Add source header
        source_url = f"https://github.com/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{DOCS_PATH}/{file_path}"
        markdown = f"# Source: {source_url}\n\n{content}"

        # Create output path maintaining directory structure
        output_path = output_dir / file_path
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {file_path}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {file_path}: {e}")
        return False


def main():
    """Main function to download all headscale documentation."""
    print("=" * 60)
    print("Headscale Documentation Scraper")
    print("=" * 60)
    print(f"Repository: {GITHUB_REPO}")
    print(f"Branch: {GITHUB_BRANCH}")
    print(f"Docs path: {DOCS_PATH}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "headscale"

    print(f"Output directory: {output_dir}")
    print()

    # Get all markdown files
    print("Discovering markdown files...")
    md_files = get_directory_contents()

    if not md_files:
        print("Error: No markdown files found!")
        sys.exit(1)

    print(f"Found {len(md_files)} markdown files")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, file_path in enumerate(sorted(md_files), 1):
        print(f"[{i:2d}/{len(md_files)}] ", end="")

        if download_file(file_path, output_dir):
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
    total_size = sum(f.stat().st_size for f in output_dir.rglob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} files failed to download")
        sys.exit(1)
    else:
        print("All files downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
