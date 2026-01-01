#!/usr/bin/env python3
"""
ROCm Documentation Extractor

Extracts ROCm documentation from the ROCm GitHub repository.
ROCm is AMD's open-source compute platform for GPU acceleration.
"""

import os
import sys
import subprocess
import shutil
import tempfile
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "rocm"


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


def clone_rocm_repo():
    """Clone the ROCm repository and extract documentation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "rocm"
        print(f"Cloning ROCm/ROCm repository to {repo_path}...")

        returncode, stdout, stderr = run_command(
            f"git clone --depth 1 --branch develop https://github.com/ROCm/ROCm.git {repo_path}",
            timeout=300
        )

        if returncode != 0:
            print(f"Error cloning repository: {stderr}")
            return False

        # Check if docs folder exists
        docs_src = repo_path / "docs"
        if not docs_src.exists():
            print(f"Warning: docs folder not found at {docs_src}")
            print("Checking for alternative documentation locations...")

            # Check for alternative docs locations
            alt_docs = [
                repo_path / "doc",
                repo_path / "documentation",
                repo_path / "README.md",
            ]

            for alt_path in alt_docs:
                if alt_path.exists():
                    print(f"Found alternative at {alt_path}")
                    docs_src = alt_path
                    break
            else:
                print("No documentation folder found")
                return False

        print(f"Extracting documentation from {docs_src}...")

        # Remove output directory if it exists
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)

        # Copy docs folder
        if docs_src.is_file():
            # If it's a single file (README), create directory and copy it
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            shutil.copy2(docs_src, OUTPUT_DIR / docs_src.name)
        else:
            # If it's a directory, copy the whole directory
            shutil.copytree(docs_src, OUTPUT_DIR)

        print(f"Extracted documentation to {OUTPUT_DIR}")

        # Count files
        md_files = list(OUTPUT_DIR.glob("**/*.md"))
        rst_files = list(OUTPUT_DIR.glob("**/*.rst"))
        total_files = md_files + rst_files

        print(f"Total markdown files: {len(md_files)}")
        print(f"Total RST files: {len(rst_files)}")
        print(f"Total documentation files: {len(total_files)}")

        return True


def main():
    """Main function."""
    print("=" * 70)
    print("ROCm Documentation Extractor")
    print("=" * 70)
    print()

    success = clone_rocm_repo()

    if success:
        print()
        print("=" * 70)
        print("Extraction Summary")
        print("=" * 70)

        # Calculate total size
        total_size = 0
        for f in OUTPUT_DIR.glob("**/*"):
            if f.is_file():
                total_size += f.stat().st_size

        print(f"Output directory: {OUTPUT_DIR}")
        print(f"Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")

        # List sample files
        files = list(OUTPUT_DIR.glob("**/*.md"))[:20]
        if files:
            print(f"\nSample files (showing {len(files)} of {len(list(OUTPUT_DIR.glob('**/*')))}):")
            for f in sorted(files):
                rel_path = f.relative_to(OUTPUT_DIR)
                print(f"  - {rel_path}")

        print()
        print("ROCm documentation extracted successfully!")
        return 0
    else:
        print()
        print("Failed to extract ROCm documentation.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
