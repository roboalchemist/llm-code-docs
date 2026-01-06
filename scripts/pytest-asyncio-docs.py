#!/usr/bin/env python3
"""
pytest-asyncio Documentation Scraper
Extracts documentation from pytest-asyncio GitHub repository and converts to markdown.
pytest-asyncio is a pytest plugin for testing asyncio code with native async/await support.
"""

import os
import sys
import requests
from pathlib import Path
import time
import re
from typing import Optional

# GitHub raw content base URL
GITHUB_BASE = "https://raw.githubusercontent.com/pytest-dev/pytest-asyncio/main/docs"

# Documentation files to extract (in order of importance)
DOCS_FILES = [
    "index.rst",
    "concepts.rst",
    "support.rst",
    "concepts_concurrent_execution_example.py",
    "concepts_function_scope_example.py",
    "concepts_module_scope_example.py",
]

REQUEST_DELAY = 0.3  # seconds between requests


def rst_to_markdown(rst_content: str) -> str:
    """
    Convert reStructuredText to markdown.
    This is a basic converter for common RST patterns.
    """
    content = rst_content

    # Add source header
    content = "# Source: pytest-asyncio GitHub Repository\n\n" + content

    # Convert RST titles
    # .. title:: becomes just the title
    content = re.sub(r'\.\. title:: (.*?)$', r'# \1', content, flags=re.MULTILINE)

    # Convert overline/underline titles to markdown headers
    # Lines with === or --- underneath become headers
    lines = content.split('\n')
    result = []
    i = 0
    while i < len(lines):
        if i + 1 < len(lines):
            current = lines[i].strip()
            next_line = lines[i + 1].strip()

            # Check for underlined headers (===, ---, ~~~, etc.)
            if current and next_line and len(next_line) >= len(current):
                if all(c == '=' for c in next_line):
                    result.append(f"# {current}")
                    i += 2
                    continue
                elif all(c == '-' for c in next_line):
                    result.append(f"## {current}")
                    i += 2
                    continue
                elif all(c == '~' for c in next_line):
                    result.append(f"### {current}")
                    i += 2
                    continue

        result.append(lines[i])
        i += 1

    content = '\n'.join(result)

    # Convert inline code markup FIRST (before other conversions)
    # ``code`` -> `code` (but not ```code```)
    content = re.sub(r'(?<!`)``([^`\n]+?)``(?!`)', r'`\1`', content)

    # Convert RST directives
    # .. code-block:: python -> ```python
    content = re.sub(r'\.\. code-block:: (\w+)', r'```\1', content)
    # .. code-block:: without language
    content = re.sub(r'\.\. code-block::', r'```python', content)

    # Convert RST include directives
    # .. include:: file.py -> Include content reference
    content = re.sub(r'\.\. include:: ([^\n]+)\n\s+:code: (\w+)', r'```\2\n[See: \1]\n```', content)
    content = re.sub(r'\.\. include:: ([^\n]+)', r'[Include: \1]', content)

    # Replace empty ``` closures with proper markdown
    content = re.sub(r'(\n```)\n', r'\1\n', content)

    # Convert RST note/warning directives to markdown blockquotes
    content = re.sub(r'\.\. note::\n\s+(.*?)(?=\n\n|\n\.\.|\Z)', r'> **Note:** \1', content, flags=re.DOTALL)
    content = re.sub(r'\.\. warning::\n\s+(.*?)(?=\n\n|\n\.\.|\Z)', r'> **Warning:** \1', content, flags=re.DOTALL)
    content = re.sub(r'\.\. caution::\n\s+(.*?)(?=\n\n|\n\.\.|\Z)', r'> **Caution:** \1', content, flags=re.DOTALL)
    content = re.sub(r'\.\. tip::\n\s+(.*?)(?=\n\n|\n\.\.|\Z)', r'> **Tip:** \1', content, flags=re.DOTALL)

    # Convert RST links
    # `text <url>`_ -> [text](url)
    content = re.sub(r'`([^<>`]+)\s+<([^>]+)>`_', r'[\1](\2)', content)
    # Reference links `text`_ -> [text]
    content = re.sub(r'`([^`]+)`_', r'[\1]', content)

    # Convert RST emphasis
    # *emphasis* -> *emphasis*
    # **strong** -> **strong**
    # Both are already markdown compatible

    # Clean up broken reference links like <pytest-asyncio-event-loops>
    content = re.sub(r'<([^>]+)>', r'[\1]', content)

    # Convert RST lists
    # * item -> * item (already compatible)
    # # item -> 1. item (auto-numbered)

    # Convert RST line blocks (|)
    content = re.sub(r'^\| ', '', content, flags=re.MULTILINE)

    # Remove RST-specific directives that have no markdown equivalent
    content = re.sub(r'\.\. toctree::.*?(?=\n\n|\Z)', '', content, flags=re.DOTALL)
    # Remove RST anchor references .. _ref-name:
    content = re.sub(r'^\.\. _[^:]+:\s*$', '', content, flags=re.MULTILINE)

    # Convert RST role references like :ref:`label` to just the label
    content = re.sub(r':ref:`([^`]+)`', r'[\1]', content)
    # Convert other role references like :py:func:`name` to just name
    content = re.sub(r':\w+:`([^`]+)`', r'[\1]', content)

    # Remove empty lines at the start
    content = content.lstrip('\n')

    # Normalize spacing
    content = re.sub(r'\n\n\n+', '\n\n', content)

    return content


def sanitize_filename(filepath: str) -> str:
    """Convert GitHub filepath to safe filename."""
    # Get the filename from the path
    filename = Path(filepath).name

    # Replace .rst with .md
    if filename.endswith('.rst'):
        filename = filename[:-4] + '.md'
    # Keep .py files as is
    elif filename.endswith('.py'):
        return filename
    elif not filename.endswith('.md'):
        filename = filename + '.md'

    return filename


def get_output_dir(filepath: str, base_output: Path) -> Path:
    """Determine output subdirectory based on source filepath."""
    path_parts = Path(filepath).parts

    # Create subdirectories based on source structure
    if len(path_parts) > 1 and path_parts[0] != 'index.rst':
        # Create subdirectory for files in subfolders
        subdir = base_output / path_parts[0]
        subdir.mkdir(parents=True, exist_ok=True)
        return subdir

    return base_output


def download_file(filepath: str, output_base: Path) -> bool:
    """Download and convert a single documentation file."""
    try:
        url = f"{GITHUB_BASE}/{filepath}"

        print(f"  Downloading: {filepath}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        file_content = response.text

        # Convert RST to Markdown (only for .rst files)
        if filepath.endswith('.rst'):
            file_content = rst_to_markdown(file_content)

        # Determine output directory and filename
        output_dir = get_output_dir(filepath, output_base)
        filename = sanitize_filename(filepath)
        output_path = output_dir / filename

        # Write to file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(file_content)

        print(f"    -> Saved: {output_path.relative_to(output_base)}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {filepath}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {filepath}: {e}")
        return False


def main():
    """Main function to download pytest-asyncio documentation."""
    print("=" * 60)
    print("pytest-asyncio Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "pytest-asyncio"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Download all documentation files
    print("Downloading documentation files...")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, filepath in enumerate(DOCS_FILES, 1):
        print(f"[{idx:2d}/{len(DOCS_FILES)}] ", end="")

        if download_file(filepath, output_dir):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(REQUEST_DELAY)

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
    total_size = sum(f.stat().st_size for f in output_dir.glob("**/*.md"))
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
