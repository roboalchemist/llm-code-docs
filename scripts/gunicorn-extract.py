#!/usr/bin/env python3
"""
Gunicorn Documentation Extractor
Downloads Gunicorn documentation from GitHub repository.
Gunicorn is a Python WSGI HTTP Server with pre-forked worker model, multiple worker types,
and comprehensive configuration options for deploying Python web applications.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/benoitc/gunicorn.git"
REPO_BRANCH = "master"
SOURCE_DOCS_FOLDER = "docs/source"

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "gunicorn"

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

        # Copy all documentation files
        file_count = 0
        for item in docs_source.rglob("*"):
            if item.is_file():
                # Calculate relative path
                rel_path = item.relative_to(docs_source)
                output_file = output_dir / rel_path

                # Create parent directories
                output_file.parent.mkdir(parents=True, exist_ok=True)

                # Copy file
                shutil.copy2(item, output_file)
                file_count += 1

        print(f"    -> Copied {file_count} documentation files")
        return file_count > 0

    except Exception as e:
        print(f"    -> Error copying documentation: {e}")
        return False


def convert_rst_to_markdown(file_path):
    """Convert RST files to Markdown using pandoc if available."""
    try:
        if file_path.suffix == ".rst":
            # Check if pandoc is available
            result = subprocess.run(
                ["which", "pandoc"],
                capture_output=True,
                timeout=5
            )
            if result.returncode == 0:
                md_path = file_path.with_suffix(".md")
                subprocess.run(
                    ["pandoc", "-f", "rst", "-t", "markdown", "-o", str(md_path), str(file_path)],
                    capture_output=True,
                    timeout=30
                )
                if md_path.exists():
                    file_path.unlink()  # Remove original RST file
                    return md_path
    except Exception:
        pass
    return file_path


def main():
    """Main extraction function."""
    print("\n" + "="*60)
    print("Gunicorn Documentation Extractor")
    print("="*60)

    # Create temporary directory
    temp_dir = tempfile.mkdtemp()
    output_dir = Path("/home/gateway/github/llm-code-docs/docs/github-scraped/gunicorn")

    try:
        # Remove existing output directory if it exists
        if output_dir.exists():
            print(f"Removing existing output directory: {output_dir}")
            shutil.rmtree(output_dir)

        # Clone repository
        print("\nCloning Gunicorn repository...")
        repo_path = clone_repository(temp_dir, REPO_URL, REPO_BRANCH)
        if not repo_path:
            print("ERROR: Failed to clone repository")
            return False

        # Copy documentation
        print("Copying documentation files...")
        if not copy_documentation(repo_path, output_dir):
            print("ERROR: Failed to copy documentation")
            return False

        # Optionally convert RST to Markdown
        print("Processing documentation files...")
        md_count = 0
        for rst_file in output_dir.rglob("*.rst"):
            md_file = convert_rst_to_markdown(rst_file)
            if md_file.suffix == ".md":
                md_count += 1

        if md_count > 0:
            print(f"    -> Converted {md_count} RST files to Markdown")

        # Print summary
        total_files = len(list(output_dir.rglob("*")))
        total_size = sum(f.stat().st_size for f in output_dir.rglob("*") if f.is_file())
        total_size_mb = total_size / (1024 * 1024)

        print(f"\nExtraction Summary:")
        print(f"  Output Directory: {output_dir}")
        print(f"  Total Files: {total_files}")
        print(f"  Total Size: {total_size_mb:.2f} MB")
        print(f"\nGunicorn documentation extracted successfully!")

        return True

    except Exception as e:
        print(f"ERROR: Unexpected error: {e}")
        return False

    finally:
        # Clean up temporary directory
        print(f"\nCleaning up temporary directory: {temp_dir}")
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
