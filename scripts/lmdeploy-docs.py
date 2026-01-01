#!/usr/bin/env python3
"""
Extract LMDeploy documentation from GitHub repository.
Source: https://github.com/InternLM/lmdeploy (main branch, docs/en folder)
Output: docs/github-scraped/lmdeploy/
"""

import os
import shutil
import subprocess
import tempfile
from pathlib import Path
import sys

def extract_lmdeploy_docs():
    """Clone LMDeploy repo and extract documentation."""

    # Configuration
    REPO_URL = "https://github.com/InternLM/lmdeploy.git"
    BRANCH = "main"
    SOURCE_FOLDER = "docs/en"
    TARGET_FOLDER = "docs/github-scraped/lmdeploy"

    # Get absolute paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    target_path = repo_root / TARGET_FOLDER

    print(f"Extracting LMDeploy documentation...")
    print(f"Repository: {REPO_URL}")
    print(f"Branch: {BRANCH}")
    print(f"Target: {target_path}")

    # Create temporary directory for clone
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        clone_path = temp_path / "lmdeploy"

        try:
            # Clone the repository
            print(f"\nCloning repository to {clone_path}...")
            result = subprocess.run(
                ["git", "clone", "--depth=1", "--branch", BRANCH, REPO_URL, str(clone_path)],
                capture_output=True,
                text=True,
                timeout=300
            )

            if result.returncode != 0:
                print(f"Error cloning repository:")
                print(result.stderr)
                return False

            print("Clone successful")

            # Check if source folder exists
            source_path = clone_path / SOURCE_FOLDER
            if not source_path.exists():
                print(f"Error: Source folder '{SOURCE_FOLDER}' not found in cloned repository")
                return False

            # Remove target folder if it exists
            if target_path.exists():
                print(f"Removing existing target folder: {target_path}")
                shutil.rmtree(target_path)

            # Copy documentation
            print(f"Copying documentation from {source_path} to {target_path}...")
            shutil.copytree(source_path, target_path)

            # Count files
            md_files = list(target_path.rglob("*.md"))
            rst_files = list(target_path.rglob("*.rst"))
            total_files = len(md_files) + len(rst_files)
            total_size = sum(f.stat().st_size for f in target_path.rglob("*") if f.is_file())

            print(f"\nExtraction complete!")
            print(f"Markdown files: {len(md_files)}")
            print(f"RST files: {len(rst_files)}")
            print(f"Total files: {total_files}")
            print(f"Total size: {total_size / 1024 / 1024:.2f} MB")
            print(f"Location: {target_path}")

            return True

        except subprocess.TimeoutExpired:
            print("Error: Clone operation timed out")
            return False
        except Exception as e:
            print(f"Error during extraction: {e}")
            return False

if __name__ == "__main__":
    success = extract_lmdeploy_docs()
    sys.exit(0 if success else 1)
