#!/usr/bin/env python3
"""
DocETL Documentation Extractor
Downloads DocETL documentation from GitHub repository.
DocETL is an open-source framework for document extraction and transformation.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/UCBepic/docetl.git"
REPO_BRANCH = "main"
SOURCE_DOCS_FOLDER = "docs"  # DocETL stores documentation in docs/


def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "docetl"

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
        docs_source = Path(source_dir) / SOURCE_DOCS_FOLDER

        if not docs_source.exists():
            print(f"    -> Documentation folder not found: {docs_source}")
            return False

        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        # Copy all files recursively
        file_count = 0
        for item in docs_source.rglob("*"):
            if item.is_file():
                relative_path = item.relative_to(docs_source)
                dest = output_dir / relative_path

                # Create parent directories if needed
                dest.parent.mkdir(parents=True, exist_ok=True)

                # Handle markdown and other text files
                if item.suffix in [".md", ".txt"]:
                    with open(item, 'r', encoding='utf-8', errors='ignore') as f:
                        original_content = f.read()

                    # Add source header to text files
                    source_url = f"https://github.com/UCBepic/docetl/blob/{REPO_BRANCH}/{SOURCE_DOCS_FOLDER}/{relative_path}"
                    header = f"""# Source: {source_url}

"""

                    with open(dest, 'w', encoding='utf-8') as f:
                        f.write(header)
                        f.write(original_content)
                    file_count += 1
                else:
                    # Copy non-text files as-is
                    shutil.copy2(item, dest)

        print(f"    -> Documentation copied successfully ({file_count} files)")
        return True

    except Exception as e:
        print(f"    -> Error copying documentation: {e}")
        return False


def main():
    """Main function to extract DocETL documentation."""
    print(f"Extracting DocETL documentation from GitHub")

    # Get script directory
    script_dir = Path(__file__).resolve().parent
    output_dir = script_dir.parent / "docs" / "github-scraped" / "docetl"

    # Create temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        # Clone repository
        repo_path = clone_repository(temp_dir, REPO_URL, REPO_BRANCH)
        if not repo_path:
            print(f"Failed to clone repository")
            return False

        # Copy documentation
        if not copy_documentation(repo_path, output_dir):
            print(f"Failed to copy documentation")
            return False

    print(f"Successfully extracted documentation to {output_dir}")
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
