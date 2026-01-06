#!/usr/bin/env python3
"""
WasmEdge Documentation Extractor
Clones the WasmEdge docs repository and extracts markdown files.
WasmEdge is a high-performance WebAssembly runtime for edge computing.
"""

import os
import sys
import shutil
import tempfile
import subprocess
from pathlib import Path
from urllib.parse import urljoin

def clone_repo(repo_url, temp_dir, branch="main"):
    """Clone the repository from GitHub."""
    try:
        print(f"Cloning repository: {repo_url}")
        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", branch, repo_url, temp_dir],
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode != 0:
            print(f"Error cloning repository: {result.stderr}")
            return False

        print(f"Repository cloned successfully to {temp_dir}")
        return True

    except subprocess.TimeoutExpired:
        print("Error: Clone operation timed out")
        return False
    except Exception as e:
        print(f"Error cloning repository: {e}")
        return False


def copy_markdown_files(source_dir, target_dir):
    """Copy all markdown files from source to target, preserving directory structure."""
    try:
        source_path = Path(source_dir)
        target_path = Path(target_dir)

        # Create target directory
        target_path.mkdir(parents=True, exist_ok=True)

        # Count files
        md_files = list(source_path.rglob("*.md"))
        print(f"Found {len(md_files)} markdown files")

        # Copy all markdown files
        copied = 0
        for source_file in md_files:
            # Preserve directory structure relative to source
            relative_path = source_file.relative_to(source_path)
            target_file = target_path / relative_path

            # Create parent directories
            target_file.parent.mkdir(parents=True, exist_ok=True)

            # Copy file
            shutil.copy2(source_file, target_file)
            copied += 1

            if copied % 10 == 0:
                print(f"  Copied {copied} files...")

        print(f"Successfully copied {copied} markdown files")
        return True

    except Exception as e:
        print(f"Error copying markdown files: {e}")
        return False


def add_metadata_headers(target_dir, source_url):
    """Add metadata headers to markdown files if they don't have them."""
    try:
        target_path = Path(target_dir)
        md_files = list(target_path.rglob("*.md"))

        updated = 0
        for md_file in md_files:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if already has source header
            if not content.startswith("# Source:"):
                # Calculate relative path for reference
                relative_path = md_file.relative_to(target_path)

                # Add metadata header
                header = f"# Source: {source_url}\n# Path: {relative_path}\n\n"
                content = header + content

                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)

                updated += 1

        if updated > 0:
            print(f"Added metadata headers to {updated} files")

        return True

    except Exception as e:
        print(f"Error adding metadata headers: {e}")
        return False


def main():
    """Main function to extract WasmEdge documentation."""
    print("=" * 70)
    print("WasmEdge Documentation Extractor")
    print("=" * 70)
    print()

    # Configuration
    repo_url = "https://github.com/WasmEdge/docs.git"
    source_folder = "docs"
    branch = "main"

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "wasmedge"

    print(f"Repository: {repo_url}")
    print(f"Source folder: {source_folder}")
    print(f"Output directory: {output_dir}")
    print()

    # Remove existing directory if it exists
    if output_dir.exists():
        print(f"Removing existing directory: {output_dir}")
        shutil.rmtree(output_dir)

    # Create temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        print("Cloning repository...")
        if not clone_repo(repo_url, temp_dir, branch):
            print("Failed to clone repository")
            sys.exit(1)

        print()

        # Check if source folder exists
        source_path = Path(temp_dir) / source_folder
        if not source_path.exists():
            print(f"Error: Source folder '{source_folder}' not found in repository")
            sys.exit(1)

        print(f"Extracting documentation from: {source_path}")
        print()

        # Copy markdown files
        if not copy_markdown_files(source_path, output_dir):
            print("Failed to copy markdown files")
            sys.exit(1)

        print()

        # Add metadata headers
        if not add_metadata_headers(output_dir, repo_url):
            print("Failed to add metadata headers")
            sys.exit(1)

    print()
    print("=" * 70)
    print("Extraction Summary")
    print("=" * 70)

    # Calculate statistics
    md_files = list(output_dir.rglob("*.md"))
    total_size = sum(f.stat().st_size for f in md_files)

    print(f"Files extracted: {len(md_files)}")
    print(f"Total size: {total_size:,} bytes ({total_size/1024/1024:.1f} MB)")
    print(f"Output directory: {output_dir}")
    print()
    print("Documentation extraction completed successfully!")

    return 0


if __name__ == "__main__":
    sys.exit(main())
