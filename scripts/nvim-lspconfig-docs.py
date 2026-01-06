#!/usr/bin/env python3
"""
Scraper for nvim-lspconfig documentation.
Extracts documentation from the GitHub repository's doc/ folder.
Output: docs/github-scraped/nvim-lspconfig/
"""

import subprocess
import shutil
import tempfile
from pathlib import Path

REPO_URL = "https://github.com/neovim/nvim-lspconfig.git"
SOURCE_FOLDER = "doc"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "nvim-lspconfig"
BRANCH = "master"

def main():
    """Clone repository and extract documentation."""
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Create temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        repo_path = temp_path / "nvim-lspconfig"

        print(f"Cloning {REPO_URL}...")
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", "--branch", BRANCH, REPO_URL, str(repo_path)],
                check=True,
                capture_output=True,
                timeout=300
            )
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e}")
            return

        # Copy documentation folder
        source_path = repo_path / SOURCE_FOLDER
        if not source_path.exists():
            print(f"Source folder {SOURCE_FOLDER} not found in repository")
            return

        print(f"Extracting documentation from {SOURCE_FOLDER}/...")

        # Remove existing files to ensure clean extraction
        if OUTPUT_DIR.exists():
            for item in OUTPUT_DIR.iterdir():
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item)

        # Copy files
        for source_file in source_path.iterdir():
            if source_file.is_file():
                dest_file = OUTPUT_DIR / source_file.name
                shutil.copy2(source_file, dest_file)
                print(f"  Copied: {source_file.name}")

        # Count and report
        files = list(OUTPUT_DIR.glob("*"))
        print(f"\nExtraction complete!")
        print(f"Total files: {len(files)}")
        print(f"Output directory: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
