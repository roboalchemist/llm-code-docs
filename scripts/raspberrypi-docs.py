#!/usr/bin/env python3
"""
Scraper for Raspberry Pi documentation.
Clones the official GitHub repository and converts AsciiDoc to Markdown.
Output: docs/github-scraped/raspberrypi/
"""
import os
import subprocess
import shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import tempfile

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "raspberrypi"
REPO_URL = "https://github.com/raspberrypi/documentation.git"
TEMP_DIR = Path(tempfile.gettempdir()) / "rpi-docs-temp"

# Create output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def clone_repository():
    """Clone the Raspberry Pi documentation repository."""
    print("Cloning Raspberry Pi documentation repository...")

    # Clean up any existing temp directory
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)

    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    # Clone with limited depth to speed up process
    result = subprocess.run(
        ["git", "clone", "--depth", "1", REPO_URL, str(TEMP_DIR / "repo")],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error cloning repository: {result.stderr}")
        return False

    print("Repository cloned successfully.")
    return True

def convert_adoc_to_markdown(adoc_file, output_file):
    """Convert AsciiDoc file to Markdown using pandoc."""
    try:
        # Check if the file exists
        if not adoc_file.exists():
            return False

        # Create output directory if needed
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Use pandoc to convert AsciiDoc to Markdown
        result = subprocess.run(
            ["pandoc", "-f", "asciidoc", "-t", "markdown", "-o", str(output_file), str(adoc_file)],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0 and output_file.stat().st_size > 0:
            return True
        else:
            # If conversion fails or produces empty file, copy as-is with note
            with open(output_file, 'w') as f:
                f.write(f"# Source: {adoc_file.name}\n\n")
                f.write("*Note: This file could not be automatically converted from AsciiDoc.*\n\n")
                with open(adoc_file, 'r', errors='ignore') as src:
                    f.write(src.read())
            return True
    except Exception as e:
        print(f"Error converting {adoc_file}: {e}")
        return False

def extract_documentation():
    """Extract documentation from the cloned repository."""
    print("Extracting documentation files...")

    source_dir = TEMP_DIR / "repo" / "documentation" / "asciidoc"

    if not source_dir.exists():
        print(f"Source directory not found: {source_dir}")
        return False

    # Find all .adoc files
    adoc_files = list(source_dir.rglob("*.adoc"))
    print(f"Found {len(adoc_files)} AsciiDoc files to convert.")

    # Convert files in parallel
    converted_count = 0
    failed_count = 0

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {}

        for adoc_file in adoc_files:
            # Calculate relative path
            try:
                rel_path = adoc_file.relative_to(source_dir)
            except ValueError:
                continue

            # Determine output path (keep directory structure)
            output_file = OUTPUT_DIR / rel_path
            output_file = output_file.with_suffix('.md')

            # Submit conversion task
            future = executor.submit(convert_adoc_to_markdown, adoc_file, output_file)
            futures[future] = (adoc_file, output_file)

        # Process completed conversions
        for i, future in enumerate(as_completed(futures), 1):
            adoc_file, output_file = futures[future]
            try:
                if future.result():
                    converted_count += 1
                    if i % 50 == 0:
                        print(f"Converted {i}/{len(adoc_files)} files...")
                else:
                    failed_count += 1
            except Exception as e:
                print(f"Error processing {adoc_file}: {e}")
                failed_count += 1

    print(f"\nConversion complete: {converted_count} successful, {failed_count} failed.")
    return True

def copy_images():
    """Copy image files to output directory."""
    print("Copying image files...")

    source_images = TEMP_DIR / "repo" / "documentation" / "asciidoc"
    image_count = 0

    for image_file in source_images.rglob("*"):
        if image_file.is_file() and image_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.svg']:
            try:
                rel_path = image_file.relative_to(source_images)
                output_path = OUTPUT_DIR / rel_path
                output_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(image_file, output_path)
                image_count += 1
            except Exception as e:
                print(f"Error copying image {image_file}: {e}")

    print(f"Copied {image_count} image files.")

def create_index():
    """Create a simple index file."""
    index_file = OUTPUT_DIR / "README.md"

    # Count files
    md_files = list(OUTPUT_DIR.rglob("*.md"))
    img_files = list(OUTPUT_DIR.rglob("*.png")) + list(OUTPUT_DIR.rglob("*.jpg")) + \
                list(OUTPUT_DIR.rglob("*.jpeg")) + list(OUTPUT_DIR.rglob("*.gif")) + \
                list(OUTPUT_DIR.rglob("*.svg"))

    content = """# Raspberry Pi Documentation

Official Raspberry Pi documentation extracted from [github.com/raspberrypi/documentation](https://github.com/raspberrypi/documentation).

## Contents

This documentation covers:
- **Computers** - Raspberry Pi hardware models and specifications
- **Microcontrollers** - Raspberry Pi Pico and microcontroller guides
- **Accessories** - Cameras, displays, and HATs (Hardware Attached on Top)
- **Services** - Raspberry Pi services like Connect, ID, and Bookshelf

## Source

- **Repository**: https://github.com/raspberrypi/documentation
- **Format**: AsciiDoc to Markdown conversion
- **License**: Creative Commons Attribution-ShareAlike 4.0 International

## Statistics

- **Markdown Files**: {md_count}
- **Images**: {img_count}

## Key Topics

The documentation includes guides for:
- Getting started with Raspberry Pi
- Operating system setup and configuration
- GPIO programming and electronics
- Camera and display configuration
- Remote access and networking
- Linux kernel customization
- Hardware specifications and datasheets
""".format(md_count=len(md_files), img_count=len(img_files))

    with open(index_file, 'w') as f:
        f.write(content)

    print(f"Created index at {index_file}")

def cleanup():
    """Clean up temporary files."""
    print("Cleaning up temporary files...")
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)
    print("Cleanup complete.")

def main():
    """Main execution."""
    print("Starting Raspberry Pi documentation extraction...\n")

    # Clone repository
    if not clone_repository():
        print("Failed to clone repository.")
        cleanup()
        return False

    # Extract and convert documentation
    if not extract_documentation():
        print("Failed to extract documentation.")
        cleanup()
        return False

    # Copy images
    copy_images()

    # Create index
    create_index()

    # Cleanup
    cleanup()

    print(f"\nDocumentation successfully extracted to {OUTPUT_DIR}")
    return True

if __name__ == "__main__":
    main()
