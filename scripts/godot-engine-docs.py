#!/usr/bin/env python3
"""
Extract Godot Engine documentation from the godot-docs GitHub repository.
Source: https://github.com/godotengine/godot-docs (4.6 branch for stable docs)
Output: docs/github-scraped/godot-engine/

This scraper fetches the complete Godot Engine documentation including:
- API reference
- Editor guide and tutorials
- Scripting documentation
- All other guides and manuals
"""

import os
import shutil
import subprocess
import tempfile
from pathlib import Path
import sys


def extract_godot_docs():
    """Clone Godot docs repo and extract documentation."""

    # Configuration
    REPO_URL = "https://github.com/godotengine/godot-docs.git"
    BRANCH = "4.6"  # Latest stable branch
    SOURCE_FOLDER = "."  # Documentation is at root, we'll copy specific directories
    TARGET_FOLDER = "docs/github-scraped/godot-engine"

    # Get absolute paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    target_path = repo_root / TARGET_FOLDER

    print(f"Extracting Godot Engine documentation...")
    print(f"Repository: {REPO_URL}")
    print(f"Branch: {BRANCH}")
    print(f"Target: {target_path}")

    # Create temporary directory for clone
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        clone_path = temp_path / "godot-docs"

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

            # Remove target folder if it exists
            if target_path.exists():
                print(f"Removing existing target folder: {target_path}")
                shutil.rmtree(target_path)

            # Create target directory
            target_path.mkdir(parents=True, exist_ok=True)

            # Copy relevant documentation directories
            print(f"Copying documentation directories from {clone_path} to {target_path}...")

            # Key documentation directories and files
            doc_dirs = ['about', 'classes', 'community', 'engine_details', 'getting_started', 'tutorials', 'img']
            doc_files = ['index.rst', 'conf.py', 'README.md', 'glossary.rst']

            for dir_name in doc_dirs:
                src_dir = clone_path / dir_name
                dst_dir = target_path / dir_name
                if src_dir.exists():
                    print(f"  Copying {dir_name}/...")
                    shutil.copytree(src_dir, dst_dir)

            for file_name in doc_files:
                src_file = clone_path / file_name
                dst_file = target_path / file_name
                if src_file.exists():
                    print(f"  Copying {file_name}...")
                    shutil.copy2(src_file, dst_file)

            # Count files
            md_files = list(target_path.rglob("*.md"))
            rst_files = list(target_path.rglob("*.rst"))
            all_files = md_files + rst_files
            total_size = sum(f.stat().st_size for f in target_path.rglob("*") if f.is_file())

            print(f"\nExtraction complete!")
            print(f"Markdown files: {len(md_files)}")
            print(f"RST files: {len(rst_files)}")
            print(f"Total documentation files: {len(all_files)}")
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
    success = extract_godot_docs()
    sys.exit(0 if success else 1)
