#!/usr/bin/env python3
"""
BigCommerce API Documentation Extractor

Downloads BigCommerce e-commerce platform API documentation from GitHub repository.
BigCommerce API documentation covers REST and GraphQL APIs including:
- Authentication (API accounts, OAuth)
- Catalog API (products, categories, brands, variants)
- Orders API
- Customers API
- Carts & Checkout API
- Storefront API
- Webhooks
- Rate limits and pagination
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/bigcommerce/docs.git"
REPO_BRANCH = "main"
SOURCE_DOCS_FOLDER = "docs"


def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "bigcommerce-docs"

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

        # Copy entire docs folder structure
        for item in source_dir.iterdir():
            if item.is_dir():
                dest = output_dir / item.name
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(item, dest)
            elif item.is_file():
                shutil.copy2(item, output_dir / item.name)

        return True

    except Exception as e:
        print(f"    -> Error copying documentation: {e}")
        return False


def main():
    """Main function to extract BigCommerce API documentation."""
    print("\nBigCommerce API Documentation Extractor")
    print("=" * 50)

    # Define output directory
    output_dir = Path(__file__).parent.parent / "docs" / "github-scraped" / "bigcommerce"

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
    md_files = list(output_dir.glob("**/*.md")) + list(output_dir.glob("**/*.mdx"))
    print(f"Total documentation files: {len(md_files)}")

    # Show folder structure
    subdirs = [d for d in output_dir.iterdir() if d.is_dir()]
    print(f"\nDocumentation folders ({len(subdirs)}):")
    for subdir in sorted(subdirs):
        file_count = len(list(subdir.glob("**/*.md")) + list(subdir.glob("**/*.mdx")))
        print(f"  - {subdir.name}: {file_count} files")

    total_size = sum(f.stat().st_size for f in output_dir.glob("**/*") if f.is_file())
    print(f"\nTotal size: {total_size:,} bytes ({total_size / (1024*1024):.2f} MB)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
