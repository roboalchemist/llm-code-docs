#!/usr/bin/env python3
"""
ts-morph Documentation Scraper
Downloads ts-morph documentation from GitHub repository.
ts-morph is a TypeScript Compiler API wrapper for programmatic code manipulation and analysis.
"""

import os
import sys
import requests
from pathlib import Path
import time
import json

# Base URL for ts-morph GitHub repository (using latest branch)
BASE_URL = "https://api.github.com/repos/dsherret/ts-morph/contents"
RAW_BASE_URL = "https://raw.githubusercontent.com/dsherret/ts-morph/latest"

# Documentation directories to scrape
DOC_DIRS = [
    "docs",
]

# Additional files to download
ADDITIONAL_FILES = [
    "readme.md",
]


def get_files_in_directory(dir_path):
    """Get all markdown files in a directory from GitHub API."""
    try:
        url = f"{BASE_URL}/{dir_path}?ref=latest"
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        files = []
        for item in response.json():
            if item['type'] == 'file' and item['name'].endswith(('.md', '.markdown')):
                files.append(item['path'])

        return files
    except Exception as e:
        print(f"    -> Error listing directory {dir_path}: {e}")
        return []


def download_file(repo_path, output_path):
    """Download a file from GitHub repository."""
    try:
        raw_url = f"{RAW_BASE_URL}/{repo_path}"

        print(f"  Downloading: {repo_path}")

        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# ts-morph Documentation
# Source: {raw_url}
# Path: {repo_path}

"""
        content = header + content

        # Create output file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {repo_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {repo_path}: {e}")
        return False


def download_directory_recursive(dir_path, output_base_dir):
    """Recursively download all markdown files from a directory."""
    successful = 0
    failed = 0

    try:
        url = f"{BASE_URL}/{dir_path}?ref=latest"
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        for item in response.json():
            if item['type'] == 'file' and item['name'].endswith(('.md', '.markdown')):
                # Download file
                output_filename = item['name']
                output_path = output_base_dir / output_filename

                if download_file(item['path'], output_path):
                    successful += 1
                else:
                    failed += 1

                time.sleep(0.3)  # Rate limiting

            elif item['type'] == 'dir':
                # Recursively process subdirectories
                sub_output_dir = output_base_dir / item['name']
                sub_successful, sub_failed = download_directory_recursive(
                    item['path'], sub_output_dir
                )
                successful += sub_successful
                failed += sub_failed

    except Exception as e:
        print(f"    -> Error processing directory {dir_path}: {e}")
        failed += 1

    return successful, failed


def main():
    """Main function to download all ts-morph documentation."""
    print("=" * 60)
    print("ts-morph Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "ts-morph"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    # Download from docs directory recursively
    print("Downloading documentation from docs/ directory...")
    sub_successful, sub_failed = download_directory_recursive("docs", output_dir)
    successful += sub_successful
    failed += sub_failed

    print()

    # Download additional files
    print("Downloading additional files...")
    for file in ADDITIONAL_FILES:
        print(f"  Checking {file}...")
        try:
            url = f"{BASE_URL}/{file}?ref=latest"
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                output_path = output_dir / f"root-{file}"
                if download_file(file, output_path):
                    successful += 1
                else:
                    failed += 1
            time.sleep(0.3)
        except Exception as e:
            print(f"    -> Skipped {file}: {e}")

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
    total_size = sum(f.stat().st_size for f in output_dir.glob("**/*") if f.is_file())
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} files failed to download")
    else:
        print("All documentation downloaded successfully!")

    print(f"Documentation saved to: {output_dir}")


if __name__ == "__main__":
    main()
