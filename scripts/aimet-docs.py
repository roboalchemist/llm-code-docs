#!/usr/bin/env python3
"""
AIMET Documentation Extractor
Clones the quic/aimet repository and extracts the Docs folder.
AIMET is Qualcomm's AI Model Efficiency Toolkit for quantization and compression.
"""

import os
import sys
import subprocess
import shutil
import tempfile
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "aimet"


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


def clone_aimet_repo():
    """Clone the AIMET repository and extract documentation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "aimet"
        print(f"Cloning quic/aimet repository to {repo_path}...")

        returncode, stdout, stderr = run_command(
            f"git clone --depth 1 --branch develop https://github.com/quic/aimet.git {repo_path}",
            timeout=600
        )

        if returncode != 0:
            print(f"Error cloning repository: {stderr}")
            return False

        # Check if Docs folder exists
        docs_folder = repo_path / "Docs"
        if not docs_folder.exists():
            print(f"Error: Docs folder not found at {docs_folder}")
            return False

        print(f"Cloned successfully. Extracting docs from {docs_folder}...")

        # Remove output directory if it exists
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)

        # Copy Docs folder
        shutil.copytree(docs_folder, OUTPUT_DIR)
        print(f"Extracted docs to {OUTPUT_DIR}")

        # Count files
        md_files = list(OUTPUT_DIR.glob("**/*.md"))
        rst_files = list(OUTPUT_DIR.glob("**/*.rst"))
        html_files = list(OUTPUT_DIR.glob("**/*.html"))
        print(f"Total markdown files: {len(md_files)}")
        print(f"Total RST files: {len(rst_files)}")
        print(f"Total HTML files: {len(html_files)}")

        return True


def main():
    """Main function."""
    print("=" * 70)
    print("AIMET Documentation Extractor")
    print("=" * 70)

    success = clone_aimet_repo()

    if success:
        print("\n" + "=" * 70)
        print("AIMET documentation extraction completed successfully!")
        print("=" * 70)
        return 0
    else:
        print("\n" + "=" * 70)
        print("AIMET documentation extraction failed!")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    sys.exit(main())
