#!/usr/bin/env python3
"""
nano-css Documentation Scraper
Downloads nano-css CSS-in-JS documentation from GitHub repository and converts to markdown.
nano-css is a tiny 5th generation CSS-in-JS library for production use.
"""

import os
import sys
import requests
from pathlib import Path
import time
import subprocess

# Base URL for nano-css GitHub repository
BASE_URL = "https://api.github.com/repos/streamich/nano-css/contents"
RAW_BASE_URL = "https://raw.githubusercontent.com/streamich/nano-css/master"

# Documentation directories to explore
DOCS_DIRS = [
    ".",  # Root README and other files
    "docs",  # Documentation files
]

# Known documentation files from README
KNOWN_DOCS = [
    "README.md",
    "CHANGELOG.md",
    "SECURITY.md",
    "docs/Installation.md",
    "docs/Addons.md",
    "docs/put.md",
    "docs/rule.md",
    "docs/drule.md",
    "docs/sheet.md",
    "docs/dsheet.md",
    "docs/jsx.md",
    "docs/useStyles.md",
    "docs/withStyles.md",
    "docs/decorator.md",
    "docs/component.md",
    "docs/style.md",
    "docs/styled.md",
    "docs/hyperstyle.md",
    "docs/stable.md",
    "docs/atoms.md",
    "docs/emmet.md",
    "docs/nesting.md",
    "docs/keyframes.md",
    "docs/hydrate.md",
    "docs/prefixer.md",
    "docs/stylis.md",
    "docs/unitless.md",
    "docs/important.md",
    "docs/global.md",
    "docs/animations.md",
    "docs/resets.md",
    "docs/reset-font.md",
    "docs/googleFont.md",
    "docs/limit.md",
    "docs/amp.md",
    "docs/virtual.md",
    "docs/spread.md",
    "docs/array.md",
    "docs/snake.md",
    "docs/tachyons.md",
    "docs/rtl.md",
    "docs/extract.md",
    "docs/sourcemaps.md",
    "docs/units.md",
    "docs/cssom.md",
    "docs/vcssom.md",
    "docs/Presets.md",
    "docs/SSR.md",
]


def download_file(repo_path, output_path):
    """Download a markdown file from GitHub repository."""
    try:
        raw_url = f"{RAW_BASE_URL}/{repo_path}"

        print(f"  Downloading: {repo_path}")

        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# nano-css Documentation
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
    """Main function to download all nano-css documentation."""
    print("=" * 60)
    print("nano-css Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "nanocss"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    print(f"Processing {len(KNOWN_DOCS)} known documentation files...")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, repo_path in enumerate(KNOWN_DOCS, 1):
        print(f"[{idx:2d}/{len(KNOWN_DOCS)}] ", end="")

        # Create category-based output filename
        if repo_path == "README.md":
            output_filename = "main-README.md"
        else:
            # docs/installation.md -> docs-installation.md
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
