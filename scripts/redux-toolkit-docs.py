#!/usr/bin/env python3
"""
Redux Toolkit Documentation Scraper
Downloads Redux Toolkit documentation from GitHub repository via git clone.
Redux Toolkit is the official library for efficient Redux development, including RTK Query
for data fetching and caching.
"""

import os
import sys
import subprocess
from pathlib import Path
import shutil
import tempfile
import time

def clone_repo(clone_dir):
    """Clone the Redux Toolkit repository with sparse checkout."""
    try:
        print("Cloning Redux Toolkit repository...")
        subprocess.run(
            ["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse",
             "https://github.com/reduxjs/redux-toolkit.git", clone_dir],
            check=True,
            capture_output=True,
            timeout=120
        )

        # Configure sparse checkout for docs folder
        subprocess.run(
            ["git", "-C", clone_dir, "sparse-checkout", "set", "docs"],
            check=True,
            capture_output=True,
            timeout=30
        )

        print("  -> Repository cloned successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  -> Error cloning repository: {e}")
        print(f"  -> stderr: {e.stderr.decode() if e.stderr else 'N/A'}")
        return False
    except Exception as e:
        print(f"  -> Error: {e}")
        return False


def copy_docs(source_dir, output_dir):
    """Copy documentation files from cloned repo to output directory."""
    try:
        docs_source = Path(source_dir) / "docs"

        if not docs_source.exists():
            print(f"  -> Error: Documentation directory not found at {docs_source}")
            return False

        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        # Copy all markdown and MDX files recursively
        file_count = 0
        for src_file in docs_source.rglob("*"):
            if src_file.is_file() and src_file.suffix in [".md", ".mdx"]:
                # Create relative path structure
                rel_path = src_file.relative_to(docs_source)
                dest_file = output_dir / rel_path

                # Create destination directory if needed
                dest_file.parent.mkdir(parents=True, exist_ok=True)

                # Copy the file
                shutil.copy2(src_file, dest_file)
                file_count += 1

        if file_count == 0:
            print(f"  -> Warning: No markdown files found in {docs_source}")
            return False

        print(f"  -> Copied {file_count} documentation files")
        return True

    except Exception as e:
        print(f"  -> Error copying documentation: {e}")
        return False


def main():
    """Main function to download Redux Toolkit documentation."""
    print("=" * 60)
    print("Redux Toolkit Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "redux-toolkit"

    print(f"Output directory: {output_dir}")
    print()

    start_time = time.time()

    # Use temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_clone_dir = Path(temp_dir) / "redux-toolkit"

        # Clone the repository
        if not clone_repo(str(temp_clone_dir)):
            print()
            print("Failed to clone repository")
            sys.exit(1)

        # Copy documentation
        if not copy_docs(temp_clone_dir, output_dir):
            print()
            print("Failed to copy documentation")
            sys.exit(1)

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Output: {output_dir}")

    # Calculate total size and file count
    if output_dir.exists():
        files = list(output_dir.glob("**/*.md*"))
        total_size = sum(f.stat().st_size for f in files)
        print(f"Files: {len(files)}")
        print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
        print(f"Time: {elapsed:.1f} seconds")
        print()
        print("Documentation downloaded successfully!")
        sys.exit(0)
    else:
        print("Output directory was not created")
        sys.exit(1)


if __name__ == "__main__":
    main()
