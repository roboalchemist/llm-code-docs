#!/usr/bin/env python3
"""
Jina Integrations Documentation Scraper
Scrapes documentation for Jina integrations with LangChain and other frameworks.
Includes JinaEmbeddings, JinaRerank, and other integration documentation.
"""

import os
import sys
import json
from pathlib import Path
from urllib.parse import urljoin
import requests

# Configuration
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "jina-integrations"
INTEGRATION_URLS = {
    "langchain-jina-embeddings": {
        "url": "https://python.langchain.com/docs/integrations/text_embedding/jina/",
        "description": "LangChain Jina Embeddings Integration"
    },
    "langchain-jina-rerank": {
        "url": "https://python.langchain.com/docs/integrations/document_compressors/jina/",
        "description": "LangChain Jina Reranker Integration"
    },
    "langchain-jina-overview": {
        "url": "https://python.langchain.com/docs/integrations/providers/jina/",
        "description": "LangChain Jina AI Provider Overview"
    },
    "langchain-js-jina": {
        "url": "https://js.langchain.com/v0.2/docs/integrations/text_embedding/jina/",
        "description": "LangChain JS Jina Embeddings Integration"
    }
}

def fetch_url(url, timeout=10):
    """Fetch URL content with error handling."""
    try:
        print(f"  Fetching: {url}")
        response = requests.get(url, timeout=timeout, allow_redirects=True)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"    Error fetching {url}: {e}")
        return None


def extract_text_from_html(html_content, url):
    """Extract text from HTML content and format as markdown."""
    try:
        import re
        from html.parser import HTMLParser

        class TextExtractor(HTMLParser):
            def __init__(self):
                super().__init__()
                self.text = []
                self.in_script = False
                self.in_style = False

            def handle_starttag(self, tag, attrs):
                if tag in ['script', 'style']:
                    self.in_script = True
                elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    self.text.append('\n\n' + '#' * int(tag[1]) + ' ')
                elif tag == 'p':
                    self.text.append('\n')
                elif tag in ['li']:
                    self.text.append('\n- ')
                elif tag == 'br':
                    self.text.append('\n')
                elif tag == 'code':
                    self.text.append('`')
                elif tag == 'pre':
                    self.text.append('\n```\n')

            def handle_endtag(self, tag):
                if tag in ['script', 'style']:
                    self.in_script = False
                elif tag in ['p']:
                    self.text.append('\n')
                elif tag == 'code':
                    self.text.append('`')
                elif tag == 'pre':
                    self.text.append('\n```\n')

            def handle_data(self, data):
                if not self.in_script and not self.in_style:
                    cleaned = data.strip()
                    if cleaned:
                        self.text.append(cleaned + ' ')

        extractor = TextExtractor()
        extractor.feed(html_content)
        markdown_text = ''.join(extractor.text)

        # Clean up multiple newlines
        markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)

        # Add source header
        header = f"""# Source: {url}

"""
        return header + markdown_text
    except Exception as e:
        print(f"    Error converting HTML to text: {e}")
        return None


def save_documentation(name, content):
    """Save documentation to file."""
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Create filename from name
        filename = f"{name}.md"
        filepath = OUTPUT_DIR / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        file_size = filepath.stat().st_size
        print(f"    -> Saved: {filename} ({file_size:,} bytes)")
        return True
    except Exception as e:
        print(f"    Error saving documentation: {e}")
        return False


def scrape_langchain_integration(name, url, description):
    """Scrape a LangChain integration page."""
    print(f"\nScraping: {description}")
    print(f"  URL: {url}")

    html_content = fetch_url(url)
    if not html_content:
        return False

    markdown_content = extract_text_from_html(html_content, url)
    if not markdown_content:
        return False

    if save_documentation(name, markdown_content):
        return True

    return False


def create_integration_index():
    """Create an index file for integrations."""
    try:
        index_content = """# Jina AI Integrations

This directory contains documentation for Jina AI integrations with popular frameworks and libraries.

## Integration Categories

### LangChain Integration
Jina AI provides embeddings and reranking capabilities through LangChain:

- **JinaEmbeddings** - Text embedding model integration for Python and JavaScript
  - Supports multilingual text embedding with Jina's embedding models
  - Available in LangChain Python and LangChain JS

- **JinaReranker** - Document reranking for improving search results
  - Integrates with LangChain's document compression framework
  - Improves relevance of RAG (Retrieval Augmented Generation) results

## Supported Models

- `jina-embeddings-v3` - 570M parameter multilingual text embedding model
- `jina-embeddings-v4` - 3.8B parameter multimodal embedding model
- `jina-clip-v2` - Multimodal embedding for text-image retrieval
- `jina-reranker-v3` - Multilingual document reranking model
- `jina-reranker-m0` - Multimodal reranking supporting text and images

## Installation

### LangChain Python
```bash
pip install langchain-community langchain jina
```

### LangChain JavaScript
```bash
npm install @langchain/community @langchain/core
```

## Usage Examples

### Python - JinaEmbeddings
```python
from langchain_community.embeddings.jina import JinaEmbeddings

embeddings = JinaEmbeddings(
    model="jina-embeddings-v3",
    api_key="your-jina-api-key"
)

# Embed text
text = "Hello, world!"
embedding = embeddings.embed_query(text)
```

### Python - JinaReranker
```python
from langchain_community.document_compressors.jina_rerank import JinaRerank

reranker = JinaRerank(
    model="jina-reranker-v3",
    api_key="your-jina-api-key"
)

# Rerank documents
reranked_docs = reranker.compress_documents(docs, query)
```

## Documentation Links

- [Jina Official Documentation](https://docs.jina.ai/)
- [LangChain Jina Integration Docs](https://python.langchain.com/docs/integrations/providers/jina/)
- [LangChain Community GitHub](https://github.com/langchain-ai/langchain)

## API Key Setup

Get your Jina API key for free at: https://jina.ai/?sui=apikey

Set the environment variable:
```bash
export JINA_API_KEY="your-api-key"
```

## Features

- **Multilingual Support**: Embedding models support 100+ languages
- **Multimodal Capabilities**: Some models support both text and images
- **High Performance**: Optimized for production use with low latency
- **Flexible Dimensions**: Truncate embeddings to desired dimensions
- **Task-Specific Optimization**: Different embedding modes for different tasks

## Support

For issues and questions:
- GitHub: https://github.com/jina-ai/jina
- Documentation: https://docs.jina.ai/
- Community Forum: https://github.com/jina-ai/jina/discussions
"""

        filepath = OUTPUT_DIR / "00-README.md"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(index_content)

        print(f"  Created index: 00-README.md")
        return True
    except Exception as e:
        print(f"  Error creating index: {e}")
        return False


def main():
    """Main function to scrape Jina integrations documentation."""
    print("=" * 70)
    print("Jina Integrations Documentation Scraper")
    print("=" * 70)
    print()

    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Remove existing documentation
    if OUTPUT_DIR.exists() and any(OUTPUT_DIR.glob("*.md")):
        print("Removing existing documentation files...")
        for file in OUTPUT_DIR.glob("*.md"):
            file.unlink()
            print(f"  Removed: {file.name}")

    # Create integration index first
    print("\nCreating integration index...")
    create_integration_index()

    # Scrape each integration
    print("\nScraping integrations...")
    scraped_count = 0

    for name, config in INTEGRATION_URLS.items():
        if scrape_langchain_integration(name, config["url"], config["description"]):
            scraped_count += 1

    # Verify extraction
    print("\nVerifying extraction...")
    if not OUTPUT_DIR.exists():
        print("  Error: Output directory was not created")
        sys.exit(1)

    md_files = list(OUTPUT_DIR.glob("*.md"))
    total_size = sum(f.stat().st_size for f in md_files)

    print(f"  Total files: {len(md_files)}")
    print(f"  Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")
    print(f"  Successfully scraped: {scraped_count}/{len(INTEGRATION_URLS)} integrations")

    # List files
    print("\n  Documentation files:")
    for md_file in sorted(md_files):
        file_size = md_file.stat().st_size
        print(f"    - {md_file.name} ({file_size:,} bytes)")

    print()
    print("=" * 70)
    print("Scraping Complete")
    print("=" * 70)
    print(f"Output: {OUTPUT_DIR}")
    print()


if __name__ == "__main__":
    main()
