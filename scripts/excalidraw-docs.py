#!/usr/bin/env python3
"""
Excalidraw Documentation Scraper
Downloads Excalidraw documentation from GitHub repository via git clone.
Excalidraw is a virtual collaborative whiteboard tool for sketching diagrams.
"""

import os
import sys
import subprocess
from pathlib import Path
import shutil
import tempfile

# Documentation directories to copy (relative to dev-docs/docs/)
DOC_DIRS = [
    "introduction",
    "codebase",
    "@excalidraw/excalidraw/api",
    "@excalidraw/excalidraw",
    "@excalidraw/mermaid-to-excalidraw",
]

# Additional files to copy from repo root
ADDITIONAL_FILES = [
    "README.md",
]


def clone_repo(clone_dir):
    """Clone the Excalidraw repository."""
    try:
        print("Cloning Excalidraw repository...")
        subprocess.run(
            ["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse",
             "https://github.com/excalidraw/excalidraw.git", clone_dir],
            check=True,
            capture_output=True,
            timeout=120
        )

        # Configure sparse checkout (disable cone mode to allow files and dirs)
        subprocess.run(
            ["git", "-C", clone_dir, "sparse-checkout", "set", "--no-cone", "dev-docs/docs", "README.md"],
            check=True,
            capture_output=True,
            timeout=30
        )

        print("  -> Repository cloned successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  -> Error cloning repository: {e}")
        print(f"  -> stderr: {e.stderr.decode() if e.stderr else 'N/A'}")
        return False
    except Exception as e:
        print(f"  -> Error: {e}")
        return False


def copy_docs(clone_dir, output_dir):
    """Copy documentation files from cloned repo to output directory."""
    successful = 0
    failed = 0

    # Copy files from dev-docs/docs directories
    dev_docs_path = Path(clone_dir) / "dev-docs" / "docs"

    for doc_dir in DOC_DIRS:
        source_path = dev_docs_path / doc_dir

        if not source_path.exists():
            print(f"  Warning: Directory not found: {source_path}")
            continue

        # Find all .md and .mdx files
        for source_file in source_path.rglob("*.md*"):
            if source_file.is_file():
                # Calculate relative path from dev-docs/docs
                try:
                    rel_path = source_file.relative_to(dev_docs_path)
                except ValueError:
                    continue

                # Create output filename (replace / with -)
                output_filename = str(rel_path).replace("/", "-")
                output_path = output_dir / output_filename

                try:
                    # Read content
                    with open(source_file, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Add metadata header
                    header = f"""# Excalidraw Documentation
# Source: https://github.com/excalidraw/excalidraw/blob/master/dev-docs/docs/{rel_path}
# Path: dev-docs/docs/{rel_path}

"""
                    content = header + content

                    # Write to output
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(content)

                    print(f"  Copied: {rel_path}")
                    successful += 1

                except Exception as e:
                    print(f"  -> Error copying {rel_path}: {e}")
                    failed += 1

    # Copy additional files
    for filename in ADDITIONAL_FILES:
        source_file = Path(clone_dir) / filename

        if not source_file.exists():
            print(f"  Warning: File not found: {filename}")
            continue

        try:
            # Read content
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Add metadata header
            header = f"""# Excalidraw Documentation
# Source: https://github.com/excalidraw/excalidraw/blob/master/{filename}
# Path: {filename}

"""
            content = header + content

            # Write to output
            output_filename = f"main-{filename}"
            output_path = output_dir / output_filename

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"  Copied: {filename}")
            successful += 1

        except Exception as e:
            print(f"  -> Error copying {filename}: {e}")
            failed += 1

    return successful, failed


def main():
    """Main function to download all Excalidraw documentation."""
    print("=" * 60)
    print("Excalidraw Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "excalidraw"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Create temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        clone_dir = Path(temp_dir) / "excalidraw"

        # Clone repository
        if not clone_repo(str(clone_dir)):
            print("\nFailed to clone repository")
            sys.exit(1)

        print()
        print("Copying documentation files...")

        # Copy documentation files
        successful, failed = copy_docs(clone_dir, output_dir)

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md*"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} files failed to download")
        sys.exit(1)
    else:
        print("All documentation downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
