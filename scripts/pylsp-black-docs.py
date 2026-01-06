#!/usr/bin/env python3
"""
python-lsp-black Documentation Scraper
Extracts documentation from python-lsp-black GitHub repository and converts to markdown.
python-lsp-black is a Black code formatter plugin for the Python LSP Server.
"""

import os
import sys
import requests
from pathlib import Path
import time
from typing import Optional

# GitHub raw content base URL
GITHUB_BASE = "https://raw.githubusercontent.com/python-lsp/python-lsp-black/master"

# Documentation files to extract
DOCS_FILES = [
    "README.md",
]

REQUEST_DELAY = 0.3  # seconds between requests


def add_source_header(content: str, url: str) -> str:
    """Add source header to markdown content."""
    return f"# Source: {url}\n\n{content}"


def download_file(filepath: str, output_base: Path) -> bool:
    """Download and process a single documentation file."""
    try:
        url = f"{GITHUB_BASE}/{filepath}"

        print(f"  Downloading: {filepath}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        file_content = response.text

        # Add source header
        file_content = add_source_header(file_content, f"https://github.com/python-lsp/python-lsp-black")

        # Determine output filename
        filename = Path(filepath).name
        output_path = output_base / filename

        # Write to file
        output_base.mkdir(parents=True, exist_ok=True)
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


def create_api_reference(output_dir: Path) -> bool:
    """Create API reference documentation for python-lsp-black."""
    try:
        api_content = """# Source: https://github.com/python-lsp/python-lsp-black

# API Reference

## Configuration Options

python-lsp-black provides the following configuration keys for the Python LSP Server:

### pylsp.plugins.black.enabled
- **Type**: boolean
- **Default**: `true`
- **Description**: Enable or disable the Black code formatter plugin.
- **Example**:
  ```json
  {
    "pylsp.plugins.black.enabled": true
  }
  ```

### pylsp.plugins.black.cache_config
- **Type**: boolean
- **Default**: `false`
- **Description**: Enable configuration caching to improve performance. When enabled, Black configuration is cached and LSP server restart is required if Black settings change.
- **Example**:
  ```json
  {
    "pylsp.plugins.black.cache_config": false
  }
  ```

### pylsp.plugins.black.line_length
- **Type**: integer
- **Default**: `88`
- **Description**: Set the maximum line length for code formatting.
- **Example**:
  ```json
  {
    "pylsp.plugins.black.line_length": 88
  }
  ```

### pylsp.plugins.black.preview
- **Type**: boolean
- **Default**: `false`
- **Description**: Enable Black's preview-style formatting (features that are experimental or not yet stable).
- **Example**:
  ```json
  {
    "pylsp.plugins.black.preview": false
  }
  ```

### pylsp.plugins.black.skip_string_normalization
- **Type**: boolean
- **Default**: `false`
- **Description**: Disable string quote normalization. When enabled, Black will not normalize quote characters in strings.
- **Example**:
  ```json
  {
    "pylsp.plugins.black.skip_string_normalization": false
  }
  ```

### pylsp.plugins.black.skip_magic_trailing_comma
- **Type**: boolean
- **Default**: `false`
- **Description**: Control trailing comma handling. When enabled, Black will not use magic trailing commas.
- **Example**:
  ```json
  {
    "pylsp.plugins.black.skip_magic_trailing_comma": false
  }
  ```

## LSP Formatting Methods

### Document Formatting

python-lsp-black integrates with the LSP document formatting protocol. When enabled, it formats entire files.

**Method**: `textDocument/formatting`

**Supported in**:
- VSCode via python-lsp-client extensions
- Vim/Neovim via coc-pyls or similar
- Emacs via lsp-pyls
- Other LSP-compatible editors

### Range Formatting

python-lsp-black supports formatting specific ranges of code within a document.

**Method**: `textDocument/rangeFormatting`

**Note**: Text selections are treated as separate Python files, so indented code blocks within functions may not format correctly if selected in isolation.

## Integration with python-lsp-server

python-lsp-black is a plugin for python-lsp-server and must be installed in the same virtual environment:

```bash
# Install python-lsp-server and python-lsp-black together
pip install python-lsp-server python-lsp-black
```

### Disabling Conflicting Formatters

If you have other formatting plugins enabled, you should disable them to avoid conflicts:

```json
{
  "pylsp.plugins.black.enabled": true,
  "pylsp.plugins.autopep8.enabled": false,
  "pylsp.plugins.yapf.enabled": false
}
```

### Configuration in Editor Settings

#### VSCode

In `.vscode/settings.json`:
```json
{
  "pylsp.plugins.black.enabled": true,
  "pylsp.plugins.black.line_length": 100
}
```

#### Vim/Neovim (with coc-pyls)

In `coc-settings.json`:
```json
{
  "pylsp.plugins.black.enabled": true,
  "pylsp.plugins.black.line_length": 100
}
```

## Behavior Notes

- **Syntactically Valid Code Only**: Black (and therefore python-lsp-black) only formats syntactically valid Python code. Incomplete or malformed code will not be formatted.
- **Configuration Files**: The plugin respects project-level `pyproject.toml` configurations for Black settings.
- **Performance**: Use `cache_config: true` for better performance in large projects, but remember to restart the LSP server when Black settings change.

## See Also

- [Black Documentation](https://black.readthedocs.io/)
- [Python LSP Server](https://github.com/python-lsp/python-lsp-server)
- [python-lsp-black GitHub Repository](https://github.com/python-lsp/python-lsp-black)
"""

        output_path = output_dir / "API_REFERENCE.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(api_content)

        print(f"  Created: API_REFERENCE.md")
        return True

    except Exception as e:
        print(f"    -> Error creating API reference: {e}")
        return False


def main():
    """Main function to download python-lsp-black documentation."""
    print("=" * 60)
    print("python-lsp-black Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "pylsp-black"
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

    # Create API reference documentation
    print()
    print("Creating API reference documentation...")
    if create_api_reference(output_dir):
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
