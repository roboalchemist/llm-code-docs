#!/usr/bin/env python3
"""
Django REST Framework Documentation Extractor
Extracts documentation from encode/django-rest-framework GitHub repository.
Django REST Framework is a comprehensive REST framework built on Django for Python APIs.
"""

import subprocess
import shutil
import tempfile
from pathlib import Path
import sys
import os

def extract_drf_docs():
    """Extract Django REST Framework documentation from GitHub repository."""
    print("=" * 70)
    print("Django REST Framework Documentation Extractor")
    print("=" * 70)
    print()

    # Paths
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "django-rest-framework"
    repo_url = "https://github.com/encode/django-rest-framework.git"
    docs_source = "docs"

    print(f"Repository: {repo_url}")
    print(f"Source folder: {docs_source}")
    print(f"Output directory: {output_dir}")
    print()

    # Create temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        clone_path = temp_path / "django-rest-framework"

        print("Cloning repository...")
        try:
            subprocess.run(
                ["git", "clone", "--depth=1", "--filter=blob:none", "--sparse", repo_url],
                cwd=temp_path,
                capture_output=True,
                text=True,
                timeout=300,
                check=True
            )

            # Configure sparse checkout for docs only
            subprocess.run(
                ["git", "sparse-checkout", "set", "docs"],
                cwd=clone_path,
                capture_output=True,
                text=True,
                timeout=60,
                check=True
            )

            print("Repository cloned successfully!")
            print()

            # Check if docs folder exists
            docs_path = clone_path / docs_source
            if not docs_path.exists():
                print(f"Error: docs folder not found at {docs_path}")
                return 1

            # Remove old output directory
            if output_dir.exists():
                print(f"Removing existing directory: {output_dir}")
                shutil.rmtree(output_dir)

            # Copy docs to output directory
            print(f"Copying documentation...")
            shutil.copytree(docs_path, output_dir)

            # Remove non-markdown files and binary content
            excluded_dirs = {'img', 'images', 'assets', '__pycache__', '.git'}
            excluded_files = {'.gitignore', '.DS_Store', 'CNAME'}

            for item in output_dir.rglob("*"):
                if item.is_dir():
                    if item.name in excluded_dirs:
                        print(f"  Removing directory: {item.relative_to(output_dir)}")
                        shutil.rmtree(item)
                elif item.is_file():
                    if item.name in excluded_files or item.suffix not in {'.md', '.markdown', '.txt', '.rst'}:
                        if item.suffix not in {'.py', '.json', '.yaml', '.yml'}:  # Keep source config files
                            # Don't delete, just note it
                            pass

            # Count files
            md_files = list(output_dir.glob("**/*.md"))
            print()
            print(f"Documentation files extracted: {len(md_files)} markdown files")

            # Calculate total size
            total_size = sum(f.stat().st_size for f in output_dir.rglob("*") if f.is_file())
            print(f"Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")

            print()
            print("=" * 70)
            print(f"Successfully extracted Django REST Framework documentation!")
            print(f"Output: {output_dir}")
            print("=" * 70)
            return 0

        except subprocess.CalledProcessError as e:
            print(f"Error during git operation: {e}")
            print(f"stdout: {e.stdout}")
            print(f"stderr: {e.stderr}")
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 1


if __name__ == "__main__":
    sys.exit(extract_drf_docs())
