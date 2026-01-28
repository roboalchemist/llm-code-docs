#!/usr/bin/env python3
"""
Extract only markdown documentation from rtorrent GitHub repository.
Extracts: README.md + all .md files from doc/manual/
Output: docs/github-scraped/rtorrent/
"""

import os
import shutil
import tempfile
import subprocess
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "rtorrent"
REPO_URL = "https://github.com/rakshasa/rtorrent.git"
TEMP_DIR = Path(tempfile.gettempdir()) / "rtorrent-extract"

def extract_rtorrent_docs():
    """Clone rtorrent and extract only markdown files."""

    # Clean and create output directory
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Clean temp directory
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    try:
        # Clone repository (shallow clone for speed)
        print(f"Cloning {REPO_URL}...")
        subprocess.run(
            ["git", "clone", "--depth", "1", REPO_URL, str(TEMP_DIR)],
            check=True,
            capture_output=True,
            timeout=60
        )

        # Copy README.md if it exists
        readme = TEMP_DIR / "README.md"
        if readme.exists():
            print(f"Copying {readme.name}...")
            shutil.copy2(readme, OUTPUT_DIR / "README.md")

        # Copy all markdown files from doc/manual/ folder
        manual_dir = TEMP_DIR / "doc" / "manual"
        if manual_dir.exists():
            print(f"Copying markdown files from {manual_dir.relative_to(TEMP_DIR)}...")
            for md_file in manual_dir.glob("*.md"):
                print(f"  - {md_file.name}")
                shutil.copy2(md_file, OUTPUT_DIR / md_file.name)

        # Report results
        md_files = list(OUTPUT_DIR.glob("*.md"))
        total_size = sum(f.stat().st_size for f in md_files)

        print(f"\nExtraction complete!")
        print(f"  Files: {len(md_files)}")
        print(f"  Size: {total_size / 1024:.1f} KB")
        print(f"  Location: {OUTPUT_DIR}")

        return len(md_files) > 0

    finally:
        # Clean temp directory
        if TEMP_DIR.exists():
            shutil.rmtree(TEMP_DIR)

if __name__ == "__main__":
    success = extract_rtorrent_docs()
    exit(0 if success else 1)
