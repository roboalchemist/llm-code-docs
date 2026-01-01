#!/usr/bin/env python3
"""
Langroid Documentation Extractor
Extracts documentation from langroid/langroid GitHub repository.
Langroid is a multi-agent LLM programming framework with message-passing architecture.
"""

import subprocess
import shutil
import tempfile
from pathlib import Path
import sys
import os

def extract_langroid_docs():
    """Extract Langroid documentation from GitHub repository."""
    print("=" * 70)
    print("Langroid Documentation Extractor")
    print("=" * 70)
    print()

    # Paths
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "langroid"
    repo_url = "https://github.com/langroid/langroid.git"
    docs_source = "docs"

    print(f"Repository: {repo_url}")
    print(f"Source folder: {docs_source}")
    print(f"Output directory: {output_dir}")
    print()

    # Create temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        clone_path = temp_path / "langroid"

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
            excluded_dirs = {'assets', 'screenshots', 'logos', 'javascripts', 'stylesheets', 'overrides'}
            excluded_files = {'auto_docstring.py'}

            for item in output_dir.rglob('*'):
                # Remove excluded directories
                if item.is_dir() and item.name in excluded_dirs:
                    shutil.rmtree(item)
                    print(f"  Removed: {item.relative_to(output_dir)}")
                # Remove excluded files
                elif item.is_file() and item.name in excluded_files:
                    item.unlink()
                    print(f"  Removed: {item.relative_to(output_dir)}")

            print()
            print("=" * 70)
            print("Extraction Summary")
            print("=" * 70)

            # Calculate statistics
            md_files = list(output_dir.glob("**/*.md"))
            total_files = len(md_files)
            total_size = sum(f.stat().st_size for f in output_dir.glob("**/*") if f.is_file())

            print(f"Total markdown files: {total_files}")
            print(f"Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")
            print(f"Output: {output_dir}")
            print()
            print("Documentation extracted successfully!")
            return 0

        except subprocess.CalledProcessError as e:
            print(f"Error during git operations: {e}")
            print(f"stderr: {e.stderr}")
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 1

if __name__ == "__main__":
    sys.exit(extract_langroid_docs())
