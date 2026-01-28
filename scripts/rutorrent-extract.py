#!/usr/bin/env python3
"""
Extract only markdown documentation from ruTorrent GitHub repository.
Extracts: README.md only (minimal documentation available)
Output: docs/github-scraped/rutorrent/
"""

import os
import shutil
import tempfile
import subprocess
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "rutorrent"
REPO_URL = "https://github.com/Novik/ruTorrent.git"
TEMP_DIR = Path(tempfile.gettempdir()) / "rutorrent-extract"

def extract_rutorrent_docs():
    """Clone ruTorrent and extract only markdown files."""

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
        else:
            # No documentation found
            print("Warning: No README.md found in repository")
            return False

        # Report results
        md_files = list(OUTPUT_DIR.glob("*.md"))
        total_size = sum(f.stat().st_size for f in md_files)

        print(f"\nExtraction complete!")
        print(f"  Files: {len(md_files)}")
        print(f"  Size: {total_size / 1024:.1f} KB")
        print(f"  Location: {OUTPUT_DIR}")
        print(f"\nNote: ruTorrent has minimal markdown documentation available")

        return len(md_files) > 0

    finally:
        # Clean temp directory
        if TEMP_DIR.exists():
            shutil.rmtree(TEMP_DIR)

if __name__ == "__main__":
    success = extract_rutorrent_docs()
    exit(0 if success else 1)
