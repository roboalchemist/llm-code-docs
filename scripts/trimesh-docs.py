#!/usr/bin/env python3
"""
Trimesh Documentation Scraper

Scrapes the complete Trimesh documentation from trimesh.org, including:
- Installation and quick start guides
- Geometry format documentation
- Complete API reference
- Examples and tutorials

Output: docs/web-scraped/trimesh/
"""

import requests
import html2text
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse
from typing import Set, Optional
import time

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "trimesh"
BASE_URL = "https://trimesh.org/"

# Core pages to scrape
CORE_PAGES = [
    "",  # index
    "install.html",
    "quick_start.html",
    "formats.html",
    "contributing.html",
    "docker.html",
    "trimesh.html",
]

# Example pages
EXAMPLE_PAGES = [
    "examples.html",
    "texture.html",
    "curvature.html",
    "colors.html",
    "nearest.html",
    "ray.html",
    "section.html",
    "shortest.html",
]


def extract_main_content(html: str) -> Optional[str]:
    """Extract main article content from Sphinx documentation HTML."""
    # Try to find the main article content
    patterns = [
        r'<article[^>]*>(.*?)</article>',
        r'<main[^>]*>(.*?)</main>',
        r'<div class="main-content"[^>]*>(.*?)</div>',
        r'<div role="main"[^>]*>(.*?)</div>',
    ]

    for pattern in patterns:
        match = re.search(pattern, html, re.DOTALL)
        if match:
            return match.group(1)

    return None


def html_to_markdown(html_content: str) -> str:
    """Convert HTML to Markdown."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0
    h.unicode_snob = True

    markdown = h.handle(html_content)

    # Clean up excessive whitespace
    markdown = re.sub(r'\n\n\n+', '\n\n', markdown)

    # Remove navigation elements
    markdown = re.sub(r'\[\s*Previous\s*\]\([^)]*\)\s*\|\s*\[\s*Next\s*\]\([^)]*\)', '', markdown)
    markdown = re.sub(r'\[\s*Edit on GitHub\s*\]\([^)]*\)', '', markdown)

    return markdown.strip()


def fetch_page(url: str, page_name: str) -> Optional[str]:
    """Fetch and convert a single page to Markdown."""
    try:
        print(f"  Fetching {page_name}...")
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Extract main content
        content = extract_main_content(response.text)
        if not content:
            print(f"    Warning: No main content found")
            # Try to get the full body as fallback
            body_match = re.search(r'<body[^>]*>(.*?)</body>', response.text, re.DOTALL)
            if body_match:
                content = body_match.group(1)
            else:
                return None

        # Convert to markdown
        markdown = html_to_markdown(content)

        if not markdown or len(markdown) < 100:
            print(f"    Warning: Content too short ({len(markdown)} chars)")
            return None

        print(f"    Success ({len(markdown)} chars)")
        return markdown

    except requests.RequestException as e:
        print(f"    Error: {e}")
        return None
    except Exception as e:
        print(f"    Error: {e}")
        return None


def extract_api_docs() -> Optional[str]:
    """Extract full API reference documentation."""
    print("  Extracting API reference...")
    try:
        api_url = urljoin(BASE_URL, "trimesh.html")
        response = requests.get(api_url, timeout=15)
        response.raise_for_status()

        # Extract the API reference content
        content = extract_main_content(response.text)
        if not content:
            return None

        markdown = html_to_markdown(content)

        # Extract all API module links
        api_modules = re.findall(
            r'href="(trimesh\.[^"]+\.html)"',
            response.text
        )

        print(f"    Found {len(api_modules)} API modules to document")

        # Fetch additional API module pages
        for module in api_modules[:30]:  # Limit to first 30 to avoid too much data
            module_url = urljoin(BASE_URL, module)
            time.sleep(0.5)  # Be polite
            try:
                module_response = requests.get(module_url, timeout=15)
                module_response.raise_for_status()
                module_content = extract_main_content(module_response.text)
                if module_content:
                    module_markdown = html_to_markdown(module_content)
                    markdown += f"\n\n---\n\n## {module}\n\n{module_markdown}"
            except Exception as e:
                print(f"      Skipping {module}: {e}")
                continue

        return markdown

    except Exception as e:
        print(f"    Error: {e}")
        return None


def scrape_documentation():
    """Main scraper function."""
    print("Trimesh Documentation Scraper")
    print("=" * 60)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    files_created = 0
    total_size = 0

    # Scrape core pages
    print("\nScraping core documentation pages...")
    for page in CORE_PAGES:
        url = urljoin(BASE_URL, page)
        page_name = page if page else "index.html"
        markdown = fetch_page(url, page_name)

        if markdown:
            # Determine output filename
            if page == "":
                filename = "index.md"
            else:
                filename = page.replace(".html", ".md")

            output_file = OUTPUT_DIR / filename
            output_file.write_text(markdown, encoding='utf-8')
            files_created += 1
            total_size += len(markdown)
            print(f"    -> Saved to {filename}")

        time.sleep(1)  # Be polite to the server

    # Scrape example pages
    print("\nScraping example pages...")
    for page in EXAMPLE_PAGES:
        url = urljoin(BASE_URL, page)
        markdown = fetch_page(url, page)

        if markdown:
            filename = page.replace(".html", ".md")
            output_file = OUTPUT_DIR / filename
            output_file.write_text(markdown, encoding='utf-8')
            files_created += 1
            total_size += len(markdown)
            print(f"    -> Saved to {filename}")

        time.sleep(1)

    # Extract and save API reference
    print("\nExtracting API reference...")
    api_markdown = extract_api_docs()
    if api_markdown:
        output_file = OUTPUT_DIR / "api_reference.md"
        output_file.write_text(api_markdown, encoding='utf-8')
        files_created += 1
        total_size += len(api_markdown)
        print(f"    -> Saved to api_reference.md")

    # Create README
    readme_content = """# Trimesh Documentation

Trimesh is a lightweight Python library for loading and working with triangular meshes.
The goal of the library is to provide a simple interface to common tasks.

## Documentation Contents

- **index.md** - Main documentation index
- **install.md** - Installation guide
- **quick_start.md** - Quick start tutorial
- **formats.md** - Supported geometry formats
- **examples.md** - Example code
- **api_reference.md** - Complete API reference

## Key Features

- Load mesh files (STL, OBJ, PLY, DAE, glTF, etc.)
- Convert between 3D geometry formats
- Compute mesh properties (volume, surface area, center of mass)
- Check mesh validity
- Perform mesh operations (merge, split, slice)
- Ray-mesh intersections
- Voxelization
- Convex hulls
- Support for point clouds

## Usage

```python
import trimesh

# Load a mesh
mesh = trimesh.load('model.stl')

# Get basic properties
print(mesh.volume)
print(mesh.bounds)
print(mesh.center_mass)

# Apply transformations
mesh.apply_scale(2.0)
mesh.apply_translation([1, 2, 3])

# Save the mesh
mesh.export('output.ply')
```

For more information, see the official documentation at https://trimesh.org/
"""

    readme_file = OUTPUT_DIR / "README.md"
    readme_file.write_text(readme_content, encoding='utf-8')
    files_created += 1
    total_size += len(readme_content)

    print("\n" + "=" * 60)
    print(f"Scraping complete!")
    print(f"  Files created: {files_created}")
    print(f"  Total size: {total_size:,} bytes ({total_size / 1024 / 1024:.2f} MB)")
    print(f"  Output directory: {OUTPUT_DIR}")

    return files_created > 0


if __name__ == "__main__":
    success = scrape_documentation()
    exit(0 if success else 1)
