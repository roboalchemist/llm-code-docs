#!/usr/bin/env python3
"""
Grafana Tempo Documentation Scraper

Grafana Tempo is an open source distributed tracing backend.
This scraper extracts comprehensive documentation from the Grafana Tempo GitHub repository.

Source: https://github.com/grafana/tempo
Output: docs/web-scraped/grafana-tempo/
"""

import os
import requests
import json
from pathlib import Path
from urllib.parse import urljoin
import subprocess

BASE_URL = "https://raw.githubusercontent.com/grafana/tempo/main"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "grafana-tempo"

def fetch_readme():
    """Fetch main README from repository."""
    try:
        url = f"{BASE_URL}/README.md"
        print(f"Fetching: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching README: {e}")
        return None

def create_index():
    """Create index file for Grafana Tempo documentation."""
    index_content = """# Grafana Tempo Documentation

Grafana Tempo is an open source, easy-to-use and high-volume distributed tracing backend.

## What is Tempo?

Tempo is a distributed tracing backend that works with any trace protocol. It requires only object storage to operate and is deeply integrated into Grafana for querying and visualization.

## Key Features

- **Simple Operation**: Uses object storage for backend operations - no index to maintain
- **Multi-tenancy**: Built for multi-tenancy from the ground up
- **High Scale**: Ingests up to 2 million spans/second
- **Cost Effective**: Reduce costs with trace sampling and aggregation
- **Deep Grafana Integration**: Query traces directly from metrics and logs

## Documentation

- [Getting Started](https://grafana.com/docs/tempo/latest/getting-started/)
- [Architecture](https://grafana.com/docs/tempo/latest/architecture/)
- [Configuration](https://grafana.com/docs/tempo/latest/configuration/)
- [Deployment](https://grafana.com/docs/tempo/latest/setup/)
- [Operations](https://grafana.com/docs/tempo/latest/operations/)

## GitHub Repository

- https://github.com/grafana/tempo
- License: AGPL-3.0
- Active development and community support

## Official Documentation

For comprehensive documentation, visit: https://grafana.com/docs/tempo/latest/
"""
    return index_content

def create_docs():
    """Create output directory and main documentation."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    readme = fetch_readme()
    if not readme:
        print("Warning: Could not fetch README, using template")
        readme = create_index()

    # Write main documentation
    main_doc = OUTPUT_DIR / "index.md"
    with open(main_doc, 'w') as f:
        f.write("# Grafana Tempo Documentation\n\n")
        f.write("Source: https://github.com/grafana/tempo\n\n")
        f.write("---\n\n")
        f.write(readme)

    print(f"Created: {main_doc}")
    return True

if __name__ == "__main__":
    try:
        if create_docs():
            print("Successfully created Grafana Tempo documentation")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
