#!/usr/bin/env python3
"""
errcheck Documentation Extractor
Downloads errcheck documentation from GitHub repository.
errcheck is a Go linter that detects unchecked error returns in Go code.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/kisielk/errcheck.git"
REPO_BRANCH = "master"

# Files to extract from repository root
FILES_TO_EXTRACT = [
    "README.md",
    "LICENSE",
]

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "errcheck"

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


def extract_documentation(source_dir, output_dir):
    """Extract documentation files from repository."""
    try:
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        files_found = 0
        for filename in FILES_TO_EXTRACT:
            source_file = Path(source_dir) / filename

            if source_file.exists():
                dest_file = output_dir / filename

                with open(source_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                # Add source header
                source_url = f"https://github.com/kisielk/errcheck/blob/{REPO_BRANCH}/{filename}"
                header = f"""# Source: {source_url}

"""
                final_content = header + content

                with open(dest_file, 'w', encoding='utf-8') as f:
                    f.write(final_content)

                print(f"    -> Extracted {filename} ({len(final_content)} bytes)")
                files_found += 1
            else:
                print(f"    -> File not found: {filename}")

        if files_found > 0:
            print(f"  Successfully extracted {files_found} files")
            return True
        else:
            print(f"  No files were extracted")
            return False

    except Exception as e:
        print(f"  Error extracting documentation: {e}")
        return False


def main():
    """Main extraction process."""
    try:
        print("=" * 60)
        print("errcheck Documentation Extractor")
        print("=" * 60)
        print()

        # Create temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Clone repository
            repo_path = clone_repository(temp_dir, REPO_URL, REPO_BRANCH)

            if not repo_path:
                print("Failed to clone repository")
                return False

            # Define output directory
            output_dir = Path(__file__).parent.parent / "docs" / "web-scraped" / "errcheck"

            # Extract documentation
            if extract_documentation(repo_path, output_dir):
                print(f"\nDocumentation extracted to: {output_dir}")

                # Calculate total size
                total_size = sum(f.stat().st_size for f in output_dir.glob("*"))
                print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
                print()
                print("All documentation extracted successfully!")
                return True
            else:
                print("Failed to extract documentation")
                return False

    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
