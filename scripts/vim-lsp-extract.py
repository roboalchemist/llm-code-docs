#!/usr/bin/env python3
"""
vim-lsp Documentation Extractor
Downloads documentation from the vim-lsp GitHub repository.
Extracts Vim help files for the LSP plugin.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/prabirshrestha/vim-lsp.git"
REPO_BRANCH = "master"
SOURCE_DOCS_FOLDER = "doc"

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "vim-lsp"

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


def convert_vim_help_to_markdown(vim_help_content):
    """
    Convert Vim help file format to Markdown.
    Vim help files use special formatting that we'll convert to Markdown.
    """
    lines = vim_help_content.split('\n')
    markdown_lines = []
    in_code_block = False

    for line in lines:
        # Convert Vim help headers (tags in tildes) to Markdown
        if '~' in line and len(line.strip()) > 4:
            # This is typically a help file header
            markdown_lines.append(f"# {line.strip()}")
            continue

        # Convert inline code references (backtick style)
        if line.startswith('\t'):
            # Indented lines become code blocks
            if not in_code_block:
                markdown_lines.append('```')
                in_code_block = True
            markdown_lines.append(line[1:])  # Remove tab
        else:
            if in_code_block:
                markdown_lines.append('```')
                in_code_block = False
            # Convert *word* style tags to bold
            line = line.replace('*', '**')
            # Convert `word` style tags appropriately
            markdown_lines.append(line)

    if in_code_block:
        markdown_lines.append('```')

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

        # Copy all documentation files
        file_count = 0
        for doc_file in source_docs.glob('*.*'):
            if doc_file.is_file():
                target_file = output_dir / doc_file.name

                # If it's a Vim help file (.txt), read it and potentially process
                if doc_file.suffix == '.txt':
                    try:
                        with open(doc_file, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()

                        # For Vim help files, try to convert key sections to markdown
                        # For now, keep them as markdown with appropriate formatting
                        markdown_content = convert_vim_help_to_markdown(content)

                        # Save as .md for consistency
                        target_file = output_dir / f"{doc_file.stem}.md"
                        with open(target_file, 'w', encoding='utf-8') as f:
                            f.write(f"# Source: {REPO_URL.replace('.git', '')}/blob/{REPO_BRANCH}/doc/{doc_file.name}\n\n")
                            f.write(markdown_content)

                        file_count += 1
                    except Exception as e:
                        print(f"    -> Error processing {doc_file.name}: {e}")
                        continue
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
    print("vim-lsp Documentation Extractor")
    print("-" * 50)

    # Create output directory path
    output_dir = Path(__file__).parent.parent / "docs" / "github-scraped" / "vim-lsp"

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
        file_count = len(list(output_dir.glob('*')))
        if file_count == 0:
            print("No files were extracted")
            return False

        print(f"\nSuccessfully extracted {file_count} files to {output_dir}")
        return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
