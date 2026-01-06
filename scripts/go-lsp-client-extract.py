#!/usr/bin/env python3
"""
Go LSP Client Documentation Extractor
Downloads and documents the tectiv3/go-lsp-client library.
go-lsp-client is a Go client library for Language Server Protocol servers.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/tectiv3/go-lsp-client.git"
REPO_BRANCH = "master"

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "go-lsp-client"

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


def extract_go_code_as_markdown(go_file_path, output_dir):
    """Extract Go source code with comments as markdown documentation."""
    try:
        with open(go_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Create a markdown file documenting the Go source
        file_name = go_file_path.name
        md_file = output_dir / f"{file_name[:-3]}.md"  # Replace .go with .md

        # Create markdown content with source header and code block
        source_url = f"https://github.com/tectiv3/go-lsp-client/blob/{REPO_BRANCH}/{file_name}"
        md_content = f"""# Source: {source_url}

# {file_name}

## Go Source Code

```go
{content}
```
"""

        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(md_content)

        return True

    except Exception as e:
        print(f"    -> Error extracting {go_file_path.name}: {e}")
        return False


def copy_documentation(source_dir, output_dir):
    """Copy and create documentation files from source to output directory."""
    try:
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        # Copy README
        readme_file = Path(source_dir) / "README.md"
        if readme_file.exists():
            with open(readme_file, 'r', encoding='utf-8') as f:
                original_content = f.read()

            source_url = f"https://github.com/tectiv3/go-lsp-client/blob/{REPO_BRANCH}/README.md"
            header = f"""# Source: {source_url}

"""
            new_content = header + original_content

            with open(output_dir / "README.md", 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"    -> Copied README.md")

        # Extract main Go source files as markdown documentation
        go_files = [
            "client.go",
            "server.go",
            "message.go",
            "models.go",
            "util.go",
            "htmlFormatter.go",
        ]

        for go_file in go_files:
            go_path = Path(source_dir) / go_file
            if go_path.exists():
                extract_go_code_as_markdown(go_path, output_dir)
                print(f"    -> Extracted {go_file} as markdown")

        # Copy LICENSE
        license_file = Path(source_dir) / "LICENSE"
        if license_file.exists():
            shutil.copy2(license_file, output_dir / "LICENSE")
            print(f"    -> Copied LICENSE")

        # Copy go.mod for dependency information
        go_mod_file = Path(source_dir) / "go.mod"
        if go_mod_file.exists():
            with open(go_mod_file, 'r', encoding='utf-8') as f:
                mod_content = f.read()

            source_url = f"https://github.com/tectiv3/go-lsp-client/blob/{REPO_BRANCH}/go.mod"
            header = f"""# Source: {source_url}

# Module Dependencies

```
{mod_content}
```
"""
            with open(output_dir / "go-mod.md", 'w', encoding='utf-8') as f:
                f.write(header)
            print(f"    -> Copied go.mod as documentation")

        return True

    except Exception as e:
        print(f"    -> Error copying documentation: {e}")
        return False


def main():
    """Main function to extract go-lsp-client documentation."""
    print("=" * 70)
    print("Go LSP Client Documentation Extractor")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "go-lsp-client"

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
        print("\nCopying and extracting documentation files...")

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

    md_files = list(output_dir.glob("*.md"))
    total_size = sum(f.stat().st_size for f in output_dir.rglob("*") if f.is_file())

    print(f"  Total markdown files: {len(md_files)}")
    print(f"  Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")

    if len(md_files) == 0:
        print("\n  Warning: No markdown files found in output directory")
        sys.exit(1)

    # List main files
    print("\n  Main documentation files:")
    for md_file in sorted(md_files)[:10]:
        file_size = md_file.stat().st_size
        print(f"    - {md_file.name} ({file_size:,} bytes)")

    if len(md_files) > 10:
        print(f"    ... and {len(md_files) - 10} more files")

    print()
    print("=" * 70)
    print("Extraction Complete")
    print("=" * 70)
    print(f"Output: {output_dir}")
    print()


if __name__ == "__main__":
    main()
