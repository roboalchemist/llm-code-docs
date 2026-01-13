#!/usr/bin/env python3
"""
golangci-lint Documentation Extractor
Downloads golangci-lint documentation from GitHub repository.
golangci-lint is a meta-linter aggregating 50+ linters for Go with
parallel execution and caching.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/golangci/golangci-lint.git"
REPO_BRANCH = "master"
SOURCE_DOCS_FOLDER = "docs/src/docs"


def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "golangci-lint"

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

        # Copy all markdown, mdx, and other documentation files from docs folder
        for doc_file in docs_source.rglob("*"):
            if doc_file.is_file() and doc_file.suffix in ['.md', '.mdx', '.html', '.yml', '.yaml']:
                relative_path = doc_file.relative_to(docs_source)
                output_file = output_dir / relative_path

                # Create subdirectories if needed
                output_file.parent.mkdir(parents=True, exist_ok=True)

                try:
                    with open(doc_file, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()

                    # Add source header for markdown files
                    if doc_file.suffix in ['.md', '.mdx']:
                        source_url = f"https://github.com/golangci/golangci-lint/blob/{REPO_BRANCH}/docs/src/docs/{relative_path}"
                        header = f"""# Source: {source_url}

"""
                        final_content = header + content
                    else:
                        final_content = content

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
        print("=" * 60)
        print("golangci-lint Documentation Extractor")
        print("=" * 60)
        print()

        # Create temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Clone repository
            repo_path = clone_repository(temp_dir, REPO_URL, REPO_BRANCH)

            if not repo_path:
                print("Failed to clone repository")
                return False

            # Define output directory
            output_dir = Path(__file__).parent.parent / "docs" / "github-scraped" / "golangci-lint"

            # Copy documentation
            if copy_documentation(repo_path, output_dir):
                print(f"\nDocumentation extracted to: {output_dir}")

                # Calculate total size
                total_size = sum(f.stat().st_size for f in output_dir.rglob("*") if f.is_file())
                print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

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
