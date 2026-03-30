#!/usr/bin/env python3
"""
mlx-swift Documentation Extractor
Downloads mlx-swift documentation from GitHub repository.
mlx-swift provides Swift APIs for the MLX array framework on Apple silicon.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/ml-explore/mlx-swift.git"
REPO_BRANCH = "main"

# Files and directories to include (relative to repo root)
INCLUDE_PATTERNS = [
    "README.md",
    "CONTRIBUTING.md",
    "MAINTENANCE.md",
    "ACKNOWLEDGMENTS.md",
    "Source/*/Documentation.docc/*.md",
]

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "mlx-swift"

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
        repo_path = Path(source_dir)

        if not repo_path.exists():
            print(f"    -> Repository path not found: {repo_path}")
            return False

        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        copied_count = 0

        # Copy README first if it exists
        readme_path = repo_path / "README.md"
        if readme_path.exists():
            dest = output_dir / "README.md"
            with open(readme_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            source_url = f"https://github.com/ml-explore/mlx-swift/blob/main/README.md"
            header = f"# Source: {source_url}\n\n"
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(header + content)
            print(f"    -> Copied: README.md")
            copied_count += 1

        # Copy CONTRIBUTING.md
        contributing_path = repo_path / "CONTRIBUTING.md"
        if contributing_path.exists():
            dest = output_dir / "CONTRIBUTING.md"
            with open(contributing_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            source_url = f"https://github.com/ml-explore/mlx-swift/blob/main/CONTRIBUTING.md"
            header = f"# Source: {source_url}\n\n"
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(header + content)
            print(f"    -> Copied: CONTRIBUTING.md")
            copied_count += 1

        # Copy MAINTENANCE.md
        maintenance_path = repo_path / "MAINTENANCE.md"
        if maintenance_path.exists():
            dest = output_dir / "MAINTENANCE.md"
            with open(maintenance_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            source_url = f"https://github.com/ml-explore/mlx-swift/blob/main/MAINTENANCE.md"
            header = f"# Source: {source_url}\n\n"
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(header + content)
            print(f"    -> Copied: MAINTENANCE.md")
            copied_count += 1

        # Copy ACKNOWLEDGMENTS.md
        acknowledgments_path = repo_path / "ACKNOWLEDGMENTS.md"
        if acknowledgments_path.exists():
            dest = output_dir / "ACKNOWLEDGMENTS.md"
            with open(acknowledgments_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            source_url = f"https://github.com/ml-explore/mlx-swift/blob/main/ACKNOWLEDGMENTS.md"
            header = f"# Source: {source_url}\n\n"
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(header + content)
            print(f"    -> Copied: ACKNOWLEDGMENTS.md")
            copied_count += 1

        # Copy documentation files from Source directories
        print(f"    -> Copying documentation files...")
        source_dir = repo_path / "Source"
        if source_dir.exists():
            for doc_dir in source_dir.rglob("Documentation.docc"):
                if doc_dir.is_dir():
                    for md_file in doc_dir.glob("*.md"):
                        relative_path = md_file.relative_to(repo_path)
                        # Create a meaningful name based on the module
                        module_name = md_file.parent.parent.name
                        dest = output_dir / f"{module_name}_{md_file.name}"

                        with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()

                        source_url = f"https://github.com/ml-explore/mlx-swift/blob/main/{relative_path}"
                        header = f"# Source: {source_url}\n\n"

                        with open(dest, 'w', encoding='utf-8') as f:
                            f.write(header + content)

                        if copied_count < 25:  # Print first 25
                            print(f"    -> Copied: {relative_path}")
                        copied_count += 1

        # Copy Package.swift as it contains useful information
        package_path = repo_path / "Package.swift"
        if package_path.exists():
            dest = output_dir / "Package.swift"
            with open(package_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            source_url = f"https://github.com/ml-explore/mlx-swift/blob/main/Package.swift"
            header = f"# Source: {source_url}\n\n```swift\n"
            footer = "\n```\n"
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(header + content + footer)
            print(f"    -> Copied: Package.swift (package configuration)")
            copied_count += 1

        if copied_count == 0:
            print(f"    -> Warning: No documentation files found")
            return False

        print(f"    -> Total files copied: {copied_count}")
        return True

    except Exception as e:
        print(f"    -> Error copying documentation: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main function to extract mlx-swift documentation."""
    print("=" * 70)
    print("mlx-swift Documentation Extractor")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "mlx-swift"

    print(f"Repository: {REPO_URL}")
    print(f"Branch: {REPO_BRANCH}")
    print(f"Output directory: {output_dir}")
    print()

    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Clone repository
        print("Cloning repository...")
        repo_path = clone_repository(temp_dir, REPO_URL, REPO_BRANCH)

        if not repo_path:
            print("\nError: Failed to clone repository")
            sys.exit(1)

        # Copy documentation
        print("\nCopying documentation files...")

        # Remove existing output directory if it exists
        if output_dir.exists():
            print(f"  Removing existing output directory: {output_dir}")
            shutil.rmtree(output_dir)

        if not copy_documentation(repo_path, output_dir):
            print("\nError: Failed to copy documentation")
            sys.exit(1)

    # Verify extraction
    print("\nVerifying extraction...")
    if not output_dir.exists():
        print("  Error: Output directory was not created")
        sys.exit(1)

    text_files = list(output_dir.glob("**/*"))
    text_files = [f for f in text_files if f.is_file()]
    total_size = sum(f.stat().st_size for f in text_files)

    print(f"  Total files: {len(text_files)}")
    print(f"  Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")

    if len(text_files) == 0:
        print("\n  Warning: No files found in output directory")
        sys.exit(1)

    # List main files
    print("\n  Main documentation files:")
    for text_file in sorted(text_files)[:15]:
        file_size = text_file.stat().st_size
        print(f"    - {text_file.relative_to(output_dir)} ({file_size:,} bytes)")

    if len(text_files) > 15:
        print(f"    ... and {len(text_files) - 15} more files")

    print()
    print("=" * 70)
    print("Extraction Complete")
    print("=" * 70)
    print(f"Output: {output_dir}")
    print()


if __name__ == "__main__":
    main()
