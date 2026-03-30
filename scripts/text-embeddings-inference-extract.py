#!/usr/bin/env python3
"""
Text Embeddings Inference Documentation Extractor
Clones the huggingface/text-embeddings-inference repository and extracts the docs.
Text Embeddings Inference is a high-performance inference server for text embeddings,
re-ranking, and sequence classification with optimized batching and quantization.
"""

import os
import sys
import subprocess
import shutil
import tempfile
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "text-embeddings-inference"


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


def clone_and_extract():
    """Clone the Text Embeddings Inference repository and extract documentation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "text-embeddings-inference"
        print(f"Cloning huggingface/text-embeddings-inference repository to {repo_path}...")

        returncode, stdout, stderr = run_command(
            f"git clone --depth 1 --branch main https://github.com/huggingface/text-embeddings-inference.git {repo_path}",
            timeout=300
        )

        if returncode != 0:
            print(f"Error cloning repository: {stderr}")
            return False

        # Source documentation folder
        src_docs = repo_path / "docs" / "source" / "en"

        if not src_docs.exists():
            print(f"Documentation folder not found at {src_docs}")
            return False

        print(f"Found documentation at {src_docs}")
        print(f"Extracting to {OUTPUT_DIR}...")

        # Remove existing output directory if it exists
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)

        # Copy the documentation folder
        shutil.copytree(src_docs, OUTPUT_DIR)

        # Get file count and size
        files = list(OUTPUT_DIR.glob("**/*"))
        md_files = list(OUTPUT_DIR.glob("**/*.md"))
        total_size = sum(f.stat().st_size for f in files if f.is_file())

        print(f"Success! Extracted {len(md_files)} markdown files")
        print(f"Total size: {total_size / 1024 / 1024:.2f} MB")
        print(f"Output: {OUTPUT_DIR}")

        return True


def main():
    success = clone_and_extract()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
