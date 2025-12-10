#!/usr/bin/env python3
"""
Tailwind CSS Documentation Scraper
Downloads all Tailwind CSS documentation from the GitHub repository.
Tailwind CSS has no llms.txt, so we clone the repo and extract MDX files.
"""

import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path


def clone_repo(temp_dir: Path) -> bool:
    """Clone the tailwindcss.com repository."""
    repo_url = "https://github.com/tailwindlabs/tailwindcss.com.git"

    print(f"Cloning repository: {repo_url}")
    print("This may take a moment...")

    try:
        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--single-branch", repo_url, str(temp_dir)],
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode != 0:
            print(f"Error cloning repository: {result.stderr}")
            return False

        print("Repository cloned successfully!")
        return True

    except subprocess.TimeoutExpired:
        print("Error: Clone operation timed out")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def process_mdx_file(mdx_path: Path, output_path: Path, repo_path: str) -> bool:
    """Process an MDX file and save as markdown."""
    try:
        content = mdx_path.read_text(encoding='utf-8')

        # Add source header
        github_url = f"https://github.com/tailwindlabs/tailwindcss.com/blob/main/{repo_path}"
        header = f"# Source: {github_url}\n\n"

        # Write the file (MDX is mostly markdown compatible)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(header + content, encoding='utf-8')

        return True

    except Exception as e:
        print(f"  -> Error processing {mdx_path}: {e}")
        return False


def main():
    """Main function to download all Tailwind CSS documentation."""
    print("=" * 60)
    print("Tailwind CSS Documentation Scraper")
    print("=" * 60)
    print("Source: GitHub (tailwindlabs/tailwindcss.com)")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "llms-txt" / "tailwindcss"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    start_time = time.time()

    # Clone to temp directory
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        if not clone_repo(temp_path):
            sys.exit(1)

        # Find all MDX files in src/docs
        docs_dir = temp_path / "src" / "docs"

        if not docs_dir.exists():
            print(f"Error: Documentation directory not found: {docs_dir}")
            sys.exit(1)

        mdx_files = list(docs_dir.glob("*.mdx"))
        print(f"\nFound {len(mdx_files)} MDX files in src/docs/")
        print()

        successful = 0
        failed = 0

        for i, mdx_path in enumerate(sorted(mdx_files), 1):
            # Output filename: convert to .md
            output_name = mdx_path.stem + ".md"
            output_path = output_dir / output_name

            # Relative path in repo
            repo_path = f"src/docs/{mdx_path.name}"

            print(f"[{i:3d}/{len(mdx_files)}] {mdx_path.name}", end="")

            if process_mdx_file(mdx_path, output_path, repo_path):
                successful += 1
                print(f" -> {output_name}")
            else:
                failed += 1
                print(" -> FAILED")

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} files failed to process")
        sys.exit(1)
    else:
        print("All documentation files processed successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
