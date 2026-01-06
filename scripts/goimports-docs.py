#!/usr/bin/env python3
"""
goimports Documentation Scraper
Downloads goimports documentation from the GitHub repository.
goimports is a Go tool that automatically manages import statements (adding missing and removing unreferenced ones) and formats code.
"""

import os
import sys
import requests
from pathlib import Path
import time
from urllib.parse import urljoin

# GitHub repository details
GITHUB_REPO = "golang/tools"
GITHUB_API_BASE = "https://api.github.com/repos"
RAW_GITHUB_BASE = "https://raw.githubusercontent.com"

# Files to download from the repository
FILES_TO_DOWNLOAD = [
    "cmd/goimports/doc.go",
    "cmd/goimports/goimports.go",
]

REQUEST_DELAY = 0.5  # seconds between requests


def download_file(repo_path, output_dir):
    """Download a file from GitHub repository."""
    try:
        # Try raw.githubusercontent first (faster)
        url = f"{RAW_GITHUB_BASE}/{GITHUB_REPO}/master/{repo_path}"

        print(f"  Downloading: {repo_path}")

        response = requests.get(url, timeout=15)

        # If not found on master, try main branch
        if response.status_code == 404:
            url = f"{RAW_GITHUB_BASE}/{GITHUB_REPO}/main/{repo_path}"
            response = requests.get(url, timeout=15)

        response.raise_for_status()

        content = response.text

        # Determine output filename
        filename = Path(repo_path).name
        if not filename.endswith('.md'):
            filename = filename + '.md'

        # Add source header for Go files
        if repo_path.endswith('.go'):
            header = f"""# Source: {url}

```go
"""
            footer = """```
"""
            content = header + content + footer
        else:
            # For markdown files, add source comment at top
            header = f"""# Source: {url}

"""
            content = header + content

        # Save to file
        output_path = output_dir / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {repo_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {repo_path}: {e}")
        return False


def main():
    """Main function to download goimports documentation."""
    print("=" * 60)
    print("goimports Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "goimports"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Download all files
    print("Downloading documentation files...")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, file_path in enumerate(FILES_TO_DOWNLOAD, 1):
        print(f"[{idx:2d}/{len(FILES_TO_DOWNLOAD)}] ", end="")

        if download_file(file_path, output_dir):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(REQUEST_DELAY)

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
