#!/usr/bin/env python3
"""
Swift Documentation Extractor
Downloads The Swift Programming Language documentation from the official GitHub repository.
The Swift Programming Language is the official Apple documentation covering language guide,
syntax, standard library, and reference manual.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/swiftlang/swift-book.git"
REPO_BRANCH = "main"
SOURCE_DOCS_FOLDER = "TSPL.docc"

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "swift-book"

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
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        docs_source = Path(source_dir) / SOURCE_DOCS_FOLDER

        if not docs_source.exists():
            print(f"    -> Docs folder not found: {docs_source}")
            return False

        files_copied = 0

        # Copy all markdown files from TSPL.docc folder
        for md_file in docs_source.rglob("*.md"):
            relative_path = md_file.relative_to(docs_source)
            output_file = output_dir / relative_path

            # Create subdirectories if needed
            output_file.parent.mkdir(parents=True, exist_ok=True)

            try:
                with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                # Add source header
                source_url = f"https://github.com/swiftlang/swift-book/blob/{REPO_BRANCH}/TSPL.docc/{relative_path}"
                header = f"""# Source: {source_url}

"""
                final_content = header + content

                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(final_content)

                print(f"    -> Copied {relative_path} ({len(final_content)} bytes)")
                files_copied += 1

            except Exception as e:
                print(f"    -> Error copying {relative_path}: {e}")

        if files_copied > 0:
            print(f"  Successfully copied {files_copied} documentation files")
            return True
        else:
            print(f"  No documentation files were copied")
            return False

    except Exception as e:
        print(f"  Error copying documentation: {e}")
        return False


def main():
    """Main extraction process."""
    try:
        print("Extracting Swift documentation...")

        # Create temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Clone repository
            repo_path = clone_repository(temp_dir, REPO_URL, REPO_BRANCH)

            if not repo_path:
                print("Failed to clone repository")
                return False

            # Define output directory
            output_dir = Path(__file__).parent.parent / "docs" / "github-scraped" / "swift"

            # Copy documentation
            if copy_documentation(repo_path, output_dir):
                print(f"\nDocumentation extracted to: {output_dir}")
                return True
            else:
                print("Failed to extract documentation")
                return False

    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
