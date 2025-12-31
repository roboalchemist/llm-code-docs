#!/usr/bin/env python3
"""
Download and process llms.txt from tldraw.dev
"""

import os
import requests
from pathlib import Path

# Configuration
BASE_URL = "https://tldraw.dev"
LLMS_TXT_URL = f"{BASE_URL}/llms.txt"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "llms-txt" / "tldraw"

def download_llms_txt():
    """Download and save the llms.txt file"""
    print(f"Downloading {LLMS_TXT_URL}...")

    response = requests.get(LLMS_TXT_URL, timeout=10)
    response.raise_for_status()

    content = response.text

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Save the full llms.txt content
    output_file = OUTPUT_DIR / "tldraw-full.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Saved to {output_file}")

    # Create a README with metadata
    readme_path = OUTPUT_DIR / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("""# tldraw SDK Documentation

Source: https://tldraw.dev/

## Overview

tldraw is an infinite canvas SDK for React. It provides a complete drawing and diagramming solution with built-in shapes, tools, and collaboration features.

## Key Features

- **Infinite Canvas**: Zoom and pan across a limitless canvas
- **Built-in Shapes**: Draw, geo shapes, arrows, text, notes, frames, and more
- **Custom Shapes**: Define your own shape types with custom rendering and behavior
- **Collaboration**: Real-time collaborative editing support
- **Persistence**: Save and load drawings with flexible storage options
- **UI Customization**: Fully customizable user interface components
- **Tools**: Rich set of drawing tools including select, draw, eraser, and more
- **TypeScript**: Full TypeScript support with comprehensive type definitions

## Documentation

The full documentation is available in the tldraw-full.md file, which includes:

- Getting started guides
- API reference
- Examples and tutorials
- Collaboration setup
- Custom shape creation
- Performance optimization

For the latest documentation, visit https://tldraw.dev/
""")

    print(f"✓ Created {readme_path}")
    print(f"\nSuccessfully downloaded tldraw documentation!")
    print(f"Total size: {len(content)} bytes")

if __name__ == "__main__":
    download_llms_txt()
