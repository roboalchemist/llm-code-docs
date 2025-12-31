#!/usr/bin/env python3
"""
Koa Documentation Scraper
Downloads Koa documentation from GitHub repository and converts to markdown.
Koa is a next generation web framework for Node.js.
"""

import os
import sys
import requests
from pathlib import Path
import time

# Base URL for Koa GitHub repository
RAW_BASE_URL = "https://raw.githubusercontent.com/koajs/koa/master/docs"

# Documentation files to download
DOCS_TO_DOWNLOAD = [
    "error-handling.md",
    "faq.md",
    "guide.md",
    "koa-vs-express.md",
    "migration-v1-to-v2.md",
    "migration-v2-to-v3.md",
    "troubleshooting.md",
    "api/index.md",
    "api/context.md",
    "api/request.md",
    "api/response.md",
]


def download_doc(doc_path, output_path):
    """Download a documentation file from GitHub repository."""
    try:
        raw_url = f"{RAW_BASE_URL}/{doc_path}"

        print(f"  Downloading: {doc_path}")

        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# Koa Documentation
# Source: {raw_url}
# Path: {doc_path}

"""
        content = header + content

        # Create output file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {doc_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {doc_path}: {e}")
        return False


def main():
    """Main function to download all Koa documentation."""
    print("=" * 60)
    print("Koa Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "koa"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    # Download all documentation files
    for idx, doc_path in enumerate(DOCS_TO_DOWNLOAD, 1):
        print(f"[{idx:3d}/{len(DOCS_TO_DOWNLOAD)}] ", end="")

        # Create output filename (preserve directory structure)
        output_filename = doc_path.replace('/', '-')
        output_path = output_dir / output_filename

        if download_doc(doc_path, output_path):
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
