#!/usr/bin/env python3
"""
ESLint Plugin React Hooks Documentation Scraper
Downloads eslint-plugin-react-hooks documentation from GitHub repository and react.dev.
eslint-plugin-react-hooks is the official ESLint plugin enforcing React Hooks rules and best practices.
"""

import os
import sys
import shutil
import tempfile
import subprocess
from pathlib import Path
from urllib.parse import urljoin

def clone_react_repository(temp_dir):
    """Clone the React repository to get eslint-plugin-react-hooks package documentation."""
    try:
        print(f"  Cloning React repository (eslint-plugin-react-hooks package)...")
        clone_path = Path(temp_dir) / "react"

        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", "main",
             "https://github.com/facebook/react.git", str(clone_path)],
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
    """Copy documentation files from eslint-plugin-react-hooks package to output directory."""
    try:
        package_dir = Path(source_dir) / "packages" / "eslint-plugin-react-hooks"

        if not package_dir.exists():
            print(f"    -> Package directory not found: {package_dir}")
            return False

        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        files_copied = 0

        # Copy README.md
        readme_file = package_dir / "README.md"
        if readme_file.exists():
            with open(readme_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Add source header
            source_url = "https://github.com/facebook/react/blob/main/packages/eslint-plugin-react-hooks/README.md"
            header = f"""# Source: {source_url}

"""
            new_content = header + content

            output_file = output_dir / "README.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"    -> Copied file: README.md")
            files_copied += 1

        # Copy CHANGELOG.md
        changelog_file = package_dir / "CHANGELOG.md"
        if changelog_file.exists():
            with open(changelog_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Add source header
            source_url = "https://github.com/facebook/react/blob/main/packages/eslint-plugin-react-hooks/CHANGELOG.md"
            header = f"""# Source: {source_url}

"""
            new_content = header + content

            output_file = output_dir / "CHANGELOG.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"    -> Copied file: CHANGELOG.md")
            files_copied += 1

        # Create a documentation index file with reference to react.dev
        index_content = """# Source: https://react.dev/reference/eslint-plugin-react-hooks

# ESLint Plugin React Hooks Documentation Index

The official ESLint plugin for React which enforces the Rules of React and other best practices.

## Official Documentation

- **Main Documentation**: https://react.dev/reference/eslint-plugin-react-hooks
- **Rules of Hooks**: https://react.dev/reference/rules/rules-of-hooks
- **GitHub Repository**: https://github.com/facebook/react/tree/main/packages/eslint-plugin-react-hooks

## Quick Links

### Installation & Configuration
- Installation instructions are in README.md
- Flat config (ESLint 9+) with recommended presets
- Legacy config support (.eslintrc) for ESLint < 9

### Core Rules
- **rules-of-hooks**: Enforces the Rules of Hooks
- **exhaustive-deps**: Validates dependency arrays in effects and callbacks

### React Compiler Rules
The plugin includes additional rules for the React Compiler:
- config
- error-boundaries
- component-hook-factories
- gating
- globals
- immutability
- preserve-manual-memoization
- purity
- refs
- set-state-in-effect
- set-state-in-render
- static-components
- unsupported-syntax
- use-memo
- incompatible-library

### Configuration Options
- **additionalHooks**: Configure custom Hooks validation with exhaustive-deps rule

## Package Information

- **NPM**: https://www.npmjs.com/package/eslint-plugin-react-hooks
- **GitHub Issues**: https://github.com/facebook/react/issues
- **License**: MIT
"""

        index_file = output_dir / "documentation-index.md"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)
        print(f"    -> Created file: documentation-index.md")
        files_copied += 1

        return files_copied > 0

    except Exception as e:
        print(f"    -> Error copying documentation: {e}")
        return False


def main():
    """Main function to extract eslint-plugin-react-hooks documentation."""
    print("=" * 70)
    print("ESLint Plugin React Hooks Documentation Scraper")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "eslint-plugin-react-hooks"

    print(f"Repository: facebook/react")
    print(f"Package: packages/eslint-plugin-react-hooks")
    print(f"Output directory: {output_dir}")
    print()

    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Clone repository
        print("Cloning repository...")
        repo_path = clone_react_repository(temp_dir)

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
    for text_file in sorted(text_files):
        file_size = text_file.stat().st_size
        print(f"    - {text_file.relative_to(output_dir)} ({file_size:,} bytes)")

    print()
    print("=" * 70)
    print("Extraction Complete")
    print("=" * 70)
    print(f"Output: {output_dir}")
    print()


if __name__ == "__main__":
    main()
