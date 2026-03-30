#!/usr/bin/env python3
"""
HAP-nodejs Documentation Extractor
Extracts documentation from the HAP-nodejs repository.
HAP-nodejs is the Node.js implementation of the HomeKit Accessory Protocol (HAP),
providing TypeScript/JavaScript APIs for building HomeKit accessories via Homebridge.
It includes comprehensive protocol documentation and service/characteristic definitions.
"""

import os
import sys
import shutil
import tempfile
import subprocess
from pathlib import Path

# Repository configuration
REPO_URL = "https://github.com/homebridge/HAP-nodejs.git"
REPO_BRANCH = "latest"

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "hap-nodejs"

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

def copy_docs(repo_path, output_path):
    """Copy documentation files from the repository."""
    try:
        print(f"Copying documentation files...")

        # Create output directory if it doesn't exist
        output_path.mkdir(parents=True, exist_ok=True)

        # Remove existing content
        if output_path.exists():
            print(f"  Removing existing output directory: {output_path}")
            shutil.rmtree(output_path)
            output_path.mkdir(parents=True, exist_ok=True)

        files_copied = 0

        # Copy docs folder
        docs_source = repo_path / "docs"
        if docs_source.exists():
            print(f"  Copying docs folder...")
            for item in docs_source.rglob("*"):
                if item.is_file():
                    rel_path = item.relative_to(docs_source)
                    target = output_path / "docs" / rel_path
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, target)
                    print(f"    -> Copied {rel_path}")
                    files_copied += 1

        # Copy README
        readme = repo_path / "README.md"
        if readme.exists():
            shutil.copy2(readme, output_path / "README.md")
            print(f"    -> Copied README.md")
            files_copied += 1

        # Copy CHANGELOG
        changelog = repo_path / "CHANGELOG.md"
        if changelog.exists():
            shutil.copy2(changelog, output_path / "CHANGELOG.md")
            print(f"    -> Copied CHANGELOG.md")
            files_copied += 1

        # Copy LICENSE
        license_file = repo_path / "LICENSE"
        if license_file.exists():
            shutil.copy2(license_file, output_path / "LICENSE.md")
            print(f"    -> Copied LICENSE")
            files_copied += 1

        # Copy package.json for reference
        package_json = repo_path / "package.json"
        if package_json.exists():
            shutil.copy2(package_json, output_path / "PACKAGE.md")
            # Convert to markdown for readability
            try:
                import json
                with open(package_json) as f:
                    pkg = json.load(f)
                with open(output_path / "PACKAGE.md", "w") as f:
                    f.write("# HAP-nodejs Package Information\n\n")
                    f.write(f"## Description\n{pkg.get('description', 'N/A')}\n\n")
                    f.write(f"## Version\n{pkg.get('version', 'N/A')}\n\n")
                    if 'keywords' in pkg:
                        f.write(f"## Keywords\n{', '.join(pkg['keywords'])}\n\n")
                    if 'repository' in pkg:
                        f.write(f"## Repository\n{pkg['repository']}\n\n")
            except:
                pass
            files_copied += 1

        return files_copied

    except Exception as e:
        print(f"  Error copying files: {e}")
        return 0

def generate_overview(output_path):
    """Generate an overview document."""
    try:
        overview = output_path / "OVERVIEW.md"
        with open(overview, "w") as f:
            f.write("""# HAP-nodejs Overview

## What is HAP-nodejs?

HAP-nodejs is the Node.js/TypeScript implementation of the HomeKit Accessory Protocol (HAP).
It allows you to build HomeKit-compatible accessories and integrate them with the Homebridge platform.

## Key Features

- **HomeKit Protocol Implementation**: Full HAP support for IP and Bluetooth LE
- **Service Definitions**: Predefined HomeKit services and characteristics
- **Pairing & Security**: SRP, Ed25519, and Curve25519 cryptography
- **TypeScript Support**: Full type definitions for IDE support
- **Accessory Categories**: Support for all HomeKit accessory types
- **Session Management**: Encrypted session handling

## Directory Structure

- `docs/` - Generated TypeDoc API documentation
- `README.md` - Getting started guide
- `CHANGELOG.md` - Version history
- `PACKAGE.md` - Package metadata

## Common Tasks

### Creating an Accessory
See the examples in the docs folder for creating HomeKit accessories.

### Pairing with Controllers
HAP-nodejs handles the HomeKit pairing process automatically.

### Working with Services and Characteristics
Use predefined service and characteristic types from the library.

## Related Documentation

- [HomeKit ADK](../homekit-adk/) - Apple's official HomeKit specification
- [Homebridge](https://github.com/homebridge/homebridge) - HomeKit bridge platform
- [HomeKit Protocol](../homekit-specification/) - HAP specification details
""")
        return True
    except Exception as e:
        print(f"  Error generating overview: {e}")
        return False

def verify_extraction(output_path):
    """Verify that documentation was extracted successfully."""
    try:
        print(f"\nVerifying extraction...")

        if not output_path.exists():
            print(f"  Error: Output directory does not exist")
            return False

        # Count files
        files = list(output_path.rglob("*"))
        total_size = sum(f.stat().st_size for f in files if f.is_file())

        print(f"  Total files: {len([f for f in files if f.is_file()])}")
        print(f"  Total size: {total_size:,} bytes ({total_size / 1024 / 1024:.2f} MB)")

        # List generated files
        print(f"\n  Generated documentation files:")
        for file in sorted(output_path.rglob("*.md")):
            size = file.stat().st_size
            rel_path = file.relative_to(output_path)
            print(f"    - {rel_path} ({size:,} bytes)")

        return True

    except Exception as e:
        print(f"  Error verifying extraction: {e}")
        return False

def main():
    print("=" * 70)
    print("HAP-nodejs Documentation Extractor")
    print("=" * 70)
    print()

    # Get output directory
    base_path = Path(__file__).parent.parent / "docs" / "github-scraped" / "hap-nodejs"

    print(f"Repository: {REPO_URL}")
    print(f"Branch: {REPO_BRANCH}")
    print(f"Output directory: {base_path}")
    print()

    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        print("Cloning repository...")
        repo_path = clone_repository(temp_dir, REPO_URL, REPO_BRANCH)

        if not repo_path:
            print("Failed to clone repository")
            sys.exit(1)

        print()

        # Copy documentation
        files_copied = copy_docs(repo_path, base_path)

        print()

        # Generate overview
        generate_overview(base_path)

        print()

        # Verify extraction
        verify_extraction(base_path)

    print()
    print("=" * 70)
    print("Extraction Complete")
    print("=" * 70)
    print(f"Output: {base_path}")

if __name__ == "__main__":
    main()
