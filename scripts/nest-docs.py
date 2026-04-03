#!/usr/bin/env python3
"""
NestJS Documentation Scraper
Downloads NestJS documentation from GitHub repository and converts to markdown.
NestJS is a progressive Node.js framework for building efficient, reliable, and scalable server-side applications.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
import time
import tempfile

# GitHub repository details
REPO_URL = "https://github.com/nestjs/docs.nestjs.com.git"
REPO_BRANCH = "master"
DOC_DIR = "content"


def clone_repo(temp_dir):
    """Clone the NestJS documentation repository."""
    try:
        print(f"Cloning repository from {REPO_URL}")
        print("This may take a minute...")

        result = subprocess.run(
            [
                "git", "clone",
                "--depth", "1",
                "--single-branch",
                "--branch", REPO_BRANCH,
                REPO_URL,
                str(temp_dir)
            ],
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode != 0:
            print(f"Error cloning repository: {result.stderr}")
            return False

        print(f"Repository cloned successfully")
        return True

    except subprocess.TimeoutExpired:
        print("Error: Git clone timed out")
        return False
    except Exception as e:
        print(f"Error cloning repository: {e}")
        return False


def copy_markdown_files(source_dir, output_dir):
    """Copy all markdown files from source to output directory."""
    source_path = Path(source_dir) / DOC_DIR
    if not source_path.exists():
        print(f"Error: Documentation directory not found: {source_path}")
        return 0, 0

    successful = 0
    failed = 0

    # Also copy README from root
    readme_path = Path(source_dir) / "README.md"
    if readme_path.exists():
        output_file = output_dir / "main-README.md"
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Add metadata header
            header = f"""# NestJS Documentation
# Source: {REPO_URL}
# Path: README.md

"""
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(header + content)

            print(f"  Copied: README.md -> main-README.md")
            successful += 1
        except Exception as e:
            print(f"  Error copying README.md: {e}")
            failed += 1

    # Get all markdown files from content directory
    md_files = list(source_path.rglob("*.md"))
    print(f"\nFound {len(md_files)} markdown files in {DOC_DIR}/")
    print()

    for idx, md_file in enumerate(sorted(md_files), 1):
        try:
            # Get relative path from content directory
            relative_path = md_file.relative_to(source_path)

            # Create output filename by replacing path separators with dashes
            output_filename = str(relative_path).replace(os.sep, "-")

            output_file = output_dir / output_filename

            # Read source file
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Add metadata header
            repo_path = f"{DOC_DIR}/{relative_path}"
            source_url = f"https://github.com/nestjs/docs.nestjs.com/blob/{REPO_BRANCH}/{repo_path}"
            header = f"""# NestJS Documentation
# Source: {source_url}
# Path: {repo_path}

"""

            # Write to output file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(header + content)

            print(f"  [{idx:3d}/{len(md_files)}] {relative_path} -> {output_filename}")
            successful += 1

        except Exception as e:
            print(f"  Error copying {md_file}: {e}")
            failed += 1

    return successful, failed


def main():
    """Main function to download all NestJS documentation."""
    print("=" * 60)
    print("NestJS Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "nest"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Create temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / "nestjs-docs"

        # Clone repository
        if not clone_repo(temp_path):
            print("Failed to clone repository")
            sys.exit(1)

        print()

        # Copy markdown files
        start_time = time.time()
        successful, failed = copy_markdown_files(temp_path, output_dir)
        elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} files failed to copy")
        sys.exit(1)
    else:
        print("All documentation downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
