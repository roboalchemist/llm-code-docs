#!/usr/bin/env python3
"""
A-Frame React Documentation Scraper
Downloads aframe-react documentation from GitHub repository and converts to markdown.
A-Frame React is a thin React wrapper for A-Frame VR experiences.
"""

import os
import sys
import requests
from pathlib import Path
import time

# Base URL for aframe-react GitHub repository
BASE_URL = "https://api.github.com/repos/supermedium/aframe-react/contents"
RAW_BASE_URL = "https://raw.githubusercontent.com/supermedium/aframe-react/master"

# Files to download
FILES_TO_DOWNLOAD = [
    "README.md",
    "package.json",
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
        header = f"""# A-Frame React Documentation
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
    """Main function to download all aframe-react documentation."""
    print("=" * 60)
    print("A-Frame React Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "aframe-react"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, repo_path in enumerate(FILES_TO_DOWNLOAD, 1):
        print(f"[{idx:2d}/{len(FILES_TO_DOWNLOAD)}] ", end="")

        # Create output filename
        if repo_path == "README.md":
            output_filename = "main-README.md"
        elif repo_path == "package.json":
            output_filename = "package.json"
        else:
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
    total_size = sum(f.stat().st_size for f in output_dir.glob("*"))
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
