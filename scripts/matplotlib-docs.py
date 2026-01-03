#!/usr/bin/env python3
"""
Matplotlib Documentation Extractor
Extracts matplotlib documentation from GitHub repository and converts RST to Markdown.
Matplotlib is a Python plotting library for creating 2D/3D visualizations.
"""

import os
import sys
import subprocess
import tempfile
from pathlib import Path
import shutil
import time

# Configuration
REPO_URL = "https://github.com/matplotlib/matplotlib.git"
SOURCE_FOLDER = "doc"
OUTPUT_BASE = "docs/github-scraped/matplotlib"


def clone_repo(temp_dir):
    """Clone the matplotlib repository."""
    try:
        print(f"Cloning matplotlib repository...")
        repo_path = temp_dir / "matplotlib"

        result = subprocess.run(
            ["git", "clone", "--depth", "1", REPO_URL, str(repo_path)],
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode != 0:
            print(f"  Error cloning repo: {result.stderr}")
            return None

        print(f"  Repository cloned successfully")
        return repo_path
    except Exception as e:
        print(f"  Error cloning repository: {e}")
        return None


def convert_rst_to_markdown(rst_file, md_file):
    """Convert RST file to Markdown using pandoc."""
    try:
        result = subprocess.run(
            ["pandoc", "-f", "rst", "-t", "markdown", "-o", str(md_file), str(rst_file)],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            # Fallback: just copy as text if conversion fails
            with open(rst_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            header = f"# Source: {rst_file.name}\n\n```rst\n"
            footer = "\n```\n"

            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(header + content + footer)

            return True

        return True
    except Exception as e:
        print(f"    Warning: Could not convert {rst_file.name}: {e}")
        return False


def copy_markdown_file(source_file, target_file):
    """Copy markdown file with source header."""
    try:
        with open(source_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        header = f"# Source: {source_file.name}\n\n"

        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(header + content)

        return True
    except Exception as e:
        print(f"    Warning: Could not copy {source_file.name}: {e}")
        return False


def process_documentation(repo_path, output_dir):
    """Process documentation files from the repository."""
    doc_path = repo_path / SOURCE_FOLDER

    if not doc_path.exists():
        print(f"  Error: Documentation folder not found at {doc_path}")
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)

    # Find all RST and MD files
    rst_files = sorted(doc_path.rglob("*.rst"))
    md_files = sorted(doc_path.rglob("*.md"))

    print(f"Found {len(rst_files)} RST files and {len(md_files)} MD files")
    print()

    processed = 0
    skipped = 0

    # Process RST files
    if rst_files:
        print("Converting RST files to Markdown...")
        for idx, rst_file in enumerate(rst_files, 1):
            # Create relative path structure
            rel_path = rst_file.relative_to(doc_path)
            md_target = output_dir / rel_path.with_suffix('.md')

            # Create subdirectories
            md_target.parent.mkdir(parents=True, exist_ok=True)

            # Skip very large files (likely generated)
            if rst_file.stat().st_size > 5_000_000:
                print(f"  [{idx:3d}] Skipping (too large): {rel_path}")
                skipped += 1
                continue

            if convert_rst_to_markdown(rst_file, md_target):
                if idx % 50 == 0:
                    print(f"  [{idx:3d}] Converted: {rel_path}")
                processed += 1
            else:
                skipped += 1

    # Process existing Markdown files
    if md_files:
        print()
        print("Processing existing Markdown files...")
        for idx, md_file in enumerate(md_files, 1):
            rel_path = md_file.relative_to(doc_path)
            md_target = output_dir / rel_path

            md_target.parent.mkdir(parents=True, exist_ok=True)

            if copy_markdown_file(md_file, md_target):
                if idx % 50 == 0:
                    print(f"  [{idx:3d}] Copied: {rel_path}")
                processed += 1
            else:
                skipped += 1

    return processed


def main():
    """Main function to extract matplotlib documentation."""
    print("=" * 70)
    print("Matplotlib Documentation Extractor")
    print("=" * 70)
    print()

    # Get absolute paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    output_dir = repo_root / OUTPUT_BASE

    print(f"Output directory: {output_dir}")
    print()

    # Create temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Clone repository
        print("Step 1: Cloning repository")
        print("-" * 70)
        repo_path = clone_repo(temp_path)
        if not repo_path:
            print("Failed to clone repository")
            sys.exit(1)
        print()

        # Process documentation
        print("Step 2: Processing documentation files")
        print("-" * 70)
        start_time = time.time()
        processed = process_documentation(repo_path, output_dir)
        elapsed = time.time() - start_time

    print()
    print("=" * 70)
    print("Extraction Summary")
    print("=" * 70)
    print(f"Files processed: {processed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output directory: {output_dir}")
    print()

    # Calculate statistics
    if output_dir.exists():
        md_files = list(output_dir.glob("**/*.md"))
        total_size = sum(f.stat().st_size for f in md_files)

        print(f"Total markdown files: {len(md_files)}")
        print(f"Total size: {total_size:,} bytes ({total_size/1024/1024:.1f} MB)")
        print()

        if processed > 0:
            print("Documentation extracted successfully!")
            sys.exit(0)
        else:
            print("Warning: No files were processed")
            sys.exit(1)
    else:
        print("Error: Output directory was not created")
        sys.exit(1)


if __name__ == "__main__":
    main()
