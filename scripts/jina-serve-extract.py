#!/usr/bin/env python3
"""
Jina Serve Documentation Extractor
Downloads Jina Serve Framework documentation from GitHub repository.
Jina Serve is a framework for building and deploying multimodal AI services with gRPC, HTTP, and WebSocket support.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/jina-ai/serve.git"
REPO_BRANCH = "master"
SOURCE_DOCS_FOLDER = "docs"

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "jina-serve"

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

        # Copy all files recursively, converting RST to Markdown where applicable
        for item in docs_source.rglob("*"):
            if item.is_file():
                relative_path = item.relative_to(docs_source)
                dest = output_dir / relative_path

                # Create parent directories if needed
                dest.parent.mkdir(parents=True, exist_ok=True)

                # Handle markdown and other text files
                if item.suffix in [".md", ".rst", ".txt", ".py"]:
                    with open(item, 'r', encoding='utf-8', errors='ignore') as f:
                        original_content = f.read()

                    # Add source header to text files
                    source_url = f"https://github.com/jina-ai/serve/blob/{REPO_BRANCH}/{SOURCE_DOCS_FOLDER}/{relative_path}"
                    header = f"""# Source: {source_url}

"""
                    new_content = header + original_content

                    with open(dest, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"    -> Copied file: {relative_path}")
                else:
                    # Copy binary files as-is
                    shutil.copy2(item, dest)

        return True

    except Exception as e:
        print(f"    -> Error copying documentation: {e}")
        return False


def main():
    """Main function to extract Jina Serve documentation."""
    print("=" * 70)
    print("Jina Serve Documentation Extractor")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "jina-serve"

    print(f"Repository: {REPO_URL}")
    print(f"Branch: {REPO_BRANCH}")
    print(f"Output directory: {output_dir}")
    print()

    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Clone repository
        print("Cloning repository...")
        repo_path = clone_repository(temp_dir, REPO_URL, REPO_BRANCH)

        if not repo_path:
            print("\nError: Failed to clone repository")
            sys.exit(1)

        # Copy documentation
        print("\nCopying documentation files...")

        # Remove existing output directory if it exists
        if output_dir.exists():
            print(f"  Removing existing output directory: {output_dir}")
            shutil.rmtree(output_dir)

        if not copy_documentation(repo_path, output_dir):
            print("\nError: Failed to copy documentation")
            sys.exit(1)

    # Verify extraction
    print("\nVerifying extraction...")
    if not output_dir.exists():
        print("  Error: Output directory was not created")
        sys.exit(1)

    text_files = list(output_dir.glob("**/*"))
    text_files = [f for f in text_files if f.is_file()]
    total_size = sum(f.stat().st_size for f in text_files)

    print(f"  Total files: {len(text_files)}")
    print(f"  Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")

    if len(text_files) == 0:
        print("\n  Warning: No files found in output directory")
        sys.exit(1)

    # List main files
    print("\n  Main documentation files:")
    for text_file in sorted(text_files)[:10]:
        file_size = text_file.stat().st_size
        print(f"    - {text_file.relative_to(output_dir)} ({file_size:,} bytes)")

    if len(text_files) > 10:
        print(f"    ... and {len(text_files) - 10} more files")

    print()
    print("=" * 70)
    print("Extraction Complete")
    print("=" * 70)
    print(f"Output: {output_dir}")
    print()


if __name__ == "__main__":
    main()
