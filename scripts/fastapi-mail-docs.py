#!/usr/bin/env python3
"""
FastAPI Mail Documentation Scraper
Downloads fastapi-mail documentation from GitHub repository and converts to markdown.
FastAPI Mail is a simple email sending library for FastAPI, supporting Jinja2 templates,
file attachments, and background tasks.
"""

import os
import sys
import requests
from pathlib import Path
import time
import json

# Base URL for fastapi-mail GitHub repository
BASE_URL = "https://api.github.com/repos/sabuhish/fastapi-mail/contents"
RAW_BASE_URL = "https://raw.githubusercontent.com/sabuhish/fastapi-mail/master"

# Documentation directories to explore
DOCS_DIRS = [
    ".",  # Root README
    "docs",  # Documentation files
]


def get_markdown_files_in_dir(dir_path):
    """Get all markdown files in a directory from GitHub API."""
    try:
        if dir_path == ".":
            url = f"{BASE_URL}/README.md"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return [{"path": "README.md", "name": "README.md"}]
            return []
        else:
            url = f"{BASE_URL}/{dir_path}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            contents = response.json()

            # Filter for markdown files
            md_files = [
                {"path": item["path"], "name": item["name"]}
                for item in contents
                if item["type"] == "file" and item["name"].endswith(".md")
            ]
            return md_files
    except Exception as e:
        print(f"  Warning: Could not fetch directory {dir_path}: {e}")
        return []


def download_file(repo_path, output_path):
    """Download a markdown file from GitHub repository."""
    try:
        raw_url = f"{RAW_BASE_URL}/{repo_path}"

        print(f"  Downloading: {repo_path}")

        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# FastAPI Mail Documentation
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


def main():
    """Main function to download all fastapi-mail documentation."""
    print("=" * 60)
    print("FastAPI Mail Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "fastapi-mail"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Discover all markdown files
    print("Discovering markdown files...")
    all_files = []
    for dir_path in DOCS_DIRS:
        print(f"  Exploring: {dir_path}")
        md_files = get_markdown_files_in_dir(dir_path)
        all_files.extend(md_files)
        time.sleep(0.3)  # Rate limiting for API calls

    print(f"\nFound {len(all_files)} markdown files")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, file_info in enumerate(all_files, 1):
        repo_path = file_info["path"]
        filename = file_info["name"]

        print(f"[{idx:2d}/{len(all_files)}] ", end="")

        # Create category-based output filename
        if repo_path == "README.md":
            output_filename = "main-README.md"
        else:
            # docs/getting-started.md -> docs-getting-started.md
            output_filename = repo_path.replace("/", "-")

        output_path = output_dir / output_filename

        if download_file(repo_path, output_path):
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
        print(f"Warning: {failed} files failed to download")
        sys.exit(1)
    else:
        print("All documentation downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
