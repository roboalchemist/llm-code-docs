#!/usr/bin/env python3
"""
Weaviate Documentation Scraper
Clones the Weaviate docs repository and extracts markdown documentation.
Weaviate is an open-source vector database for AI applications.
"""

import os
import sys
import shutil
from pathlib import Path
import subprocess
import time

REPO_URL = "https://github.com/weaviate/docs"
DOCS_SOURCE_FOLDER = "."


def clone_or_update_repo(repo_path):
    """Clone or update the Weaviate docs repository."""
    if repo_path.exists():
        print(f"Updating existing repository: {repo_path}")
        try:
            subprocess.run(
                ['git', '-C', str(repo_path), 'pull'],
                check=True,
                capture_output=True,
                timeout=120
            )
            print("  -> Repository updated")
            return True
        except subprocess.CalledProcessError as e:
            print(f"  -> Error updating repository: {e}")
            # Try to remove and re-clone
            print("  -> Attempting fresh clone...")
            shutil.rmtree(repo_path)

    print(f"Cloning repository: {REPO_URL}")
    try:
        subprocess.run(
            ['git', 'clone', '--depth', '1', REPO_URL, str(repo_path)],
            check=True,
            capture_output=True,
            timeout=300
        )
        print("  -> Repository cloned successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  -> Error cloning repository: {e}")
        return False


def copy_markdown_files(source_dir, target_dir):
    """Copy markdown files from source to target directory."""
    if not source_dir.exists():
        print(f"Error: Source directory not found: {source_dir}")
        return 0, 0

    # Clear target directory
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    copied = 0
    skipped = 0

    # Find all markdown files
    md_files = list(source_dir.glob('**/*.md'))
    md_files.extend(list(source_dir.glob('**/*.mdx')))

    print(f"Found {len(md_files)} documentation files")

    for src_file in md_files:
        try:
            # Get relative path from source directory
            rel_path = src_file.relative_to(source_dir)

            # Skip certain files
            skip_patterns = [
                'node_modules',
                '.git',
                'README.md',
                'CONTRIBUTING.md',
                'CHANGELOG.md'
            ]

            if any(pattern in str(rel_path) for pattern in skip_patterns):
                skipped += 1
                continue

            # Create target path (flatten directory structure with hyphens)
            # e.g., tutorials/basics.md -> tutorials-basics.md
            if rel_path.parent != Path('.'):
                target_name = str(rel_path.parent).replace(os.sep, '-') + '-' + rel_path.name
            else:
                target_name = rel_path.name

            # Ensure .md extension (convert .mdx to .md)
            if target_name.endswith('.mdx'):
                target_name = target_name[:-4] + '.md'

            target_file = target_dir / target_name

            # Read source content
            with open(src_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Add source header
            source_url = f"https://github.com/weaviate/docs/blob/main/{rel_path}"
            content_with_header = f"# Source: {source_url}\n\n{content}"

            # Write to target
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(content_with_header)

            copied += 1

        except Exception as e:
            print(f"  -> Error processing {src_file}: {e}")
            skipped += 1

    return copied, skipped


def main():
    """Main function to clone Weaviate docs and extract documentation."""
    print("=" * 60)
    print("Weaviate Documentation Scraper")
    print("=" * 60)
    print(f"Repository: {REPO_URL}")
    print()

    start_time = time.time()

    # Setup paths
    script_dir = Path(__file__).parent.parent
    temp_dir = Path('/tmp/weaviate-docs-clone')
    output_dir = script_dir / "docs" / "github-scraped" / "weaviate"

    # Clone repository
    if not clone_or_update_repo(temp_dir):
        print("Failed to clone/update repository")
        sys.exit(1)

    print()

    # Source directory
    source_dir = temp_dir / DOCS_SOURCE_FOLDER

    if not source_dir.exists():
        print(f"Error: Documentation folder not found: {source_dir}")
        print("Repository structure may have changed.")
        sys.exit(1)

    print(f"Source directory: {source_dir}")
    print(f"Output directory: {output_dir}")
    print()

    # Copy markdown files
    copied, skipped = copy_markdown_files(source_dir, output_dir)

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Extraction Summary")
    print("=" * 60)
    print(f"Files copied: {copied}")
    print(f"Files skipped: {skipped}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    if output_dir.exists():
        total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
        print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()

    if copied == 0:
        print("Warning: No files were copied")
        sys.exit(1)
    else:
        print(f"Successfully extracted {copied} documentation files!")
        sys.exit(0)


if __name__ == "__main__":
    main()
