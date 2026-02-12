#!/usr/bin/env python3
"""
Scraper for Marker OCR documentation.
Extracts README and relevant markdown files from the Marker GitHub repository.
Output: docs/web-scraped/marker/
"""

import os
import shutil
import subprocess
from pathlib import Path
from urllib.parse import urljoin

# Configuration
REPO_URL = "https://github.com/VikParuchuri/marker"
REPO_DIR = "/tmp/marker-docs-clone"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "marker"

def clone_repo():
    """Clone the repository."""
    if Path(REPO_DIR).exists():
        shutil.rmtree(REPO_DIR)

    print(f"Cloning {REPO_URL}...")
    subprocess.run([
        "git", "clone", "--depth", "1", REPO_URL, REPO_DIR
    ], check=True, capture_output=True)
    print(f"Repository cloned to {REPO_DIR}")

def extract_documentation():
    """Extract markdown documentation files."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    repo_path = Path(REPO_DIR)
    files_to_copy = [
        "README.md",
        "CLA.md",
        "examples/README.md",
    ]

    copied_files = []

    for file_path in files_to_copy:
        source = repo_path / file_path
        if source.exists():
            # Create target directory based on source structure
            if source.parent != repo_path:
                # File is in a subdirectory
                target_dir = OUTPUT_DIR / source.parent.name
            else:
                # File is in root
                target_dir = OUTPUT_DIR

            target_dir.mkdir(parents=True, exist_ok=True)
            target = target_dir / source.name

            # Add source header to the file
            with open(source, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Add source attribution at the top
            source_header = f"# Source: {REPO_URL}/blob/master/{file_path}\n\n"

            with open(target, 'w', encoding='utf-8') as f:
                f.write(source_header)
                f.write(content)

            copied_files.append(str(target.relative_to(OUTPUT_DIR)))
            print(f"Copied: {file_path}")

    # Create an index document
    index_content = """# Marker OCR Documentation

Marker is a tool that converts PDFs, images, and other documents to markdown, JSON, or HTML using deep learning models.

## Quick Links

- **Main Documentation**: See [README.md](README.md) for comprehensive usage guide
- **Examples**: See [examples/README.md](examples/README.md) for usage examples
- **Official Repository**: https://github.com/VikParuchuri/marker
- **Hosted API**: https://www.datalab.to/

## Key Features

- Converts PDF, image, PPTX, DOCX, XLSX, HTML, EPUB files in all languages
- Formats tables, forms, equations, inline math, links, references, and code blocks
- Extracts and saves images
- Removes headers/footers/other artifacts
- Extensible with custom formatting and logic
- Structured extraction with JSON schema (beta)
- Optional LLM-powered accuracy boost
- Works on GPU, CPU, or MPS

## Installation

```bash
pip install marker-pdf
```

For full feature support (PPTX, DOCX, XLSX, etc.):

```bash
pip install marker-pdf[full]
```

## Basic Usage

### Single File Conversion

```bash
marker_single /path/to/file.pdf
```

### Batch Conversion

```bash
marker /path/to/input/folder
```

### With LLM Enhancement

```bash
marker_single file.pdf --use_llm
```

## Output Formats

- **Markdown**: Default output with formatted tables, equations, and code blocks
- **JSON**: Tree-structured output with block types and metadata
- **HTML**: HTML representation with proper formatting
- **Chunks**: Flattened JSON format suitable for RAG applications

## Configuration

Key environment variables and flags:

- `TORCH_DEVICE`: Force a specific torch device (e.g., `cuda`, `cpu`, `mps`)
- `--force_ocr`: Force OCR processing on entire document
- `--use_llm`: Use LLM for improved accuracy
- `--output_format`: Specify output format (markdown, json, html, chunks)
- `--workers`: Number of parallel workers for batch processing

## LLM Services

Marker supports multiple LLM services for enhanced accuracy:

- **Gemini** (default): Google's Gemini API
- **Google Vertex**: Vertex AI for reliability
- **Ollama**: Local models
- **Claude**: Anthropic's Claude API
- **OpenAI**: OpenAI API
- **Azure OpenAI**: Azure's OpenAI service

## API Server

Run a simple FastAPI server:

```bash
pip install uvicorn fastapi python-multipart
marker_server --port 8001
```

Access at `http://localhost:8001/docs` for interactive API documentation.

## Performance

Marker benchmarks favorably against commercial tools like Llamaparse and Mathpix:

- **Speed**: ~2.8 seconds per page (faster than competitors)
- **Accuracy**: 95.67% heuristic score, 4.24/5 LLM score
- **Throughput**: 122 pages/second on H100 GPU

## For More Information

See the complete [README.md](README.md) for:
- Detailed configuration options
- Advanced usage examples
- Custom processor development
- Integration guides
- Troubleshooting tips
- Benchmark methodology and results
"""

    # Ensure OUTPUT_DIR exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    index_path = OUTPUT_DIR / "INDEX.md"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"Created INDEX.md")

    return copied_files

def cleanup():
    """Clean up temporary directory."""
    if Path(REPO_DIR).exists():
        shutil.rmtree(REPO_DIR)
    print(f"Cleaned up temporary directory")

def main():
    """Main function."""
    print("Extracting Marker OCR documentation...")

    clone_repo()
    files = extract_documentation()
    cleanup()

    print(f"\nDocumentation extracted to: {OUTPUT_DIR}")
    print(f"Files created: {len(files) + 1}")
    for file in sorted(files):
        print(f"  - {file}")
    print(f"  - marker/INDEX.md")

if __name__ == "__main__":
    main()
