#!/usr/bin/env python3
"""
FormatJS Documentation Scraper
Downloads FormatJS documentation from GitHub repository and converts to markdown.
FormatJS is a modular collection of JavaScript libraries for internationalization.
"""

import os
import sys
import requests
from pathlib import Path
import time
import json

# Base URL for FormatJS GitHub repository
BASE_URL = "https://api.github.com/repos/formatjs/formatjs/contents"
RAW_BASE_URL = "https://raw.githubusercontent.com/formatjs/formatjs/main"

# Documentation directories to scrape
DOC_DIRS = [
    "website/docs/getting-started",
    "website/docs/core-concepts",
    "website/docs/guides",
    "website/docs/react-intl",
    "website/docs/vue-intl",
    "website/docs/intl",
    "website/docs/polyfills",
    "website/docs/tooling",
]

# Additional files to download
ADDITIONAL_FILES = [
    "README.md",
]


def get_files_in_directory(dir_path):
    """Get all markdown files in a directory from GitHub API."""
    try:
        # Use raw GitHub to avoid API rate limits
        # We'll try to get the directory listing via scraping
        raw_url = f"{RAW_BASE_URL}/{dir_path}"

        # For now, we'll just try common file names
        # This is a simplified approach since we're rate limited
        return []
    except Exception as e:
        print(f"    -> Error listing directory {dir_path}: {e}")
        return []


def try_download_file(repo_path, output_path):
    """Try to download a file from GitHub repository."""
    try:
        raw_url = f"{RAW_BASE_URL}/{repo_path}"

        print(f"  Trying: {repo_path}")

        response = requests.get(raw_url, timeout=15)

        if response.status_code == 404:
            print(f"    -> Not found (404)")
            return False

        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# FormatJS Documentation
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
        if "404" not in str(e):
            print(f"    -> Error downloading {repo_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {repo_path}: {e}")
        return False


def discover_docs_structure():
    """Discover documentation files by trying common patterns."""
    print("Discovering documentation structure...")

    # Common documentation files based on website structure
    known_files = [
        # Getting Started
        "website/docs/getting-started/installation.md",
        "website/docs/getting-started/message-declaration.md",
        "website/docs/getting-started/message-extraction.md",

        # Core Concepts
        "website/docs/core-concepts/basic-internationalization-principles.md",
        "website/docs/core-concepts/icu-syntax.md",

        # Guides
        "website/docs/guides/message-declaration.md",
        "website/docs/guides/runtime-requirements.md",
        "website/docs/guides/advanced.md",

        # React Intl
        "website/docs/react-intl/index.md",
        "website/docs/react-intl/api.md",
        "website/docs/react-intl/components.md",
        "website/docs/react-intl/upgrade-guide-2x.md",
        "website/docs/react-intl/upgrade-guide-3x.md",
        "website/docs/react-intl/upgrade-guide-4x.md",
        "website/docs/react-intl/upgrade-guide-5x.md",

        # Vue Intl
        "website/docs/vue-intl/index.md",

        # Intl Libraries
        "website/docs/intl.md",
        "website/docs/intl-messageformat.md",
        "website/docs/intl-numberformat.md",
        "website/docs/intl-datetimeformat.md",
        "website/docs/intl-relativetimeformat.md",
        "website/docs/intl-listformat.md",
        "website/docs/intl-displaynames.md",
        "website/docs/intl-locale.md",
        "website/docs/intl-pluralrules.md",

        # Polyfills
        "website/docs/polyfills.md",
        "website/docs/polyfills/intl-datetimeformat.md",
        "website/docs/polyfills/intl-displaynames.md",
        "website/docs/polyfills/intl-getcanonicallocales.md",
        "website/docs/polyfills/intl-listformat.md",
        "website/docs/polyfills/intl-locale.md",
        "website/docs/polyfills/intl-numberformat.md",
        "website/docs/polyfills/intl-pluralrules.md",
        "website/docs/polyfills/intl-relativetimeformat.md",

        # Tooling
        "website/docs/tooling/cli.md",
        "website/docs/tooling/linter.md",
        "website/docs/tooling/ts-transformer.md",
        "website/docs/tooling/swc-plugin.md",
    ]

    return known_files


def main():
    """Main function to download all FormatJS documentation."""
    print("=" * 60)
    print("FormatJS Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "formatjs"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Collect all files to download
    files_to_download = []

    # Add additional files
    files_to_download.extend(ADDITIONAL_FILES)

    # Add known documentation files
    files_to_download.extend(discover_docs_structure())

    print(f"\nAttempting to download {len(files_to_download)} files")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, repo_path in enumerate(files_to_download, 1):
        print(f"[{idx:2d}/{len(files_to_download)}] ", end="")

        # Create output filename
        if repo_path == "README.md":
            output_filename = "main-README.md"
        elif repo_path.startswith("website/docs/"):
            # Remove "website/docs/" prefix
            relative_path = repo_path.replace("website/docs/", "")
            # Replace slashes with dashes and remove .md extension, then re-add it
            output_filename = relative_path.replace("/", "-")
        else:
            output_filename = repo_path.replace("/", "-")

        output_path = output_dir / output_filename

        if try_download_file(repo_path, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.3)

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
