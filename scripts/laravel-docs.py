#!/usr/bin/env python3
"""
Extract Laravel documentation from laravel/docs GitHub repository.
Source: https://github.com/laravel/docs
Output: docs/github-scraped/laravel/
"""

import os
import shutil
import subprocess
import tempfile
from pathlib import Path
import sys

def extract_laravel_docs():
    """Clone Laravel docs repo and extract documentation."""

    # Configuration
    REPO_URL = "https://github.com/laravel/docs.git"
    BRANCH = "master"
    SOURCE_FOLDER = "."
    TARGET_FOLDER = "docs/github-scraped/laravel"

    # Get absolute paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    target_path = repo_root / TARGET_FOLDER

    print(f"Extracting Laravel documentation...")
    print(f"Repository: {REPO_URL}")
    print(f"Branch: {BRANCH}")
    print(f"Target: {target_path}")

    # Create temporary directory for clone
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        clone_path = temp_path / "laravel-docs"

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

            # Check if we have markdown files
            md_files = list(clone_path.glob("*.md"))
            if not md_files:
                print(f"Error: No markdown files found in cloned repository")
                return False

            # Remove target folder if it exists
            if target_path.exists():
                print(f"Removing existing target folder: {target_path}")
                shutil.rmtree(target_path)

            # Create target folder
            target_path.mkdir(parents=True, exist_ok=True)

            # Copy all markdown files from root
            print(f"Copying documentation from {clone_path} to {target_path}...")
            for md_file in clone_path.glob("*.md"):
                shutil.copy2(md_file, target_path / md_file.name)

            # Count files
            files_copied = list(target_path.glob("*.md"))
            total_size = sum(f.stat().st_size for f in target_path.rglob("*") if f.is_file())

            print(f"\nExtraction complete!")
            print(f"Files copied: {len(files_copied)} markdown files")
            print(f"Total size: {total_size / 1024 / 1024:.2f} MB")
            print(f"Location: {target_path}")

            return True

        except subprocess.TimeoutExpired:
            print(f"Error: Clone operation timed out after 300 seconds")
            return False
        except Exception as e:
            print(f"Error during extraction: {e}")
            return False


if __name__ == "__main__":
    success = extract_laravel_docs()
    sys.exit(0 if success else 1)
