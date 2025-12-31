#!/usr/bin/env python3
"""
React Styleguidist Documentation Scraper
Downloads React Styleguidist documentation from the GitHub repository.
React Styleguidist is an isolated React component development environment with a living style guide.
"""

import os
import sys
import requests
from pathlib import Path
import time

# Base URL for react-styleguidist GitHub repository
BASE_URL = "https://api.github.com/repos/styleguidist/react-styleguidist/contents"
RAW_BASE_URL = "https://raw.githubusercontent.com/styleguidist/react-styleguidist/master"

# Documentation files to download
DOCS_FILES = [
    "docs/API.md",
    "docs/CLI.md",
    "docs/Components.md",
    "docs/Configuration.md",
    "docs/Cookbook.md",
    "docs/Development.md",
    "docs/Documenting.md",
    "docs/GettingStarted.md",
    "docs/Maintenance.md",
    "docs/Readme.md",
    "docs/Thirdparties.md",
    "docs/Webpack.md",
]

# Main repository files
MAIN_FILES = [
    "Readme.md",
]


def download_file(repo_path, output_path):
    """Download a file from GitHub repository."""
    try:
        raw_url = f"{RAW_BASE_URL}/{repo_path}"

        print(f"  Downloading: {repo_path}")

        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# React Styleguidist Documentation
# Source: {raw_url}
# Path: {repo_path}

"""
        content = header + content

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


def main():
    """Main function to download all react-styleguidist documentation."""
    print("=" * 60)
    print("React Styleguidist Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "styleguidist"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    # Download all files
    all_files = MAIN_FILES + DOCS_FILES

    for idx, repo_path in enumerate(all_files, 1):
        print(f"[{idx:2d}/{len(all_files)}] ", end="")

        # Create output filename
        if repo_path.startswith("docs/"):
            # Remove docs/ prefix
            output_filename = repo_path.replace("docs/", "")
        else:
            # Main files
            output_filename = repo_path.replace("/", "-")

        # Rename main Readme.md to avoid collision with docs/Readme.md
        if repo_path == "Readme.md":
            output_filename = "main-README.md"

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
