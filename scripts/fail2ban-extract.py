#!/usr/bin/env python3
"""
fail2ban Documentation Extractor
Downloads fail2ban documentation from GitHub repository.
fail2ban is an intrusion prevention software that monitors log files and bans IPs exhibiting malicious behavior.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/fail2ban/fail2ban.git"
REPO_BRANCH = "master"
SOURCE_DOCS_FOLDER = "doc"

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "fail2ban"

def clone_repo(repo_url, branch, timeout=300):
    """Clone repository to temporary directory."""
    temp_dir = tempfile.mkdtemp(prefix="fail2ban_")
    print(f"Cloning {repo_url} (branch: {branch})...")
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", branch, repo_url, temp_dir],
            timeout=timeout,
            check=True,
            capture_output=True
        )
        return temp_dir
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e.stderr.decode()}", file=sys.stderr)
        return None

def copy_docs(temp_dir, source_folder, output_dir):
    """Copy documentation from cloned repo to output directory."""
    source_path = Path(temp_dir) / source_folder

    if not source_path.exists():
        print(f"Error: Source folder '{source_folder}' not found in repository", file=sys.stderr)
        return False

    print(f"Copying documentation from {source_path} to {output_dir}...")

    # Remove existing output directory
    if output_dir.exists():
        shutil.rmtree(output_dir)

    # Copy entire directory
    shutil.copytree(source_path, output_dir)

    return True

def convert_rst_to_md(directory):
    """Convert RST files to markdown using pandoc if available."""
    try:
        import subprocess
        for rst_file in directory.rglob("*.rst"):
            md_file = rst_file.with_suffix(".md")
            print(f"Converting {rst_file.name} to markdown...")
            subprocess.run(
                ["pandoc", "-f", "rst", "-t", "markdown", "-o", str(md_file), str(rst_file)],
                capture_output=True,
                timeout=10
            )
            # Remove original RST file after successful conversion
            if md_file.exists():
                rst_file.unlink()
    except Exception as e:
        print(f"Warning: RST conversion skipped ({e})")

def cleanup(temp_dir):
    """Remove temporary directory."""
    if Path(temp_dir).exists():
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("fail2ban Documentation Extractor")
    print("=" * 50)

    # Clone repository
    temp_dir = clone_repo(REPO_URL, REPO_BRANCH)
    if not temp_dir:
        sys.exit(1)

    try:
        # Copy documentation
        if not copy_docs(temp_dir, SOURCE_DOCS_FOLDER, OUTPUT_DIR):
            sys.exit(1)

        print(f"Documentation copied to {OUTPUT_DIR}")

        # Convert RST to markdown if pandoc is available
        convert_rst_to_md(OUTPUT_DIR)

        # List generated files
        files = list(OUTPUT_DIR.rglob("*"))
        print(f"\nGenerated {len([f for f in files if f.is_file()])} files:")
        for f in sorted(files)[:10]:
            if f.is_file():
                size = f.stat().st_size
                print(f"  {f.relative_to(OUTPUT_DIR)} ({size} bytes)")

        print("\nSuccess!")
    finally:
        cleanup(temp_dir)
