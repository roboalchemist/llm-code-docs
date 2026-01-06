#!/usr/bin/env python3
"""
Neovim Documentation Scraper
Downloads Neovim documentation from GitHub repository.
Neovim is a hyperextensible Vim-based text editor with built-in LSP client support.
Focus: configuration, APIs, LSP integration, and Lua scripting.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
import time

def clone_neovim_repo():
    """Clone the Neovim repository and extract documentation."""
    print("=" * 60)
    print("Neovim Documentation Scraper")
    print("=" * 60)
    print()

    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "neovim"
    temp_dir = script_dir / ".temp" / "neovim-repo"

    print(f"Output directory: {output_dir}")
    print()

    # Clean up any existing output
    if output_dir.exists():
        print(f"Removing existing output directory: {output_dir}")
        shutil.rmtree(output_dir)

    # Clean up temp directory if it exists
    if temp_dir.exists():
        print(f"Removing existing temp directory: {temp_dir}")
        shutil.rmtree(temp_dir)

    temp_dir.parent.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    print()
    print("Cloning Neovim repository...")
    start_time = time.time()

    try:
        # Clone only the master branch (faster)
        clone_cmd = [
            "git", "clone",
            "--depth", "1",
            "--branch", "master",
            "https://github.com/neovim/neovim.git",
            str(temp_dir)
        ]
        subprocess.run(clone_cmd, check=True, capture_output=True, timeout=300)
        print("  -> Repository cloned successfully")
    except subprocess.TimeoutExpired:
        print("  -> ERROR: Clone operation timed out")
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        return 0, 1
    except subprocess.CalledProcessError as e:
        print(f"  -> ERROR: Failed to clone repository: {e}")
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        return 0, 1
    except Exception as e:
        print(f"  -> ERROR: Unexpected error during clone: {e}")
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        return 0, 1

    print()
    print("Extracting documentation files...")

    # Copy runtime/doc directory (main documentation)
    source_doc_dir = temp_dir / "runtime" / "doc"
    if source_doc_dir.exists():
        print(f"  Copying documentation from {source_doc_dir}")
        successful = 0
        failed = 0

        for file in source_doc_dir.glob("*.txt"):
            try:
                dest_file = output_dir / file.name
                shutil.copy2(file, dest_file)
                successful += 1
                print(f"    -> Copied: {file.name}")
            except Exception as e:
                print(f"    -> ERROR copying {file.name}: {e}")
                failed += 1

        # Also look for markdown files in doc directory
        for file in source_doc_dir.glob("*.md"):
            try:
                dest_file = output_dir / file.name
                shutil.copy2(file, dest_file)
                successful += 1
                print(f"    -> Copied: {file.name}")
            except Exception as e:
                print(f"    -> ERROR copying {file.name}: {e}")
                failed += 1
    else:
        print(f"  WARNING: Documentation directory not found at {source_doc_dir}")
        successful = 0
        failed = 1

    # Copy README files for context
    readme_files = [
        "README.md",
        "CONTRIBUTING.md",
        "BUILD.md",
        "INSTALL.md"
    ]

    print()
    print("Copying root documentation files...")
    readme_successful = 0
    readme_failed = 0

    for readme_name in readme_files:
        source_file = temp_dir / readme_name
        if source_file.exists():
            try:
                dest_file = output_dir / f"root-{readme_name}"
                shutil.copy2(source_file, dest_file)
                readme_successful += 1
                print(f"  -> Copied: {readme_name}")
            except Exception as e:
                print(f"  -> ERROR copying {readme_name}: {e}")
                readme_failed += 1
        else:
            print(f"  -> Not found: {readme_name}")

    # Clean up temp directory
    print()
    print("Cleaning up temporary files...")
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
        print("  -> Temporary files removed")

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Documentation files: {successful}")
    print(f"README files: {readme_successful}")
    print(f"Failed: {failed + readme_failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    if output_dir.exists():
        total_size = sum(f.stat().st_size for f in output_dir.glob("**/*") if f.is_file())
        print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
        file_count = len(list(output_dir.glob("*")))
        print(f"Total files: {file_count}")
    else:
        print("WARNING: Output directory is empty")

    print()
    if (failed + readme_failed) > 0:
        print(f"Warning: {failed + readme_failed} items failed to download")
    else:
        print("All documentation downloaded successfully!")

    print(f"Documentation saved to: {output_dir}")

    return successful + readme_successful, failed + readme_failed


if __name__ == "__main__":
    try:
        successful, failed = clone_neovim_repo()
        sys.exit(0 if failed == 0 else 1)
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)
