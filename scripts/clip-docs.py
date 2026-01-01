#!/usr/bin/env python3
"""
CLIP Documentation Scraper
Extracts documentation from OpenAI's CLIP repository (https://github.com/openai/CLIP)
CLIP is a vision-language model that aligns image and text representations.
"""

import os
import sys
import requests
from pathlib import Path
import time
import json
import re
from urllib.parse import urljoin

# GitHub raw content URLs for CLIP repository
REPO_OWNER = "openai"
REPO_NAME = "CLIP"
REPO_BRANCH = "main"
BASE_URL = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{REPO_BRANCH}"
API_BASE = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "clip"

REQUEST_DELAY = 0.3  # seconds between requests
MAX_RETRIES = 3
TIMEOUT = 20


def sanitize_filename(path):
    """Convert URL path to safe filename."""
    # Remove leading/trailing slashes and .git
    path = path.strip("/").replace(".git", "")

    # If empty, use 'index'
    if not path:
        return "index.md"

    # Replace slashes with hyphens, keep the filename part
    parts = path.rsplit("/", 1)
    if len(parts) == 2:
        safe = parts[1]
    else:
        safe = parts[0]

    # Remove common extensions and add .md
    safe = re.sub(r'\.(md|txt|rst)$', '', safe)

    # Ensure .md extension
    if not safe.endswith('.md'):
        safe = safe + '.md'

    return safe


def fetch_url(url, max_retries=MAX_RETRIES):
    """Fetch URL with retries and error handling."""
    for attempt in range(max_retries):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=TIMEOUT)

            if response.status_code == 200:
                time.sleep(REQUEST_DELAY)
                return response.text
            elif response.status_code == 404:
                return None
            elif response.status_code == 429:  # Rate limit
                wait_time = (2 ** attempt) * 5
                print(f"    Rate limited, waiting {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"    HTTP {response.status_code} for {url}")
                return None
        except requests.RequestException as e:
            print(f"    Error fetching {url}: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)

    return None


def add_source_header(content, url):
    """Add source header to markdown content."""
    source_header = f"# Source: {url}\n\n"
    return source_header + content


def download_file(file_path, url):
    """Download a file from GitHub and save it."""
    print(f"  Downloading {file_path}...")
    content = fetch_url(url)

    if content is None:
        print(f"    Failed to download {file_path}")
        return False

    # Add source header
    content = add_source_header(content, url)

    # Save to file
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True


def get_notebook_content(url):
    """Extract markdown content from Jupyter notebook."""
    print(f"  Processing notebook...")

    content = fetch_url(url)
    if content is None:
        return None

    try:
        notebook = json.loads(content)
    except json.JSONDecodeError:
        print(f"    Failed to parse notebook JSON")
        return None

    markdown_content = []

    # Extract markdown from notebook cells
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            source = cell.get('source', [])
            if isinstance(source, list):
                markdown_content.append(''.join(source))
            else:
                markdown_content.append(source)
        elif cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            if isinstance(source, list):
                code = ''.join(source)
            else:
                code = source

            if code.strip():
                markdown_content.append(f"\n```python\n{code}\n```\n")

    return '\n\n'.join(markdown_content) if markdown_content else None


def scrape_clip():
    """Scrape CLIP documentation from GitHub."""
    print(f"Scraping CLIP documentation from {API_BASE}...")

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Download README.md
    print("\n1. Downloading README.md...")
    readme_url = f"{BASE_URL}/README.md"
    readme_file = OUTPUT_DIR / "01-readme.md"
    download_file(readme_file, readme_url)

    # 2. Download model-card.md
    print("\n2. Downloading model-card.md...")
    modelcard_url = f"{BASE_URL}/model-card.md"
    modelcard_file = OUTPUT_DIR / "02-model-card.md"
    download_file(modelcard_file, modelcard_url)

    # 3. Download notebooks
    notebooks = [
        "notebooks/Interacting_with_CLIP.ipynb",
        "notebooks/Prompt_Engineering_for_ImageNet.ipynb"
    ]

    print("\n3. Processing Jupyter notebooks...")
    for i, notebook_path in enumerate(notebooks, start=3):
        notebook_url = f"{BASE_URL}/{notebook_path}"
        notebook_name = Path(notebook_path).stem
        output_file = OUTPUT_DIR / f"0{i}-notebook-{notebook_name}.md"

        print(f"  Processing {notebook_path}...")
        notebook_content = get_notebook_content(notebook_url)

        if notebook_content:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            notebook_content = add_source_header(notebook_content, notebook_url)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(notebook_content)
            print(f"    Saved to {output_file}")
        else:
            print(f"    Failed to extract content from {notebook_path}")

    # 4. Create overview document
    print("\n4. Creating overview document...")
    overview_content = """# Source: https://github.com/openai/CLIP

# CLIP (Contrastive Language-Image Pre-Training) Overview

CLIP is a neural network trained on diverse (image, text) pairs to learn visual concepts from natural language supervision. It can be applied to any visual classification benchmark by simply providing the names of the visual categories to be recognized, similar to the "zero-shot" capabilities of GPT-2 and GPT-3.

## Key Features

- **Vision-Language Alignment**: Aligns image and text representations in a shared embedding space
- **Zero-Shot Learning**: Can classify images without task-specific training data
- **Flexible Architecture**: Supports multiple vision and text encoder architectures
- **Model Variants**: Available in multiple sizes (RN50, RN50x64, ViT-B/32, ViT-L/14)
- **Efficient Inference**: Fast and efficient for inference on both CPU and GPU

## Architecture

CLIP uses a dual-encoder architecture:

1. **Vision Encoder**: Processes images into feature representations
   - Options: ResNet or Vision Transformer (ViT)
   - Outputs: 512-dimensional embeddings

2. **Text Encoder**: Processes text descriptions
   - 12-layer Transformer
   - Tokenizer-based input processing

3. **Alignment Mechanism**:
   - Learned temperature parameter for scaling similarities
   - Batch-global negative sampling for contrastive training

## Model Variants

| Model | Parameters | Vision Encoder | Text Encoder |
|-------|-----------|-----------------|--------------|
| RN50 | ~102M | ResNet-50 | Transformer |
| RN50x64 | ~430M | ResNet-50x64 | Transformer |
| ViT-B/32 | ~149M | Vision Transformer | Transformer |
| ViT-L/14 | ~428M | Vision Transformer Large | Transformer |

## Usage Patterns

### Image Classification
CLIP can classify images into arbitrary categories by computing similarity between image embeddings and text embeddings of category names.

### Image-Text Similarity
Measure similarity between images and natural language descriptions for retrieval and ranking tasks.

### Zero-Shot Transfer
Classify images into novel categories without any task-specific training data.

## Training Details

- **Dataset**: Trained on 400 million diverse (image, text) pairs from the internet
- **Method**: Contrastive pre-training with symmetric cross-entropy loss
- **Architecture**: Vision and text encoders trained jointly
- **Efficiency**: Demonstrates strong performance with modest computational requirements

## Repository Contents

- `clip/` - Core CLIP implementation
- `notebooks/` - Interactive examples and demonstrations
- `data/` - Data loading utilities
- `requirements.txt` - Python dependencies
- `setup.py` - Package installation configuration

## Common Use Cases

1. **Content Moderation**: Classify user-generated images
2. **Image Search**: Search image databases by natural language queries
3. **Accessibility**: Generate image descriptions for accessibility
4. **Semantic Analysis**: Analyze visual content semantically
5. **Transfer Learning**: Fine-tune for downstream vision tasks

## Model Scaling

CLIP demonstrates strong scaling properties:
- Larger models consistently perform better
- Zero-shot transfer improves with model scale
- Efficient scaling on both vision and text components

## Performance Characteristics

- **Robustness**: Strong performance on distribution shifts and out-of-distribution data
- **Generalization**: Excellent zero-shot transfer capabilities
- **Efficiency**: Fast inference compared to task-specific models
- **Compositionality**: Can handle complex composed descriptions

## Related Resources

- OpenAI Blog: https://openai.com/blog/clip/
- GitHub Repository: https://github.com/openai/CLIP
- Paper: Learning Transferable Models for Semantic Segmentation
- Hugging Face Integration: https://huggingface.co/docs/transformers/model_doc/clip

## Implementation Notes

CLIP implementations are available in:
- PyTorch (Official)
- TensorFlow/JAX variants
- ONNX for cross-platform compatibility
- Hugging Face Transformers integration

For detailed implementation examples, see the notebooks directory in the repository.
"""

    overview_file = OUTPUT_DIR / "00-overview.md"
    with open(overview_file, 'w', encoding='utf-8') as f:
        f.write(overview_content)
    print(f"  Created overview at {overview_file}")

    # Summary
    files_created = list(OUTPUT_DIR.glob("*.md"))
    print(f"\nDocumentation saved to: {OUTPUT_DIR}")
    print(f"Total files created: {len(files_created)}")

    return True


def main():
    """Main function."""
    print("=" * 70)
    print("CLIP Documentation Scraper")
    print("=" * 70)

    try:
        success = scrape_clip()

        if success:
            print("\n" + "=" * 70)
            print("CLIP documentation extraction completed successfully!")
            print("=" * 70)
            return 0
        else:
            print("\n" + "=" * 70)
            print("CLIP documentation extraction failed!")
            print("=" * 70)
            return 1
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
