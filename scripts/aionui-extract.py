#!/usr/bin/env python3
"""
AionUi Documentation Extractor
Downloads documentation from the AionUi GitHub repository.
Extracts README, WEBUI_GUIDE, and all other documentation files.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/iOfficeAI/AionUi.git"
REPO_BRANCH = "main"

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "aionui"

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

        # Files and directories to extract
        files_to_copy = [
            "README.md",
            "WEBUI_GUIDE.md",
            "CODE_STYLE.md",
            "LICENSE"
        ]

        dirs_to_copy = [
            "docs",
            ".github"
        ]

        # Copy specific files
        for file_name in files_to_copy:
            file_path = Path(source_dir) / file_name
            if file_path.exists():
                dest_path = output_dir / file_name
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    original_content = f.read()

                # Add source header
                source_url = f"https://github.com/iOfficeAI/AionUi/blob/{REPO_BRANCH}/{file_name}"
                header = f"""# Source: {source_url}

"""
                new_content = header + original_content

                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"    -> Copied file: {file_name}")

        # Copy directories
        for dir_name in dirs_to_copy:
            dir_path = Path(source_dir) / dir_name
            if dir_path.exists() and dir_path.is_dir():
                dest_path = output_dir / dir_name
                if dest_path.exists():
                    shutil.rmtree(dest_path)
                shutil.copytree(dir_path, dest_path)
                print(f"    -> Copied directory: {dir_name}/")

        return True

    except Exception as e:
        print(f"    -> Error copying documentation: {e}")
        return False


def main():
    """Main function to extract AionUi documentation."""
    print("=" * 70)
    print("AionUi Documentation Extractor")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "aionui"

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

    # Count files
    all_files = list(output_dir.rglob("*"))
    file_count = sum(1 for f in all_files if f.is_file())
    total_size = sum(f.stat().st_size for f in all_files if f.is_file())

    md_files = list(output_dir.glob("*.md"))

    print(f"  Total files: {file_count}")
    print(f"  Total markdown files: {len(md_files)}")
    print(f"  Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")

    # List main files
    print("\n  Main documentation files:")
    for file_path in sorted(all_files):
        if file_path.is_file() and (file_path.suffix in ['.md', '.txt'] or file_path.name == 'LICENSE'):
            file_size = file_path.stat().st_size
            rel_path = file_path.relative_to(output_dir)
            print(f"    - {rel_path} ({file_size:,} bytes)")

    print()
    print("=" * 70)
    print("Extraction Complete")
    print("=" * 70)
    print(f"Output: {output_dir}")
    print()


if __name__ == "__main__":
    main()
