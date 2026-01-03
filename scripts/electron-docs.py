#!/usr/bin/env python3
"""
Electron Documentation Extractor
Clones the electron/electron repository and extracts the docs folder.
Electron is a framework for building cross-platform desktop applications using web technologies.
"""

import os
import sys
import subprocess
import shutil
import tempfile
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "electron"


def run_command(cmd, cwd=None, timeout=300):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        print(f"Command timed out after {timeout} seconds: {cmd}")
        return 1, "", "Timeout"


def clone_electron_repo():
    """Clone the electron repository."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "electron"
        print(f"Cloning electron/electron repository to {repo_path}...")
        
        returncode, stdout, stderr = run_command(
            f"git clone --depth 1 --branch main https://github.com/electron/electron.git {repo_path}",
            timeout=300
        )
        
        if returncode != 0:
            print(f"Error cloning repository: {stderr}")
            return False
        
        # Check if docs folder exists
        docs_src = repo_path / "docs"
        if not docs_src.exists():
            print(f"Error: docs folder not found at {docs_src}")
            return False
        
        print(f"Cloned successfully. Extracting docs from {docs_src}...")
        
        # Remove output directory if it exists
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)
        
        # Copy docs folder
        shutil.copytree(docs_src, OUTPUT_DIR)
        print(f"Extracted docs to {OUTPUT_DIR}")
        
        # Count files
        md_files = list(OUTPUT_DIR.glob("**/*.md"))
        print(f"Total markdown files: {len(md_files)}")
        
        return True


def main():
    """Main function."""
    print("=" * 70)
    print("Electron Documentation Extractor")
    print("=" * 70)
    
    success = clone_electron_repo()
    
    if success:
        print("\nElectron documentation extracted successfully!")
        return 0
    else:
        print("\nFailed to extract Electron documentation.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
