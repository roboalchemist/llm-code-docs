#!/usr/bin/env python3
"""
Scraper for lsprotocol documentation.
Extracts from GitHub repo and PyPI.
Output: docs/web-scraped/lsprotocol/
"""
import os
import re
import json
from pathlib import Path
from urllib.request import urlopen
from datetime import datetime

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "lsprotocol"

def fetch_text(url, timeout=10):
    """Fetch text from URL."""
    try:
        with urlopen(url, timeout=timeout) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def create_markdown_doc(title, content, source_url):
    """Create markdown document with source header."""
    doc = f"# Source: {source_url}\n\n"
    doc += f"# {title}\n\n"
    doc += content
    return doc

def scrape_readme():
    """Scrape README.md from GitHub."""
    url = "https://raw.githubusercontent.com/microsoft/lsprotocol/main/packages/python/README.md"
    content = fetch_text(url)
    if not content:
        return None
    
    return create_markdown_doc(
        "Language Server Protocol Types Implementation for Python",
        content,
        url
    )

def scrape_pypi():
    """Scrape PyPI package information."""
    url = "https://pypi.org/pypi/lsprotocol/json"
    try:
        with urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        info = data['info']
        content = f"""## Package Information

**Name:** {info['name']}
**Version:** {info['version']}
**Author:** {info['author']}
**License:** {info['license']}
**Home Page:** {info['home_page']}
**Project URL:** {info['project_url']}

## Summary

{info['summary']}

## Description

{info['description']}

## Requires Python

{info['requires_python']}

## Classifiers

"""
        for classifier in info.get('classifiers', []):
            content += f"- {classifier}\n"
        
        return create_markdown_doc(
            "lsprotocol - PyPI Package Information",
            content,
            url
        )
    except Exception as e:
        print(f"Error fetching PyPI info: {e}")
        return None

def scrape_types_documentation():
    """Scrape and document the types module."""
    url = "https://raw.githubusercontent.com/microsoft/lsprotocol/main/packages/python/lsprotocol/types.py"
    content = fetch_text(url)
    if not content:
        return None
    
    # Extract enums and classes
    lines = content.split('\n')
    doc = "# LSP Types Reference\n\n"
    doc += "This document provides a reference of the main types and enums available in the lsprotocol package.\n\n"
    
    # Extract top-level classes and enums
    doc += "## Enums and Classes\n\n"
    
    in_class = False
    class_name = None
    class_doc = []
    
    for i, line in enumerate(lines[20:300]):  # Sample first part of file
        if line.startswith('class ') or line.startswith('@enum.unique'):
            if class_name:
                doc += f"### {class_name}\n\n"
                doc += '\n'.join(class_doc) + "\n\n"
            
            if '@enum.unique' in line:
                # Next line is the class definition
                pass
            elif line.startswith('class '):
                class_name = line.split('class ')[1].split('(')[0].split(':')[0]
                class_doc = []
                in_class = True
        elif in_class and line.strip() and not line.startswith(' '):
            in_class = False
        elif in_class and line.strip():
            class_doc.append(line.strip())
    
    doc += "\n## Module Information\n\n"
    doc += f"- **LSP Version:** 3.17.0\n"
    doc += f"- **Generated File:** Yes (do not edit directly)\n"
    doc += f"- **Generation Command:** `python -m nox --session build_lsp`\n"
    
    return create_markdown_doc(
        "LSP Types Reference",
        doc,
        url
    )

def scrape_converters():
    """Scrape converters module documentation."""
    url = "https://raw.githubusercontent.com/microsoft/lsprotocol/main/packages/python/lsprotocol/converters.py"
    content = fetch_text(url)
    if not content:
        return None
    
    # Extract docstrings and functions
    lines = content.split('\n')
    doc = "# Type Converters\n\n"
    doc += "The converters module provides utilities for converting between lsprotocol types and JSON-serializable objects.\n\n"
    
    # Extract class/function definitions and their docstrings
    for i, line in enumerate(lines[:100]):
        if line.strip().startswith('def ') or line.strip().startswith('class '):
            doc += f"```python\n{line}\n```\n\n"
    
    doc += "## Converter Usage\n\n"
    doc += """The `get_converter()` function returns a converter instance that can be used to:
- **Unstructure:** Convert lsprotocol types to JSON-serializable dicts
- **Structure:** Convert dicts back to lsprotocol types

### Example:
```python
from lsprotocol import converters, types

position = types.Position(line=10, character=3)
converter = converters.get_converter()
json_data = converter.unstructure(position, unstructure_as=types.Position)
```
"""
    
    return create_markdown_doc(
        "Type Converters Module",
        doc,
        url
    )

def scrape_installation_guide():
    """Create installation and usage guide."""
    doc = """# Installation and Usage Guide

## Installation

Install lsprotocol via pip:

```bash
python -m pip install lsprotocol
```

## Quick Start

### Import and Use Types

```python
from lsprotocol import types

# Create a Position
position = types.Position(line=10, character=3)

# Create a Range
range_obj = types.Range(
    start=position,
    end=types.Position(line=10, character=10)
)
```

### Using Type Converters

```python
import json
from lsprotocol import converters, types

# Create a type instance
position = types.Position(line=10, character=3)

# Get a converter
converter = converters.get_converter()

# Convert to JSON-serializable dict
json_dict = converter.unstructure(position, unstructure_as=types.Position)
print(json.dumps(json_dict))  # {"line": 10, "character": 3}

# Convert back from dict to type
position_obj = converter.structure(json_dict, types.Position)
```

## Supported LSP Version

- **LSP Version:** 3.17.0

## Use Cases

lsprotocol is designed for developers building:
- Language Server Protocol (LSP) servers
- LSP clients and editor plugins
- Tools that extend LSP functionality
- Applications that need LSP type definitions

## Project Structure

The project consists of:
- **types.py** - Auto-generated LSP type definitions
- **converters.py** - Type conversion utilities
- **validators.py** - Validation utilities
- **_hooks.py** - Internal hooks for type generation

## Generation Process

The types are generated from the official LSP specification:

```bash
# To regenerate types (requires nox)
python -m pip install nox
python -m nox --session build_lsp
```

## Links

- **GitHub Repository:** https://github.com/microsoft/lsprotocol
- **PyPI Package:** https://pypi.org/project/lsprotocol/
- **Language Server Protocol:** https://microsoft.github.io/language-server-protocol/
"""
    
    return create_markdown_doc(
        "Installation and Usage Guide",
        doc,
        "https://github.com/microsoft/lsprotocol"
    )

def main():
    """Main scraper function."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print(f"Scraping lsprotocol documentation to {OUTPUT_DIR}")
    
    docs = [
        ("00_README.md", scrape_readme()),
        ("01_Installation_Guide.md", scrape_installation_guide()),
        ("02_PyPI_Package_Info.md", scrape_pypi()),
        ("03_Types_Reference.md", scrape_types_documentation()),
        ("04_Converters.md", scrape_converters()),
    ]
    
    saved_count = 0
    for filename, content in docs:
        if content:
            filepath = OUTPUT_DIR / filename
            filepath.write_text(content, encoding='utf-8')
            saved_count += 1
            print(f"  Saved: {filename}")
        else:
            print(f"  Failed to scrape: {filename}")
    
    print(f"\nTotal files saved: {saved_count}")
    
    # Print summary
    if OUTPUT_DIR.exists():
        files = list(OUTPUT_DIR.glob("*.md"))
        total_size = sum(f.stat().st_size for f in files)
        print(f"Total size: {total_size / 1024:.1f} KB")

if __name__ == "__main__":
    main()
