#!/usr/bin/env python3
"""
HomeKit ADK Documentation Extractor
Extracts documentation from Apple's HomeKit Accessory Development Kit.
The HomeKit ADK contains Apple's official HomeKit Accessory Protocol (HAP) specification,
implementation guide, reference implementation in C, and comprehensive documentation.
"""

import os
import sys
import shutil
import tempfile
import subprocess
from pathlib import Path

# Repository configuration
REPO_URL = "https://github.com/apple/HomeKitADK.git"
REPO_BRANCH = "master"

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "homekit-adk"

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

        # Copy Documentation folder
        docs_source = repo_path / "Documentation"
        if docs_source.exists():
            print(f"  Copying Documentation folder...")
            for item in docs_source.rglob("*"):
                if item.is_file():
                    rel_path = item.relative_to(docs_source)
                    target = output_path / rel_path
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, target)
                    print(f"    -> Copied {rel_path}")
                    files_copied += 1

        # Copy HAP header files (for reference)
        hap_source = repo_path / "HAP"
        if hap_source.exists():
            print(f"  Copying HAP header files for reference...")
            hap_target = output_path / "HAP-Headers"
            hap_target.mkdir(parents=True, exist_ok=True)

            # Copy only .h files (headers)
            for item in hap_source.glob("*.h"):
                shutil.copy2(item, hap_target / item.name)
                print(f"    -> Copied {item.name}")
                files_copied += 1

        # Copy README
        readme = repo_path / "README.md"
        if readme.exists():
            shutil.copy2(readme, output_path / "README.md")
            print(f"    -> Copied README.md")
            files_copied += 1

        # Copy CODE_OF_CONDUCT
        coc = repo_path / "CODE_OF_CONDUCT.md"
        if coc.exists():
            shutil.copy2(coc, output_path / "CODE_OF_CONDUCT.md")
            print(f"    -> Copied CODE_OF_CONDUCT.md")
            files_copied += 1

        # Copy CONTRIBUTING
        contrib = repo_path / "CONTRIBUTING.md"
        if contrib.exists():
            shutil.copy2(contrib, output_path / "CONTRIBUTING.md")
            print(f"    -> Copied CONTRIBUTING.md")
            files_copied += 1

        # Copy LICENSE
        license_file = repo_path / "LICENSE.md"
        if license_file.exists():
            shutil.copy2(license_file, output_path / "LICENSE.md")
            print(f"    -> Copied LICENSE.md")
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
            f.write("""# HomeKit Accessory Development Kit (ADK)

## Overview

The HomeKit Accessory Development Kit (HomeKit ADK) is Apple's official kit for developing HomeKit-compatible accessories.
It contains the complete HomeKit Accessory Protocol (HAP) specification, implementation guide, reference implementation in C,
and comprehensive documentation for building HomeKit accessories.

## What's Included

### Documentation
- **HAP Specification**: Complete protocol definition for HomeKit communication
- **Getting Started Guide**: How to build your first HomeKit accessory
- **Crypto Documentation**: Security protocols (SRP, Ed25519, Curve25519)
- **Visual Debug Guide**: Debugging tips for macOS development

### Reference Implementation
- **HAP Library**: Full C implementation of the HomeKit Accessory Protocol
- **Services & Characteristics**: Predefined HomeKit service and characteristic definitions
- **Examples**: Reference implementations for various accessory types
- **Test Suite**: Validation tools for accessory implementations

### Key Features

- **IP and BLE Transport**: Support for both HTTP/IP and Bluetooth LE
- **Security**: TLS 1.2, SRP authentication, frame encryption
- **Pairing**: HomeKit secure pairing and session establishment
- **Accessories**: Support for all HomeKit accessory categories
- **Services**: Lighting, locks, thermostats, sensors, and more
- **Characteristics**: Standardized device attributes and states

## Directory Structure

- `Documentation/` - Official HAP specification and guides
  - `index.rst` - Main documentation index
  - `getting_started.md` - Getting started guide
  - `crypto.md` - Cryptography details
  - `darwin_visual_debug.md` - macOS debugging guide
  - `coding_convention.md` - Development conventions
- `HAP/` - Header files for the HAP implementation
- `HAP-Headers/` - Reference HAP interface definitions
- `Applications/` - Example applications
- `README.md` - Repository overview
- `LICENSE.md` - Apache 2.0 license

## Common Tasks

### Understanding HAP
Start with the Documentation folder to understand the protocol.

### Implementing an Accessory
Use the reference implementation and examples to guide your development.

### Working with Services & Characteristics
Refer to the service definitions for all available HomeKit types.

### Security & Pairing
Review crypto.md for security protocol details.

## Related Resources

- [HAP-nodejs](../hap-nodejs/) - Node.js implementation of HAP
- [Homebridge](https://github.com/homebridge/homebridge) - HomeKit bridge platform
- [HomeKit Official](https://www.apple.com/homekit/) - Apple's HomeKit ecosystem

## License

Apache License 2.0 - See LICENSE.md
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

        for file in sorted(output_path.rglob("*.rst")):
            size = file.stat().st_size
            rel_path = file.relative_to(output_path)
            print(f"    - {rel_path} ({size:,} bytes)")

        return True

    except Exception as e:
        print(f"  Error verifying extraction: {e}")
        return False

def main():
    print("=" * 70)
    print("HomeKit ADK Documentation Extractor")
    print("=" * 70)
    print()

    # Get output directory
    base_path = Path(__file__).parent.parent / "docs" / "github-scraped" / "homekit-adk"

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
