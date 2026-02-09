#!/usr/bin/env python3
"""
mlx-lm Documentation Extractor
Downloads mlx-lm documentation from GitHub repository.
mlx-lm is a Python package for generating text and fine-tuning large language
models on Apple silicon with MLX.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/ml-explore/mlx-lm.git"
REPO_BRANCH = "main"

# Files and directories to include (relative to repo root)
INCLUDE_PATTERNS = [
    "README.md",
    "mlx_lm/LORA.md",
    "mlx_lm/examples/**/*.py",
    "mlx_lm/examples/**/*.yaml",
]

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "mlx-lm"

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
        if "/**/" in pattern:
            # Directory patterns
            base_dir = pattern.split("/")[0]
            if path_str.startswith(base_dir + "/"):
                ext = file_path.suffix
                required_exts = [p.split(".")[-1] for p in pattern.split(".")[-1:]]
                if ext in [".md", ".py", ".yaml", ".yml"] or ext == "":
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
            source_url = f"https://github.com/ml-explore/mlx-lm/blob/main/README.md"
            header = f"# Source: {source_url}\n\n"
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(header + content)
            print(f"    -> Copied: README.md")
            copied_count += 1

        # Copy LORA.md
        lora_path = repo_path / "mlx_lm" / "LORA.md"
        if lora_path.exists():
            dest = output_dir / "LORA.md"
            with open(lora_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            source_url = f"https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md"
            header = f"# Source: {source_url}\n\n"
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(header + content)
            print(f"    -> Copied: LORA.md (Fine-tuning documentation)")
            copied_count += 1

        # Copy examples directory with Python and YAML files
        examples_dir = repo_path / "mlx_lm" / "examples"
        if examples_dir.exists():
            print(f"    -> Copying examples...")
            for item in examples_dir.rglob("*"):
                if item.is_file() and item.suffix in [".py", ".yaml", ".yml"]:
                    relative_path = item.relative_to(repo_path)
                    dest = output_dir / ("examples_" + item.name)

                    with open(item, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()

                    source_url = f"https://github.com/ml-explore/mlx-lm/blob/main/{relative_path}"
                    header = f"# Source: {source_url}\n\n```python\n" if item.suffix == ".py" else f"# Source: {source_url}\n\n```yaml\n"
                    footer = "\n```\n"

                    with open(dest, 'w', encoding='utf-8') as f:
                        f.write(header + content + footer)

                    if copied_count < 20:  # Only print first 20
                        print(f"    -> Copied: {relative_path}")
                    copied_count += 1

        # Create API reference file from source code
        print(f"    -> Extracting API reference...")
        api_files = []

        # Look for main module files
        mlx_lm_dir = repo_path / "mlx_lm"
        if mlx_lm_dir.exists():
            for py_file in mlx_lm_dir.glob("*.py"):
                if py_file.name not in ["__init__.py"]:
                    with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()

                    # Extract docstrings and function definitions
                    lines = []
                    in_docstring = False
                    for line in content.split('\n'):
                        if '"""' in line or "'''" in line:
                            in_docstring = not in_docstring
                        if in_docstring or line.strip().startswith('def ') or line.strip().startswith('class '):
                            lines.append(line)

                    if lines:
                        dest = output_dir / f"api_{py_file.stem}.md"
                        source_url = f"https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/{py_file.name}"
                        header = f"# Source: {source_url}\n\n## API Reference\n\n```python\n"
                        footer = "\n```\n"
                        with open(dest, 'w', encoding='utf-8') as f:
                            f.write(header + '\n'.join(lines[:100]) + footer)
                        print(f"    -> Extracted: API from {py_file.name}")
                        api_files.append(dest)

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
    """Main function to extract mlx-lm documentation."""
    print("=" * 70)
    print("mlx-lm Documentation Extractor")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "mlx-lm"

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
