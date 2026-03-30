#!/usr/bin/env python3
"""
Scraper for W3C RDF (Resource Description Framework) specifications.
Output: docs/web-scraped/w3c-rdf-specs/

Fetches the core RDF 1.1 specifications from W3C including:
- RDF Concepts and Abstract Syntax
- RDF Semantics
- RDF Turtle serialization
- JSON-LD
- SPARQL Query Language
- N-Triples, N-Quads
"""

import re
import requests
from pathlib import Path
from urllib.parse import urljoin
from markdownify import markdownify as md

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "w3c-rdf-specs"

# Core RDF 1.1 specifications from W3C
SPECS = {
    "rdf-concepts": {
        "url": "https://www.w3.org/TR/rdf11-concepts/",
        "title": "RDF 1.1 Concepts and Abstract Syntax",
        "description": "Defines the abstract syntax and formal model for RDF (Resource Description Framework), covering RDF graphs, IRIs, literals, and datatypes."
    },
    "rdf-semantics": {
        "url": "https://www.w3.org/TR/rdf11-semantics/",
        "title": "RDF 1.1 Semantics",
        "description": "Provides formal semantics and model-theoretic foundations for RDF, including entailment and reasoning rules."
    },
    "turtle": {
        "url": "https://www.w3.org/TR/turtle/",
        "title": "RDF 1.1 Turtle - Terse RDF Triple Language",
        "description": "Specification for Turtle, a human-readable serialization format for RDF that is easier to read than RDF/XML."
    },
    "json-ld": {
        "url": "https://www.w3.org/TR/json-ld11/",
        "title": "JSON-LD 1.1 - A JSON-based Serialization for Linked Data",
        "description": "Specification for JSON-LD, a JSON-based format for expressing linked data, widely used in modern RDF applications."
    },
    "sparql-overview": {
        "url": "https://www.w3.org/TR/sparql11-overview/",
        "title": "SPARQL 1.1 Overview",
        "description": "Overview of SPARQL 1.1 specifications for querying and manipulating RDF data and linked data on the Web."
    },
    "sparql-query": {
        "url": "https://www.w3.org/TR/sparql11-query/",
        "title": "SPARQL 1.1 Query Language",
        "description": "Specification for the SPARQL 1.1 query language for retrieving and manipulating data stored in RDF format."
    },
    "sparql-update": {
        "url": "https://www.w3.org/TR/sparql11-update/",
        "title": "SPARQL 1.1 Update",
        "description": "Specification for SPARQL 1.1 Update, enabling modification of RDF graphs on SPARQL endpoints."
    },
    "n-triples": {
        "url": "https://www.w3.org/TR/n-triples/",
        "title": "RDF 1.1 N-Triples - A line-based syntax for RDF",
        "description": "Specification for N-Triples, a line-based serialization format for RDF that is easy to parse and process."
    },
    "n-quads": {
        "url": "https://www.w3.org/TR/n-quads/",
        "title": "RDF 1.1 N-Quads - Extending N-Triples with context",
        "description": "Specification for N-Quads, an extension of N-Triples that adds the ability to represent RDF datasets with named graphs."
    },
    "rdf-xml": {
        "url": "https://www.w3.org/TR/rdf-xml/",
        "title": "RDF 1.1 XML Syntax",
        "description": "Specification for RDF/XML, an XML-based serialization format for RDF (older than Turtle but still widely used)."
    },
}

def clean_html(html_content: str) -> str:
    """Remove script tags and other non-content elements from HTML."""
    # Remove script tags
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    # Remove style tags
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    return html_content

def fetch_specification(spec_key: str, spec_info: dict) -> bool:
    """Fetch a single W3C specification and save as markdown."""
    url = spec_info["url"]
    title = spec_info["title"]
    description = spec_info["description"]

    try:
        print(f"  Fetching {title}...", end=" ", flush=True)
        headers = {
            'Accept-Encoding': 'gzip, deflate',  # Skip brotli to avoid encoding issues
        }
        response = requests.get(url, timeout=30, headers=headers)
        response.raise_for_status()

        # Clean HTML and convert to markdown
        cleaned_html = clean_html(response.text)
        markdown_content = md(cleaned_html)

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
    print("Scraping W3C RDF Specifications...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Create index
    index_content = """# W3C RDF (Resource Description Framework) Specifications

This directory contains W3C specifications for RDF and related technologies, including:
- Core RDF concepts and abstract syntax
- SPARQL query and update languages
- Serialization formats (Turtle, JSON-LD, N-Triples, N-Quads, RDF/XML)

## Core Specifications

### RDF 1.1
- **[RDF 1.1 Concepts and Abstract Syntax](rdf-concepts.md)** - The normative definition of RDF graph syntax and semantics
- **[RDF 1.1 Semantics](rdf-semantics.md)** - Formal model-theoretic semantics for RDF entailment

### RDF Serialization Formats
- **[RDF 1.1 Turtle](turtle.md)** - Human-readable RDF serialization format
- **[RDF 1.1 XML Syntax](rdf-xml.md)** - XML-based RDF serialization (legacy)
- **[RDF 1.1 N-Triples](n-triples.md)** - Line-based RDF serialization for easy parsing
- **[RDF 1.1 N-Quads](n-quads.md)** - Extension of N-Triples supporting named graphs
- **[JSON-LD 1.1](json-ld.md)** - JSON-based serialization for linked data

### SPARQL Query Language
- **[SPARQL 1.1 Overview](sparql-overview.md)** - Overview of SPARQL specifications
- **[SPARQL 1.1 Query Language](sparql-query.md)** - Query language for RDF
- **[SPARQL 1.1 Update](sparql-update.md)** - Specification for updating RDF graphs

## Key Concepts

### RDF Basics
- **Triple**: The fundamental RDF data structure (subject, predicate, object)
- **IRI**: Internationalized Resource Identifier for identifying resources
- **Literal**: Values such as strings, numbers, dates
- **Blank Node**: Anonymous resources without explicit IRIs
- **RDF Graph**: A set of RDF triples

### SPARQL
- **SPARQL Query**: SELECT, CONSTRUCT, DESCRIBE, ASK query forms
- **SPARQL Update**: INSERT, DELETE, LOAD, CLEAR operations
- **SPARQL Endpoint**: HTTP service providing SPARQL query/update access
- **SPARQL Results**: XML, JSON, CSV, TSV result formats

## Learning Path

1. Start with [RDF 1.1 Concepts](rdf-concepts.md) to understand core RDF concepts
2. Learn [Turtle](turtle.md) syntax for readable RDF serialization
3. Explore [SPARQL Query Language](sparql-query.md) to query RDF data
4. Check other formats ([JSON-LD](json-ld.md), [N-Triples](n-triples.md)) as needed

## Related Technologies

- **Linked Data**: Publication of RDF on the web using HTTP and IRIs
- **RDFa**: HTML5 extension for embedding RDF in web pages
- **Semantic Web**: Web of machine-readable data using RDF, SPARQL, and ontologies
- **OWL**: Web Ontology Language (uses RDF for knowledge representation)
- **SKOS**: Simple Knowledge Organization System (uses RDF for taxonomies)

---

All specifications are W3C Recommendations published by the World Wide Web Consortium.
"""

    (OUTPUT_DIR / "README.md").write_text(index_content, encoding='utf-8')
    print(f"Created {OUTPUT_DIR}/README.md")

    # Fetch each specification
    success_count = 0
    for spec_key, spec_info in SPECS.items():
        if fetch_specification(spec_key, spec_info):
            success_count += 1

    print(f"\nCompleted: {success_count}/{len(SPECS)} specifications fetched")
    return success_count == len(SPECS)

if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
