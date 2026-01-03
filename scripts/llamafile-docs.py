#!/usr/bin/env python3
"""
Llamafile Documentation Extractor
Clones the mozilla-ai/llamafile repository and extracts the docs folder.
Llamafile is a Mozilla project for single-file executables for running LLMs locally without dependencies.
"""

import os
import sys
import subprocess
import shutil
import tempfile
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "llamafile"


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


def clone_llamafile_repo():
    """Clone the llamafile repository and extract documentation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "llamafile"
        print(f"Cloning mozilla-ai/llamafile repository to {repo_path}...")

        returncode, stdout, stderr = run_command(
            f"git clone --depth 1 --branch main https://github.com/mozilla-ai/llamafile.git {repo_path}",
            timeout=600
        )

        if returncode != 0:
            print(f"Error cloning repository: {stderr}")
            return False

        # Check if docs folder exists
        docs_dir = repo_path / "docs"
        if not docs_dir.exists():
            print(f"Error: docs folder not found at {docs_dir}")
            return False

        print(f"Cloned successfully. Extracting docs from {docs_dir}...")

        # Remove output directory if it exists
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)

        # Copy docs folder
        shutil.copytree(docs_dir, OUTPUT_DIR)
        print(f"Extracted docs to {OUTPUT_DIR}")

        # Count files
        md_files = list(OUTPUT_DIR.glob("**/*.md"))
        print(f"Total markdown files: {len(md_files)}")

        return True


def main():
    """Main function."""
    print("=" * 70)
    print("Llamafile Documentation Extractor")
    print("=" * 70)

    success = clone_llamafile_repo()

    if success:
        print("\n" + "=" * 70)
        print("Llamafile documentation extraction completed successfully!")
        print("=" * 70)
        return 0
    else:
        print("\n" + "=" * 70)
        print("Llamafile documentation extraction failed!")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    sys.exit(main())
