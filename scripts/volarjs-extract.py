#!/usr/bin/env python3
"""
Volar.js Documentation Extractor
Downloads documentation from the Volar.js GitHub repository.
Extracts MDX documentation files and converts them to Markdown.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/volarjs/docs.git"
REPO_BRANCH = "main"
SOURCE_DOCS_FOLDER = "src/content/docs"

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "volarjs-docs"

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


def convert_mdx_to_markdown(mdx_content, mdx_file_path):
    """
    Convert MDX format to Markdown.
    MDX is Markdown with JSX, so we extract the markdown content.
    """
    lines = mdx_content.split('\n')
    markdown_lines = []
    in_jsx_component = False
    skip_next = False

    for i, line in enumerate(lines):
        # Skip JSX import statements
        if line.strip().startswith('import '):
            skip_next = True
            continue

        if skip_next and (line.strip() == '' or not line.strip().startswith('import')):
            skip_next = False

        # Skip pure JSX components on their own lines
        if line.strip().startswith('<') and line.strip().endswith('/>'):
            # Self-closing JSX component
            continue

        if line.strip().startswith('<') and not line.strip().startswith('<!--'):
            in_jsx_component = True
            continue

        if in_jsx_component:
            if line.strip().startswith('>') or line.strip().endswith('>'):
                in_jsx_component = False
            continue

        # Keep the line as-is for markdown content
        markdown_lines.append(line)

    # Remove leading/trailing empty lines
    while markdown_lines and not markdown_lines[0].strip():
        markdown_lines.pop(0)
    while markdown_lines and not markdown_lines[-1].strip():
        markdown_lines.pop()

    return '\n'.join(markdown_lines)


def copy_documentation(source_dir, output_dir):
    """Copy documentation files from source to output directory."""
    try:
        print(f"  Copying documentation from {source_dir} to {output_dir}")

        # Create output directory if it doesn't exist
        output_dir.mkdir(parents=True, exist_ok=True)

        source_docs = Path(source_dir) / SOURCE_DOCS_FOLDER
        if not source_docs.exists():
            print(f"    -> Source docs folder not found: {source_docs}")
            return False

        # Copy all documentation files recursively
        file_count = 0
        for doc_file in source_docs.rglob('*'):
            if doc_file.is_file():
                # Calculate relative path from source_docs
                relative_path = doc_file.relative_to(source_docs)
                target_file = output_dir / relative_path

                # Create parent directories if needed
                target_file.parent.mkdir(parents=True, exist_ok=True)

                # Handle different file types
                if doc_file.suffix in ['.mdx', '.md']:
                    try:
                        with open(doc_file, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()

                        # Convert MDX to Markdown
                        markdown_content = convert_mdx_to_markdown(content, doc_file)

                        # Save as .md for consistency
                        target_file = target_file.with_suffix('.md')
                        with open(target_file, 'w', encoding='utf-8') as f:
                            source_url = REPO_URL.replace('.git', '')
                            doc_path = str(relative_path).replace('\\', '/')
                            f.write(f"# Source: {source_url}/blob/{REPO_BRANCH}/{SOURCE_DOCS_FOLDER}/{doc_path}\n\n")
                            f.write(markdown_content)

                        file_count += 1
                        print(f"    -> Processed: {relative_path}")
                    except Exception as e:
                        print(f"    -> Error processing {doc_file.name}: {e}")
                        continue
                elif doc_file.suffix in ['.png', '.jpg', '.jpeg', '.gif', '.svg']:
                    # Copy image files as-is
                    shutil.copy2(doc_file, target_file)
                    file_count += 1
                    print(f"    -> Copied image: {relative_path}")
                else:
                    # Copy other files as-is
                    shutil.copy2(doc_file, target_file)
                    file_count += 1

        if file_count == 0:
            print(f"    -> No documentation files found in {source_docs}")
            return False

        print(f"    -> Copied {file_count} documentation files")
        return True

    except Exception as e:
        print(f"    -> Error copying documentation: {e}")
        return False


def main():
    """Main extraction function."""
    print("Volar.js Documentation Extractor")
    print("-" * 50)

    # Create output directory path
    output_dir = Path(__file__).parent.parent / "docs" / "github-scraped" / "volarjs"

    # Create temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        # Clone repository
        repo_path = clone_repository(temp_dir, REPO_URL, REPO_BRANCH)
        if not repo_path:
            print("Failed to clone repository")
            return False

        # Remove old output directory if it exists
        if output_dir.exists():
            print(f"  Removing existing output directory: {output_dir}")
            shutil.rmtree(output_dir)

        # Copy documentation
        if not copy_documentation(repo_path, output_dir):
            print("Failed to copy documentation")
            return False

        # Verify extraction
        file_count = len(list(output_dir.rglob('*')))
        if file_count == 0:
            print("No files were extracted")
            return False

        print(f"\nSuccessfully extracted {file_count} files to {output_dir}")
        return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
