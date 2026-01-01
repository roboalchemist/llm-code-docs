#!/usr/bin/env python3
"""
Hugging Face Diffusers Documentation Extractor
Clones the huggingface/diffusers repository and extracts the docs/source folder.
Diffusers is a library for generating images, audio, and 3D objects with diffusion models.
"""

import os
import sys
import subprocess
import shutil
import tempfile
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "huggingface-diffusers"


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


def clone_diffusers_repo():
    """Clone the Hugging Face Diffusers repository and extract documentation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "diffusers"
        print(f"Cloning huggingface/diffusers repository to {repo_path}...")

        returncode, stdout, stderr = run_command(
            f"git clone --depth 1 --branch main https://github.com/huggingface/diffusers.git {repo_path}",
            timeout=300
        )

        if returncode != 0:
            print(f"Error cloning repository: {stderr}")
            return False

        print(f"Cloned successfully. Extracting documentation...")

        # Remove output directory if it exists
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)

        # Copy docs/source folder
        docs_src = repo_path / "docs" / "source"
        if not docs_src.exists():
            print(f"Error: docs/source folder not found at {docs_src}")
            return False

        shutil.copytree(docs_src, OUTPUT_DIR)
        print(f"Extracted docs/source to {OUTPUT_DIR}")

        # Also copy the main README
        readme_src = repo_path / "README.md"
        if readme_src.exists():
            shutil.copy2(readme_src, OUTPUT_DIR / "README.md")
            print(f"Extracted: README.md")

        # Count files
        all_files = list(OUTPUT_DIR.glob("**/*"))
        md_files = list(OUTPUT_DIR.glob("**/*.md"))

        print(f"Total files extracted: {len([f for f in all_files if f.is_file()])}")
        print(f"  - Markdown files: {len(md_files)}")

        return True


def main():
    """Main function."""
    print("=" * 70)
    print("Hugging Face Diffusers Documentation Extractor")
    print("=" * 70)

    success = clone_diffusers_repo()

    if success:
        print("\nHugging Face Diffusers documentation extracted successfully!")
        return 0
    else:
        print("\nFailed to extract Hugging Face Diffusers documentation.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
