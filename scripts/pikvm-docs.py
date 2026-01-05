#!/usr/bin/env python3
"""
PiKVM Documentation Extractor
Downloads PiKVM documentation from GitHub repository's docs folder.
PiKVM is an IP-based KVM (keyboard, video, mouse) control solution.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
import time

# GitHub repository details
REPO_URL = "https://github.com/pikvm/pikvm.git"
REPO_BRANCH = "master"
DOCS_FOLDER = "docs"


def clone_repo(temp_dir, repo_url, branch):
    """Clone the GitHub repository to temporary directory."""
    try:
        print(f"  Cloning repository from {repo_url} (branch: {branch})...")
        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", branch, repo_url, temp_dir],
            capture_output=True,
            text=True,
            timeout=300
        )
        if result.returncode != 0:
            print(f"    -> Error cloning repository: {result.stderr}")
            return False
        print(f"    -> Repository cloned successfully")
        return True
    except Exception as e:
        print(f"    -> Error during clone: {e}")
        return False


def copy_docs(temp_dir, output_dir, docs_folder):
    """Copy documentation files from temp directory to output directory."""
    try:
        source_docs_path = Path(temp_dir) / docs_folder
        
        if not source_docs_path.exists():
            print(f"    -> Error: {docs_folder} folder not found in repository")
            return False
        
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy all files from docs folder
        copied_count = 0
        for src_file in source_docs_path.rglob("*"):
            if src_file.is_file():
                # Calculate relative path
                rel_path = src_file.relative_to(source_docs_path)
                dst_file = output_dir / rel_path
                
                # Create parent directories
                dst_file.parent.mkdir(parents=True, exist_ok=True)
                
                # Copy file
                shutil.copy2(src_file, dst_file)
                copied_count += 1
        
        print(f"    -> Copied {copied_count} files from {docs_folder}")
        return True
        
    except Exception as e:
        print(f"    -> Error copying documentation: {e}")
        return False


def main():
    """Main function to extract PiKVM documentation."""
    print("=" * 60)
    print("PiKVM Documentation Extractor")
    print("=" * 60)
    print()

    # Setup directories
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "pikvm"
    temp_dir = Path("/tmp") / "pikvm-repo-clone"
    
    print(f"Output directory: {output_dir}")
    print()

    # Clean output directory if it exists
    if output_dir.exists():
        print("Removing existing output directory...")
        shutil.rmtree(output_dir)
    
    # Clean temp directory if it exists
    if temp_dir.exists():
        shutil.rmtree(temp_dir)

    start_time = time.time()

    # Clone repository
    print("Cloning repository...")
    if not clone_repo(temp_dir, REPO_URL, REPO_BRANCH):
        print("\nError: Failed to clone repository")
        sys.exit(1)

    print()

    # Copy documentation
    print("Extracting documentation...")
    if not copy_docs(temp_dir, output_dir, DOCS_FOLDER):
        print("\nError: Failed to copy documentation")
        shutil.rmtree(temp_dir)
        sys.exit(1)

    print()

    # Cleanup temp directory
    try:
        shutil.rmtree(temp_dir)
        print("Cleaned up temporary directory")
    except Exception as e:
        print(f"Warning: Could not clean up temp directory: {e}")

    elapsed = time.time() - start_time

    # Summary
    print()
    print("=" * 60)
    print("Extraction Summary")
    print("=" * 60)
    
    # Count files and calculate size
    if output_dir.exists():
        files = list(output_dir.rglob("*"))
        file_count = sum(1 for f in files if f.is_file())
        total_size = sum(f.stat().st_size for f in files if f.is_file())
        
        print(f"Files extracted: {file_count}")
        print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
        print(f"Time: {elapsed:.1f} seconds")
        print(f"Output: {output_dir}")
        print()
        print("Documentation extracted successfully!")
        sys.exit(0)
    else:
        print("Error: Output directory was not created")
        sys.exit(1)


if __name__ == "__main__":
    main()
