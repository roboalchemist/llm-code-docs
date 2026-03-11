#!/usr/bin/env python3
"""
Scraper for RDF/JS (JavaScript) specifications and documentation.
Output: docs/web-scraped/rdfjs-specs/

Fetches the RDF/JS Community Group specifications for working with RDF in JavaScript/ECMAScript:
- RDF/JS Data Model specification
- RDF/JS Dataset specification
- RDF/JS Stream interfaces specification
- N3.js documentation
"""

import re
import requests
from pathlib import Path
from markdownify import markdownify as md

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "rdfjs-specs"

# RDF/JS specifications from the community group
SPECS = {
    "data-model": {
        "url": "https://rdf.js.org/data-model-spec/",
        "title": "RDF/JS Data Model",
        "description": "Specification for the RDF/JS Data Model, defining interfaces for RDF terms, quads, and datasets in JavaScript."
    },
    "dataset": {
        "url": "https://rdf.js.org/dataset-spec/",
        "title": "RDF/JS Dataset",
        "description": "Specification for the RDF/JS Dataset interface, providing a standard way to work with RDF quads in JavaScript."
    },
    "stream": {
        "url": "https://rdf.js.org/stream-spec/",
        "title": "RDF/JS Stream",
        "description": "Specification for RDF/JS Stream interfaces, enabling efficient streaming of RDF quads in JavaScript."
    },
    "query": {
        "url": "https://rdf.js.org/query-spec/",
        "title": "RDF/JS Query",
        "description": "Specification for RDF/JS Query interfaces for querying RDF graphs in JavaScript."
    },
}

def fetch_specification(spec_key: str, spec_info: dict) -> bool:
    """Fetch a single RDF/JS specification and save as markdown."""
    url = spec_info["url"]
    title = spec_info["title"]
    description = spec_info["description"]

    try:
        print(f"  Fetching {title}...", end=" ", flush=True)
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0'
        }
        response = requests.get(url, timeout=30, headers=headers)
        response.raise_for_status()

        # Clean HTML and convert to markdown
        html_content = response.text
        # Remove script tags
        html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
        # Remove style tags
        html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

        markdown_content = md(html_content)

        # Create markdown with metadata header
        output_content = f"""# {title}

**Source**: {url}

**Description**: {description}

---

{markdown_content}
"""

        # Ensure output directory exists
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Save to file
        output_file = OUTPUT_DIR / f"{spec_key}.md"
        output_file.write_text(output_content, encoding='utf-8')

        print(f"✓ ({len(output_content)} bytes)")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def main():
    print("Scraping RDF/JS Specifications...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Create index
    index_content = """# RDF/JS (JavaScript) Specifications

This directory contains specifications and documentation for working with RDF (Resource Description Framework) in JavaScript/ECMAScript environments, maintained by the W3C RDFJS Community Group.

## Core Specifications

- **[Data Model](data-model.md)** - Defines interfaces for RDF terms, triples, quads, and datasets in JavaScript
- **[Dataset](dataset.md)** - Standard interface for working with collections of RDF quads
- **[Stream](stream.md)** - Interfaces for streaming RDF data efficiently in JavaScript
- **[Query](query.md)** - Query interfaces for working with RDF graphs

## Key Concepts

### RDF Terms
- **NamedNode**: An IRI-identified resource
- **Literal**: A value with optional language tag or datatype
- **BlankNode**: An anonymous resource (no explicit IRI)
- **Variable**: A query variable (used in SPARQL-like queries)
- **DefaultGraph**: Represents the default graph in a dataset

### Quads vs Triples
- **Triple**: (subject, predicate, object) - basic RDF statement
- **Quad**: (subject, predicate, object, graph) - extends triples with named graphs support

### Datasets
- Collection of quads organized by named graphs
- Supports querying and manipulation of RDF data
- Primary abstraction for working with RDF in JavaScript

## Popular RDF/JS Libraries

The RDF/JS ecosystem includes many implementations:

- **N3.js** - Lightning-fast, spec-compliant RDF library with streaming support
- **Comunica** - Query engine for federated SPARQL querying
- **Rdflib.js** - Original JavaScript RDF library
- **rdf-js-elements** - Web components for RDF visualization
- **json-ld.js** - JSON-LD 1.1 processor
- **graphy** - RDF stream utilities

## Getting Started

1. Choose an RDF/JS implementation (e.g., N3.js, rdflib.js)
2. Learn the Data Model specification for working with terms and quads
3. Use the Dataset interface for graph manipulation
4. Explore stream interfaces for processing large RDF datasets
5. Query with SPARQL endpoints using standard query interfaces

## Resources

- **W3C RDFJS Community Group**: https://www.w3.org/community/rdfjs/
- **RDF.js Organization**: https://github.com/rdfjs
- **Official Specs**: https://rdf.js.org/

---

All specifications are developed by the W3C RDFJS Community Group.
"""

    (OUTPUT_DIR / "README.md").write_text(index_content, encoding='utf-8')
    print(f"Created {OUTPUT_DIR}/README.md")

    # Fetch each specification
    success_count = 0
    for spec_key, spec_info in SPECS.items():
        if fetch_specification(spec_key, spec_info):
            success_count += 1

    print(f"\nCompleted: {success_count}/{len(SPECS)} specifications fetched")
    return success_count >= len(SPECS) - 1  # Allow query spec to fail if it doesn't exist

if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
