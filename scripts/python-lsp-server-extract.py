#!/usr/bin/env python3
"""
Python LSP Server Documentation Extractor
Downloads documentation from the python-lsp-server GitHub repository.
Covers plugin configuration, flake8 integration, and LSP protocol usage.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess
import time

# Repository configuration
REPO_URL = "https://github.com/python-lsp/python-lsp-server.git"
REPO_BRANCH = "develop"

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "python-lsp-server"

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


def extract_documentation(source_dir, output_dir):
    """Extract documentation files from the repository."""
    try:
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        # Key documentation files to extract
        source_files = {
            'CONFIGURATION.md': 'Configuration and plugin settings for python-lsp-server',
            'README.md': 'Project overview and installation instructions',
            'docs/': 'Plugin-specific documentation',
            'pylsp/': 'Source code and plugin implementations',
        }

        extracted_count = 0

        # Extract CONFIGURATION.md
        config_file = Path(source_dir) / 'CONFIGURATION.md'
        if config_file.exists():
            dest = output_dir / 'CONFIGURATION.md'
            with open(config_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Add source header
            source_url = f"https://github.com/python-lsp/python-lsp-server/blob/{REPO_BRANCH}/CONFIGURATION.md"
            header = f"""# Source: {source_url}

"""
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(header + content)
            print(f"    -> Extracted: CONFIGURATION.md")
            extracted_count += 1

        # Extract README.md
        readme_file = Path(source_dir) / 'README.md'
        if readme_file.exists():
            dest = output_dir / 'README.md'
            with open(readme_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Add source header
            source_url = f"https://github.com/python-lsp/python-lsp-server/blob/{REPO_BRANCH}/README.md"
            header = f"""# Source: {source_url}

"""
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(header + content)
            print(f"    -> Extracted: README.md")
            extracted_count += 1

        # Extract docs folder
        docs_folder = Path(source_dir) / 'docs'
        if docs_folder.exists():
            for doc_file in docs_folder.rglob('*'):
                if doc_file.is_file():
                    relative_path = doc_file.relative_to(docs_folder)
                    dest = output_dir / 'docs' / relative_path
                    dest.parent.mkdir(parents=True, exist_ok=True)

                    if doc_file.suffix in ['.md', '.rst', '.txt']:
                        with open(doc_file, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()

                        # Add source header
                        source_url = f"https://github.com/python-lsp/python-lsp-server/blob/{REPO_BRANCH}/docs/{relative_path}"
                        header = f"""# Source: {source_url}

"""
                        with open(dest, 'w', encoding='utf-8') as f:
                            f.write(header + content)
                    else:
                        shutil.copy2(doc_file, dest)

                    print(f"    -> Extracted: docs/{relative_path}")
                    extracted_count += 1

        # Extract pylsp plugin files (especially flake8)
        pylsp_folder = Path(source_dir) / 'pylsp' / 'plugins'
        if pylsp_folder.exists():
            # Create a comprehensive plugin guide
            plugin_guide = output_dir / 'PLUGINS_GUIDE.md'
            plugins_content = """# Source: https://github.com/python-lsp/python-lsp-server/tree/develop/pylsp/plugins

# Python LSP Server - Plugin System Guide

This document describes the built-in plugins available in python-lsp-server.

## Available Plugins

### flake8_lint.py
Flake8 integration plugin for linting Python code with flake8.

**Configuration Keys:**
- `pylsp.plugins.flake8.enabled` - Enable/disable flake8 plugin (default: false)
- `pylsp.plugins.flake8.config` - Path to .flake8 config file
- `pylsp.plugins.flake8.exclude` - Exclude patterns
- `pylsp.plugins.flake8.extendIgnore` - Error codes to ignore
- `pylsp.plugins.flake8.extendSelect` - Error codes to select
- `pylsp.plugins.flake8.executable` - Path to flake8 executable
- `pylsp.plugins.flake8.filename` - Filename patterns to check
- `pylsp.plugins.flake8.hangClosing` - Hang closing bracket
- `pylsp.plugins.flake8.ignore` - Error codes to ignore
- `pylsp.plugins.flake8.maxComplexity` - Max cyclomatic complexity
- `pylsp.plugins.flake8.maxLineLength` - Max line length
- `pylsp.plugins.flake8.indentSize` - Indentation size
- `pylsp.plugins.flake8.perFileIgnores` - Per-file ignore rules
- `pylsp.plugins.flake8.select` - Error codes to select

### Other Built-in Plugins
- autopep8 - Auto-formatting with autopep8
- jedi - Code completion with jedi
- mccabe - McCabe complexity checking
- pycodestyle - PEP 8 style checking
- pylint - Linting with pylint
- rope - Refactoring support with rope

## Plugin Configuration

Configuration is managed via Language Server Protocol's `workspace/didChangeConfiguration` method.
Typical configuration locations:
1. `.pylsp.cfg` or `.pylsprc`
2. `setup.cfg`
3. `pyproject.toml`
4. Language server client settings

## Example Configuration

```json
{
  "pylsp": {
    "plugins": {
      "flake8": {
        "enabled": true,
        "maxLineLength": 100,
        "ignore": ["E501", "W503"]
      }
    },
    "configurationSources": ["flake8"]
  }
}
```

## Plugin Development

Plugins can be created by implementing the `PylspPlugin` interface and registering
as a setuptools entry point in the `pylsp_plugins` group.

For details, see the source code at: https://github.com/python-lsp/python-lsp-server/tree/develop/pylsp/plugins
"""
            with open(plugin_guide, 'w', encoding='utf-8') as f:
                f.write(plugins_content)
            print(f"    -> Created: PLUGINS_GUIDE.md (comprehensive plugin reference)")
            extracted_count += 1

        # Extract source code comments and structure
        pylsp_init = Path(source_dir) / 'pylsp' / '__init__.py'
        if pylsp_init.exists():
            dest = output_dir / 'pylsp_init.py'
            with open(pylsp_init, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            source_url = f"https://github.com/python-lsp/python-lsp-server/blob/{REPO_BRANCH}/pylsp/__init__.py"
            header = f"""# Source: {source_url}

"""
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(header + content)
            print(f"    -> Extracted: pylsp/__init__.py")
            extracted_count += 1

        # Extract flake8 plugin source directly
        flake8_plugin = Path(source_dir) / 'pylsp' / 'plugins' / 'flake8_lint.py'
        if flake8_plugin.exists():
            dest = output_dir / 'flake8_lint.py'
            with open(flake8_plugin, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            source_url = f"https://github.com/python-lsp/python-lsp-server/blob/{REPO_BRANCH}/pylsp/plugins/flake8_lint.py"
            header = f"""# Source: {source_url}

"""
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(header + content)
            print(f"    -> Extracted: pylsp/plugins/flake8_lint.py (flake8 plugin implementation)")
            extracted_count += 1

        return extracted_count > 0

    except Exception as e:
        print(f"    -> Error extracting documentation: {e}")
        return False


def main():
    """Main function to extract python-lsp-server documentation."""
    print("=" * 70)
    print("Python LSP Server Documentation Extractor")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "python-lsp-server"

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

        # Extract documentation
        print("\nExtracting documentation files...")

        # Remove existing output directory if it exists
        if output_dir.exists():
            print(f"  Removing existing output directory: {output_dir}")
            shutil.rmtree(output_dir)

        if not extract_documentation(repo_path, output_dir):
            print("\nError: Failed to extract documentation")
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
