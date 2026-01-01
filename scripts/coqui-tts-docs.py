#!/usr/bin/env python3
"""
Coqui TTS Documentation Extractor
Clones the coqui-ai/TTS repository and extracts the docs/source folder.
Coqui TTS is an open-source text-to-speech library with multiple models
supporting multiple languages.
"""

import os
import sys
import subprocess
import shutil
import tempfile
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "coqui-tts"


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


def clone_coqui_tts_repo():
    """Clone the Coqui TTS repository and extract documentation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "coqui-tts"
        print(f"Cloning coqui-ai/TTS repository to {repo_path}...")

        returncode, stdout, stderr = run_command(
            f"git clone --depth 1 --branch dev https://github.com/coqui-ai/TTS.git {repo_path}",
            timeout=600
        )

        if returncode != 0:
            print(f"Error cloning repository: {stderr}")
            return False

        # Check if docs/source folder exists
        docs_src = repo_path / "docs" / "source"
        if not docs_src.exists():
            print(f"Error: docs/source folder not found at {docs_src}")
            return False

        print(f"Cloned successfully. Extracting docs from {docs_src}...")

        # Remove output directory if it exists
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)

        # Copy docs/source folder
        shutil.copytree(docs_src, OUTPUT_DIR)
        print(f"Extracted docs to {OUTPUT_DIR}")

        # Count files
        md_files = list(OUTPUT_DIR.glob("**/*.md"))
        rst_files = list(OUTPUT_DIR.glob("**/*.rst"))
        print(f"Total markdown files: {len(md_files)}")
        print(f"Total RST files: {len(rst_files)}")

        return True


def main():
    """Main function."""
    print("=" * 70)
    print("Coqui TTS Documentation Extractor")
    print("=" * 70)

    success = clone_coqui_tts_repo()

    if success:
        print("\n" + "=" * 70)
        print("Coqui TTS documentation extraction completed successfully!")
        print("=" * 70)
        return 0
    else:
        print("\n" + "=" * 70)
        print("Coqui TTS documentation extraction failed!")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    sys.exit(main())
