#!/usr/bin/env python3
"""
HTMX Documentation Scraper
Downloads all HTMX documentation from the GitHub repository.
HTMX has no llms.txt, so we clone the repo and extract markdown files from www/content.
"""

import subprocess
import sys
import tempfile
import time
from pathlib import Path


def clone_repo(temp_dir: Path) -> bool:
    """Clone the htmx repository."""
    repo_url = "https://github.com/bigskysoftware/htmx.git"

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


def process_md_file(md_path: Path, output_path: Path, repo_path: str) -> bool:
    """Process a markdown file and save it."""
    try:
        content = md_path.read_text(encoding='utf-8')

        # Add source header
        github_url = f"https://github.com/bigskysoftware/htmx/blob/master/{repo_path}"
        header = f"# Source: {github_url}\n\n"

        # Write the file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(header + content, encoding='utf-8')

        return True

    except Exception as e:
        print(f"  -> Error processing {md_path}: {e}")
        return False


def get_output_name(md_path: Path, content_dir: Path) -> str:
    """Generate output filename from path."""
    # Get relative path from content dir
    rel_path = md_path.relative_to(content_dir)

    # Convert to flat filename
    parts = list(rel_path.parts)

    # Handle _index.md files
    if parts[-1] == "_index.md":
        if len(parts) == 1:
            return "index.md"
        else:
            parts[-1] = "index.md"
            return "-".join(parts)

    # Join with dashes for nested paths
    return "-".join(parts)


def main():
    """Main function to download all HTMX documentation."""
    print("=" * 60)
    print("HTMX Documentation Scraper")
    print("=" * 60)
    print("Source: GitHub (bigskysoftware/htmx)")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "llms-txt" / "htmx"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    start_time = time.time()

    # Clone to temp directory
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        if not clone_repo(temp_path):
            sys.exit(1)

        # Find all markdown files in www/content
        content_dir = temp_path / "www" / "content"

        if not content_dir.exists():
            print(f"Error: Content directory not found: {content_dir}")
            sys.exit(1)

        md_files = list(content_dir.glob("**/*.md"))
        print(f"\nFound {len(md_files)} markdown files in www/content/")
        print()

        successful = 0
        failed = 0

        for i, md_path in enumerate(sorted(md_files), 1):
            # Generate output filename
            output_name = get_output_name(md_path, content_dir)
            output_path = output_dir / output_name

            # Relative path in repo for source header
            repo_path = f"www/content/{md_path.relative_to(content_dir)}"

            print(f"[{i:3d}/{len(md_files)}] {md_path.relative_to(content_dir)}", end="")

            if process_md_file(md_path, output_path, repo_path):
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
