#!/usr/bin/env python3
"""
Matter SDK (connectedhomeip) Documentation Extractor
Downloads Matter SDK documentation from the official Project CHIP repository.
The Matter SDK is the official C++ implementation of the Matter smart home protocol.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess

# Repository configuration
REPO_URL = "https://github.com/project-chip/connectedhomeip.git"
REPO_BRANCH = "master"
SOURCE_DOCS_FOLDER = "docs"

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "connectedhomeip"

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
    """Copy documentation from source to output directory."""
    try:
        print(f"  Copying documentation from {source_dir}")

        if not source_dir.exists():
            print(f"    -> Source directory not found: {source_dir}")
            return False

        # Create output directory if it doesn't exist
        output_dir.mkdir(parents=True, exist_ok=True)

        # Copy all files from source to output
        for item in source_dir.rglob('*'):
            if item.is_file():
                # Skip build-related and config files
                if item.name in ['Doxyfile', '.envrc', 'Makefile', 'make.bat', 'conf.py', 'requirements.txt']:
                    continue
                if item.suffix in ['.xml', '.py', '.sh', '.bat']:
                    # Skip config and build files
                    if item.parent.name not in ['_extensions']:
                        continue

                # Calculate relative path
                rel_path = item.relative_to(source_dir)
                dest_file = output_dir / rel_path

                # Create parent directories
                dest_file.parent.mkdir(parents=True, exist_ok=True)

                # Copy file
                shutil.copy2(item, dest_file)

        print(f"    -> Documentation copied successfully")
        return True

    except Exception as e:
        print(f"    -> Error copying documentation: {e}")
        return False


def extract_matter_sdk_docs():
    """Main extraction function."""
    print("Extracting Matter SDK (connectedhomeip) documentation...")

    # Create temp directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Clone repository
        repo_path = clone_repository(temp_dir, REPO_URL, REPO_BRANCH)
        if not repo_path:
            print("Failed to clone repository")
            return False

        # Source and output directories
        source_dir = repo_path / SOURCE_DOCS_FOLDER
        output_dir = Path(__file__).parent.parent / "docs" / "github-scraped" / "matter-sdk"

        # Copy documentation
        if not copy_documentation(source_dir, output_dir):
            print("Failed to copy documentation")
            return False

        # Verify output
        if output_dir.exists() and list(output_dir.rglob('*')):
            file_count = len(list(output_dir.rglob('*')))
            print(f"\nSuccess! Matter SDK documentation extracted:")
            print(f"  Location: {output_dir}")
            print(f"  Files: {file_count}")
            return True
        else:
            print("No files were copied")
            return False


if __name__ == "__main__":
    success = extract_matter_sdk_docs()
    sys.exit(0 if success else 1)
