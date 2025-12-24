#!/usr/bin/env python3
"""
Mistral Vibe Documentation Scraper
Downloads documentation from the mistralai/mistral-vibe GitHub repository.
Mistral Vibe is an open-source CLI coding assistant powered by Mistral's models.
"""

import os
import sys
import requests
from pathlib import Path
import time

# GitHub raw content base URL
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/mistralai/mistral-vibe/main"

# Documentation files to download
DOC_FILES = [
    # Main documentation
    {"path": "README.md", "output": "readme.md"},
    {"path": "CHANGELOG.md", "output": "changelog.md"},
    {"path": "CONTRIBUTING.md", "output": "contributing.md"},
    {"path": "AGENTS.md", "output": "agents-guidelines.md"},
    {"path": "LICENSE", "output": "license.txt"},
]


def download_file(url, output_path):
    """Download a file from GitHub raw content."""
    try:
        print(f"Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Add source header for markdown files
        content = response.text
        if output_path.suffix == '.md':
            content = f"# Source: {url}\n\n{content}"

        # Write file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def create_llms_full(output_dir):
    """Create a combined llms-full.txt file from all documentation."""
    print("Creating llms-full.txt...")

    # Read all markdown files in order
    combined_content = []

    # Add header
    combined_content.append("# Mistral Vibe Documentation")
    combined_content.append("")
    combined_content.append("Repository: https://github.com/mistralai/mistral-vibe")
    combined_content.append("Mistral's open-source CLI coding assistant powered by Mistral's models.")
    combined_content.append("")
    combined_content.append("## Overview")
    combined_content.append("")
    combined_content.append("Mistral Vibe is a command-line coding assistant that provides a conversational")
    combined_content.append("interface to your codebase, allowing you to use natural language to explore,")
    combined_content.append("modify, and interact with your projects through a powerful set of tools.")
    combined_content.append("")
    combined_content.append("---")
    combined_content.append("")

    # Order of files for combined doc
    file_order = [
        "readme.md",
        "agents-guidelines.md",
        "contributing.md",
        "changelog.md",
    ]

    for filename in file_order:
        filepath = output_dir / filename
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Add section separator
            combined_content.append(f"\n## File: {filename}\n")
            combined_content.append(content)
            combined_content.append("\n---\n")

    # Write combined file
    llms_full_path = output_dir / "llms-full.txt"
    with open(llms_full_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(combined_content))

    print(f"  -> Created: {llms_full_path}")


def main():
    """Main function to download Mistral Vibe documentation."""
    print("=" * 60)
    print("Mistral Vibe Documentation Scraper")
    print("=" * 60)
    print(f"Source: {GITHUB_RAW_BASE}")
    print(f"Files to download: {len(DOC_FILES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "mistral-vibe"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, doc in enumerate(DOC_FILES, 1):
        url = f"{GITHUB_RAW_BASE}/{doc['path']}"
        output_path = output_dir / doc['output']

        print(f"[{i:2d}/{len(DOC_FILES)}] ", end="")

        if download_file(url, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.3)

    # Create combined llms-full.txt
    create_llms_full(output_dir)

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
        print("All files downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
