#!/usr/bin/env python3
"""
llama.cpp Documentation Extractor
Downloads llama.cpp documentation from GitHub repository.
llama.cpp is a C/C++ inference engine for LLMs with GGUF format support
and CPU, CUDA, Vulkan, OpenCL backend support.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/ggerganov/llama.cpp.git"
REPO_BRANCH = "master"

# Files and directories to include (relative to repo root)
INCLUDE_PATTERNS = [
    "README.md",
    "docs/**/*.md",
    "examples/**/*.md",
    "examples/**/*.cpp",
    "examples/**/*.c",
    "include/llama.h",
    "ggml/include/ggml.h",
    "ggml/include/ggml-*.h",
]

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "llama-cpp"

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


def should_include_file(file_path, repo_path):
    """Check if a file should be included based on patterns."""
    relative_path = file_path.relative_to(repo_path)
    path_str = str(relative_path).replace("\\", "/")

    # Always include if it matches explicitly
    for pattern in INCLUDE_PATTERNS:
        if "/" in pattern and pattern.startswith("include/"):
            # Exact header file paths
            if path_str == pattern:
                return True
        elif "/**/" in pattern:
            # Directory patterns
            base_dir = pattern.split("/")[0]
            if path_str.startswith(base_dir + "/"):
                ext = file_path.suffix
                required_exts = [p.split(".")[-1] for p in pattern.split(".")[-1:]]
                if ext in [".md", ".cpp", ".c", ".h"] or ext == "":
                    return True
        elif path_str == pattern:
            # Exact file matches
            return True

    return False


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
            source_url = f"https://github.com/ggerganov/llama.cpp/blob/master/README.md"
            header = f"# Source: {source_url}\n\n"
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(header + content)
            print(f"    -> Copied: README.md")
            copied_count += 1

        # Copy docs directory recursively
        docs_dir = repo_path / "docs"
        if docs_dir.exists():
            print(f"    -> Copying docs directory...")
            for item in docs_dir.rglob("*"):
                if item.is_file() and item.suffix in [".md", ".txt"]:
                    relative_path = item.relative_to(repo_path)
                    dest = output_dir / relative_path
                    dest.parent.mkdir(parents=True, exist_ok=True)

                    with open(item, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()

                    source_url = f"https://github.com/ggerganov/llama.cpp/blob/master/{relative_path}"
                    header = f"# Source: {source_url}\n\n"

                    with open(dest, 'w', encoding='utf-8') as f:
                        f.write(header + content)

                    if copied_count < 20:  # Only print first 20
                        print(f"    -> Copied: {relative_path}")
                    copied_count += 1

        # Copy key header files for API reference
        print(f"    -> Copying header files...")
        headers = [
            repo_path / "include" / "llama.h",
            repo_path / "ggml" / "include" / "ggml.h",
        ]

        for header in headers:
            if header.exists():
                relative_path = header.relative_to(repo_path)
                dest = output_dir / f"API_{header.stem}.h"

                with open(header, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                # Extract just the public API (comments and function declarations)
                source_url = f"https://github.com/ggerganov/llama.cpp/blob/master/{relative_path}"
                header_text = f"# Source: {source_url}\n\n```c\n{content}\n```\n"

                with open(dest, 'w', encoding='utf-8') as f:
                    f.write(header_text)

                print(f"    -> Copied: {relative_path}")
                copied_count += 1

        # Copy examples directory with markdown files
        examples_dir = repo_path / "examples"
        if examples_dir.exists():
            print(f"    -> Copying examples...")
            for item in examples_dir.rglob("*"):
                if item.is_file() and item.suffix in [".md", ".cpp", ".c"]:
                    relative_path = item.relative_to(repo_path)
                    dest = output_dir / relative_path
                    dest.parent.mkdir(parents=True, exist_ok=True)

                    with open(item, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()

                    source_url = f"https://github.com/ggerganov/llama.cpp/blob/master/{relative_path}"
                    header = f"# Source: {source_url}\n\n"

                    with open(dest, 'w', encoding='utf-8') as f:
                        f.write(header + content)

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
    """Main function to extract llama.cpp documentation."""
    print("=" * 70)
    print("llama.cpp Documentation Extractor")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "llama-cpp"

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
