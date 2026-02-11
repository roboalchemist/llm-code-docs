#!/usr/bin/env python3
"""
Terraform Cloud Documentation Extractor
Downloads Terraform Cloud (HCP Terraform) documentation from HashiCorp's web-unified-docs repository.
Terraform Cloud provides remote state management, run environments, VCS integration, policy enforcement, and team collaboration.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/hashicorp/web-unified-docs.git"
REPO_BRANCH = "main"
SOURCE_DOCS_FOLDER = "content/terraform-docs-common/docs/cloud-docs"

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "terraform-cloud"

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

        # Copy all markdown files and subdirectories
        for item in docs_source.iterdir():
            dest = output_dir / item.name

            if item.is_dir():
                # Skip specific directories if needed
                if item.name in ["img", "images", ".git"]:
                    print(f"    -> Skipping {item.name}/ directory")
                    continue
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(item, dest)
                print(f"    -> Copied directory: {item.name}/")
            elif item.is_file() and item.suffix in [".md", ".mdx"]:
                # Add source header to markdown files
                with open(item, 'r', encoding='utf-8') as f:
                    original_content = f.read()

                # Add source information header
                source_url = f"https://github.com/hashicorp/web-unified-docs/blob/{REPO_BRANCH}/{SOURCE_DOCS_FOLDER}/{item.name}"
                header = f"""# Source: {source_url}

"""
                new_content = header + original_content

                with open(dest, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"    -> Copied file: {item.name}")
            elif item.is_file():
                # Copy non-markdown files too (like images, etc)
                if dest.exists():
                    dest.unlink()
                shutil.copy2(item, dest)

        return True

    except Exception as e:
        print(f"    -> Error copying documentation: {e}")
        return False


def main():
    """Main function to extract Terraform Cloud documentation."""
    print("=" * 70)
    print("Terraform Cloud Documentation Extractor")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "terraform-cloud"

    print(f"Repository: {REPO_URL}")
    print(f"Branch: {REPO_BRANCH}")
    print(f"Source folder: {SOURCE_DOCS_FOLDER}")
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

    # Count markdown files including subdirectories
    md_files = list(output_dir.glob("**/*.md")) + list(output_dir.glob("**/*.mdx"))
    total_size = sum(f.stat().st_size for f in output_dir.rglob("*") if f.is_file())

    print(f"  Total markdown files: {len(md_files)}")
    print(f"  Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")

    if len(md_files) == 0:
        print("\n  Warning: No markdown files found in output directory")
        sys.exit(1)

    # List main files
    print("\n  Main documentation files:")
    for md_file in sorted(md_files)[:10]:
        file_size = md_file.stat().st_size
        relative_path = md_file.relative_to(output_dir)
        print(f"    - {relative_path} ({file_size:,} bytes)")

    if len(md_files) > 10:
        print(f"    ... and {len(md_files) - 10} more files")

    print()
    print("=" * 70)
    print("Extraction Complete")
    print("=" * 70)
    print(f"Output: {output_dir}")
    print()


if __name__ == "__main__":
    main()
