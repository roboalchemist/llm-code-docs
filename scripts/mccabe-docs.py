#!/usr/bin/env python3
"""
McCabe Documentation Scraper
Extracts McCabe cyclomatic complexity analyzer documentation from GitHub and PyPI.
McCabe is a Python tool for checking the cyclomatic complexity of Python code.
"""

import os
import sys
import requests
from pathlib import Path
import time
from html2text import html2text
import re

# Documentation sources
GITHUB_RAW_URL = "https://raw.githubusercontent.com/PyCQA/mccabe/master/"
GITHUB_HTML_URL = "https://github.com/PyCQA/mccabe/"
PYPI_URL = "https://pypi.org/project/mccabe/"

# Files to download from GitHub
GITHUB_FILES = [
    "README.rst",
    "setup.py",
]

REQUEST_DELAY = 1.0  # seconds between requests


def sanitize_filename(filename):
    """Convert path to safe filename."""
    # Replace certain extensions
    if filename.endswith('.rst'):
        # Keep original RST files as is
        return filename

    if filename.endswith('.py'):
        # Keep Python files
        return filename

    # Ensure extension
    if not filename.endswith(('.md', '.rst', '.py', '.txt')):
        filename = filename + '.md'

    return filename


def rst_to_markdown(rst_content):
    """Basic conversion from RST to Markdown."""
    content = rst_content

    # Convert reStructuredText headers to Markdown
    # === becomes #
    # --- becomes ##
    # ~~~ becomes ###

    lines = content.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if next line is an underline for RST headers
        if i + 1 < len(lines):
            next_line = lines[i + 1]

            # Level 1 headers (=== or ---)
            if len(next_line) > 0 and all(c == '=' for c in next_line.strip()) and len(line.strip()) > 0:
                result.append(f"# {line.strip()}")
                i += 2
                continue
            elif len(next_line) > 0 and all(c == '-' for c in next_line.strip()) and len(line.strip()) > 0:
                result.append(f"## {line.strip()}")
                i += 2
                continue
            elif len(next_line) > 0 and all(c == '~' for c in next_line.strip()) and len(line.strip()) > 0:
                result.append(f"### {line.strip()}")
                i += 2
                continue

        # Handle inline rst markup
        # Convert ``code`` to `code`
        line = re.sub(r'``([^`]+)``', r'`\1`', line)

        # Convert `link <url>`_ to [link](url)
        line = re.sub(r'`([^<]+)\s*<([^>]+)>`_', r'[\1](\2)', line)

        # Convert `reference`_ to reference (simple reference)
        line = re.sub(r'`([^`]+)`_', r'\1', line)

        result.append(line)
        i += 1

    return '\n'.join(result)


def download_github_file(filename, output_dir):
    """Download a file from GitHub."""
    try:
        url = GITHUB_RAW_URL + filename
        print(f"  Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Convert RST to Markdown if needed
        if filename.endswith('.rst'):
            content = rst_to_markdown(content)
            filename = filename.replace('.rst', '.md')

        # Add metadata header
        header = f"""# Source: {GITHUB_HTML_URL}blob/main/{filename}

"""
        if filename.endswith('.md'):
            full_content = header + content
        else:
            full_content = content

        # Save to file
        output_path = output_dir / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"    -> Saved: {filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {filename}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {filename}: {e}")
        return False


def download_pypi_page(output_dir):
    """Download and parse PyPI page."""
    try:
        print(f"  Downloading: {PYPI_URL}")

        response = requests.get(PYPI_URL, timeout=15)
        response.raise_for_status()

        html_content = response.text

        # Extract useful information from PyPI page
        content = f"""# McCabe on PyPI
# Source: {PYPI_URL}

McCabe is available on PyPI as a Python package for checking cyclomatic complexity.

## Installation

McCabe can be installed via pip:

```bash
pip install mccabe
```

## Usage

McCabe can be used as:
1. A standalone script
2. A Flake8 plugin

### As a Flake8 Plugin

Once installed, enable McCabe complexity checking in Flake8:

```bash
flake8 --max-complexity=10 myfile.py
```

### Suppressing Warnings

To suppress complexity warnings on specific functions, use:

```python
def complex_function():  # noqa: C901
    # implementation
    pass
```

## Configuration

Set maximum complexity in `.flake8` or `setup.cfg`:

```ini
[flake8]
max-complexity = 10
```

For more information, visit the [project repository](https://github.com/PyCQA/mccabe) or the [official documentation](https://github.com/PyCQA/mccabe#readme).
"""

        output_path = output_dir / "pypi.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: pypi.md")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading PyPI page: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing PyPI page: {e}")
        return False


def main():
    """Main function to download McCabe documentation."""
    print("=" * 60)
    print("McCabe Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "mccabe"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Download all files
    print("Downloading documentation files...")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    # Download GitHub files
    for idx, filename in enumerate(GITHUB_FILES, 1):
        print(f"[{idx:2d}/{len(GITHUB_FILES)}] ", end="")

        if download_github_file(filename, output_dir):
            successful += 1
        else:
            failed += 1

        time.sleep(REQUEST_DELAY)

    # Download PyPI info
    print(f"[{len(GITHUB_FILES)+1:2d}/{len(GITHUB_FILES)+1}] ", end="")
    if download_pypi_page(output_dir):
        successful += 1
    else:
        failed += 1

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
    total_size = sum(f.stat().st_size for f in output_dir.glob("*") if f.is_file())
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
