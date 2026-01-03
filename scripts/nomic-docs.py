#!/usr/bin/env python3
"""
Nomic Documentation Extractor
Clones the nomic-ai/nomic repository and extracts the docs folder.
Nomic provides open-source embedding models and data exploration tools for LLM applications.
"""

import os
import sys
import subprocess
import shutil
import tempfile
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "nomic"


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


def clone_nomic_repo():
    """Clone the nomic repository."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "nomic"
        print(f"Cloning nomic-ai/nomic repository to {repo_path}...")

        returncode, stdout, stderr = run_command(
            f"git clone --depth 1 --branch main https://github.com/nomic-ai/nomic.git {repo_path}",
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
        ipynb_files = list(OUTPUT_DIR.glob("**/*.ipynb"))
        print(f"Total markdown files: {len(md_files)}")
        print(f"Total notebook files: {len(ipynb_files)}")

        return True


def main():
    """Main function."""
    print("=" * 70)
    print("Nomic Documentation Extractor")
    print("=" * 70)

    success = clone_nomic_repo()

    if success:
        print("\nNomic documentation extracted successfully!")
        return 0
    else:
        print("\nFailed to extract Nomic documentation.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
