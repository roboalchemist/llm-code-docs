#!/usr/bin/env python3
"""
OpenBambuAPI Documentation Extractor
Downloads OpenBambuAPI documentation from GitHub repository.
OpenBambuAPI is a community-maintained reverse-engineered documentation project
for Bambu Lab 3D printer communication protocols (MQTT, HTTP, FTP, G-code, video, TLS).
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/Doridian/OpenBambuAPI.git"
REPO_BRANCH = "main"
SOURCE_DOCS_FOLDER = "."

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "openbambuapi"

        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", branch, repo_url, str(clone_path)],
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode != 0:
            print(f"    -> Error cloning repository: {result.stderr}")
            return None

        print(f"    -> Repository cloned successfully")
        return clone_path

    except subprocess.TimeoutExpired:
        print(f"    -> Timeout cloning repository")
        return None
    except Exception as e:
        print(f"    -> Error cloning repository: {e}")
        return None


def copy_documentation(source_dir, output_dir):
    """Copy documentation files from source to output directory."""
    try:
        print(f"  Copying documentation files...")

        # Create output directory if it doesn't exist
        output_dir.mkdir(parents=True, exist_ok=True)

        # Copy markdown files
        markdown_files = list(source_dir.glob("*.md"))
        if markdown_files:
            for md_file in markdown_files:
                shutil.copy2(md_file, output_dir / md_file.name)
            print(f"    -> Copied {len(markdown_files)} markdown files")

        # Also copy examples folder if it exists
        examples_dir = source_dir / "examples"
        if examples_dir.exists():
            target_examples = output_dir / "examples"
            if target_examples.exists():
                shutil.rmtree(target_examples)
            shutil.copytree(examples_dir, target_examples)
            print(f"    -> Copied examples folder")

        return True

    except Exception as e:
        print(f"    -> Error copying documentation: {e}")
        return False


def main():
    """Main function to extract OpenBambuAPI documentation."""
    print("\nOpenBambuAPI Documentation Extractor")
    print("=" * 50)

    # Define output directory
    output_dir = Path(__file__).parent.parent / "docs" / "github-scraped" / "openbambuapi"

    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"\nUsing temporary directory: {temp_dir}")

        # Clone repository
        clone_path = clone_repository(temp_dir, REPO_URL, REPO_BRANCH)
        if not clone_path:
            print("\nFailed to clone repository")
            return 1

        # Find source documentation folder
        source_docs = clone_path / SOURCE_DOCS_FOLDER
        if not source_docs.exists():
            print(f"\nSource documentation folder not found: {source_docs}")
            return 1

        # Remove existing output directory
        if output_dir.exists():
            print(f"\nRemoving existing output directory: {output_dir}")
            shutil.rmtree(output_dir)

        # Copy documentation
        if not copy_documentation(source_docs, output_dir):
            print("\nFailed to copy documentation")
            return 1

    print(f"\nDocumentation successfully extracted to: {output_dir}")

    # Verify extraction
    md_files = list(output_dir.glob("*.md"))
    print(f"Total markdown files: {len(md_files)}")
    if md_files:
        print("Files:")
        for f in sorted(md_files):
            size = f.stat().st_size
            print(f"  - {f.name} ({size:,} bytes)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
