#!/usr/bin/env python3
"""
Scraper for GraphML documentation from graphml.graphdrawing.org
Output: docs/web-scraped/graphml/

This scraper fetches and converts GraphML specification, primer, and DTD/XSD docs
from the official GraphML website into Markdown format.
"""

import requests
import re
from pathlib import Path
from html.parser import HTMLParser
from html2text import html2text
from urllib.parse import urljoin

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "graphml"
BASE_URL = "http://graphml.graphdrawing.org"

# Create output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

class GraphMLExtractor(HTMLParser):
    """Extract main content from GraphML HTML pages"""
    def __init__(self):
        super().__init__()
        self.in_body = False
        self.content = []
        self.skip_tags = {'script', 'style', 'noscript'}
        self.skip = False

    def handle_starttag(self, tag, attrs):
        if tag == 'body':
            self.in_body = True
        elif tag in self.skip_tags:
            self.skip = True

    def handle_endtag(self, tag):
        if tag == 'body':
            self.in_body = False
        elif tag in self.skip_tags:
            self.skip = False

    def handle_data(self, data):
        if self.in_body and not self.skip:
            self.content.append(data)

    def get_content(self):
        return ''.join(self.content)

def fetch_and_convert(url, title):
    """Fetch a page and convert to Markdown"""
    print(f"Fetching {title} from {url}...")
    try:
        response = requests.get(url, timeout=10)
        response.encoding = 'iso-8859-1'
        response.raise_for_status()

        # Extract body content
        body_match = re.search(r'<body[^>]*>(.*?)</body>', response.text, re.DOTALL | re.IGNORECASE)
        if body_match:
            html_content = body_match.group(1)
        else:
            html_content = response.text

        # Convert HTML to Markdown
        markdown = html2text(html_content, bodywidth=100)
        return markdown
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def create_introduction():
    """Create introduction document"""
    intro = """# GraphML Documentation

GraphML (Graph Markup Language) is an XML-based file format for graphs used in network analysis, graph visualization, and computational graph theory.

## Overview

GraphML is designed to be:
- **Flexible**: Supports various graph types (directed, undirected, mixed) and nested structures
- **Extensible**: Allows custom data attributes on graphs, nodes, edges, and other elements
- **Interoperable**: XML-based format supported by many graph visualization and analysis tools
- **Human-readable**: Text-based XML format easy to inspect and debug

## Official Resources

- **Specification**: http://graphml.graphdrawing.org/specification/
- **Primer**: http://graphml.graphdrawing.org/primer/graphml-primer.html
- **DTD Reference**: http://graphml.graphdrawing.org/specification/dtd.html
- **XSD Reference**: http://graphml.graphdrawing.org/specification/xsd.html
- **FAQ**: http://graphml.graphdrawing.org/faq/

## Common Use Cases

- Network topology visualization
- Social network analysis
- Knowledge graph representation
- Computational workflow graphs
- Dependency graphs (software, project management)
- Visualization tool data exchange (Gephi, yEd, Cytoscape)

## Quick Links

- **Specification & DTD** - Full element definitions and attributes
- **Primer** - Tutorial and common patterns
- **Examples** - Code samples for parsing and creating GraphML files
- **Tools** - Ecosystem of parsers and visualization tools

## File Extension

GraphML files typically use the `.graphml` extension.
"""
    return intro

def create_quick_reference():
    """Create a quick reference guide"""
    reference = """# GraphML Quick Reference

## Basic Document Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns
                             http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">
  <key id="attr1" for="node" attr.name="label" attr.type="string"/>
  <graph id="G" edgedefault="undirected">
    <node id="n1">
      <data key="attr1">Node 1</data>
    </node>
    <edge id="e1" source="n1" target="n2"/>
  </graph>
</graphml>
```

## Root Elements

### `<graphml>`
Root element containing the entire graph definition.

**Attributes:**
- `xmlns` - XML namespace (required): `http://graphml.graphdrawing.org/xmlns`
- `version` - GraphML version (typically "1.0")

**Child Elements:**
- `<key>` - Define custom data attributes (0 or more)
- `<graph>` - The actual graph definition (1 or more)

### `<graph>`
Container for nodes and edges.

**Attributes:**
- `id` - Unique identifier (required)
- `edgedefault` - Default edge direction: `directed` or `undirected` (required)
- `parse.nodeids` - Node ID validation: `free` or `canonical`
- `parse.edgeids` - Edge ID validation: `free` or `canonical`
- `parse.order` - Edge order tracking: `free` or `canonical`

**Child Elements:**
- `<desc>` - Optional description
- `<data>` - Custom graph attributes
- `<node>` - Node definitions (0 or more)
- `<edge>` - Edge definitions (0 or more)
- `<graph>` - Nested subgraphs (for hierarchical graphs)

### `<node>`
Represents a single node/vertex in the graph.

**Attributes:**
- `id` - Unique identifier within the graph (required)

**Child Elements:**
- `<desc>` - Optional description
- `<data>` - Custom node attributes

### `<edge>`
Represents a connection between two nodes.

**Attributes:**
- `id` - Unique identifier (optional but recommended)
- `source` - ID of source node (required)
- `target` - ID of target node (required)
- `directed` - Override default edge direction: `true` or `false`

**Child Elements:**
- `<desc>` - Optional description
- `<data>` - Custom edge attributes

### `<data>`
Associates custom data with an element.

**Attributes:**
- `key` - References a `<key>` element's id (required)

**Content:** The actual data value

### `<key>`
Defines custom attributes for nodes, edges, graphs, or ports.

**Attributes:**
- `id` - Unique identifier (required)
- `for` - Element type: `graph`, `node`, `edge`, `all` (required)
- `attr.name` - Attribute name (required for typed keys)
- `attr.type` - Data type: `boolean`, `int`, `long`, `float`, `double`, `string` (optional)
- `attr.default` - Default value if not specified (optional)

**Child Elements:**
- `<desc>` - Description
- `<default>` - Default value

## Common Data Types

| Type | Description | Example |
|------|-------------|---------|
| `string` | Text data | "Hello" |
| `int` | 32-bit integer | 42 |
| `long` | 64-bit integer | 9223372036854775807 |
| `float` | Single precision | 3.14 |
| `double` | Double precision | 3.141592653589793 |
| `boolean` | True/false | true |

## Practical Examples

### Simple Undirected Graph

```xml
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <graph id="simple" edgedefault="undirected">
    <node id="a"/>
    <node id="b"/>
    <node id="c"/>
    <edge source="a" target="b"/>
    <edge source="b" target="c"/>
    <edge source="c" target="a"/>
  </graph>
</graphml>
```

### Graph with Node Labels

```xml
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <key id="label" for="node" attr.name="label" attr.type="string"/>
  <graph id="labeled" edgedefault="directed">
    <node id="n1">
      <data key="label">Node 1</data>
    </node>
    <node id="n2">
      <data key="label">Node 2</data>
    </node>
    <edge id="e1" source="n1" target="n2"/>
  </graph>
</graphml>
```

### Mixed Directed/Undirected Edges

```xml
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <graph id="mixed" edgedefault="undirected">
    <node id="a"/>
    <node id="b"/>
    <node id="c"/>
    <!-- Undirected (uses default) -->
    <edge source="a" target="b"/>
    <!-- Directed (overrides default) -->
    <edge source="b" target="c" directed="true"/>
  </graph>
</graphml>
```

### Graph with Multiple Custom Attributes

```xml
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <key id="label" for="node" attr.name="label" attr.type="string"/>
  <key id="weight" for="node" attr.name="weight" attr.type="double" attr.default="1.0"/>
  <key id="color" for="node" attr.name="color" attr.type="string" attr.default="white"/>

  <graph id="weighted" edgedefault="directed">
    <node id="n1">
      <data key="label">Start</data>
      <data key="weight">10.5</data>
      <data key="color">red</data>
    </node>
    <node id="n2">
      <data key="label">End</data>
      <data key="weight">5.3</data>
    </node>
    <edge source="n1" target="n2"/>
  </graph>
</graphml>
```

### Hypergraph (Nested Nodes)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <graph id="hypergraph" edgedefault="directed">
    <node id="group1">
      <graph id="subgraph1" edgedefault="directed">
        <node id="n1"/>
        <node id="n2"/>
        <edge source="n1" target="n2"/>
      </graph>
    </node>
    <node id="group2">
      <graph id="subgraph2" edgedefault="directed">
        <node id="n3"/>
      </graph>
    </node>
    <edge source="group1" target="group2"/>
  </graph>
</graphml>
```

## Nested Graphs (Hierarchical Graphs)

Nodes can contain graphs, creating hierarchical structures:

```xml
<node id="compound">
  <graph id="inner" edgedefault="directed">
    <node id="inner_node1"/>
    <node id="inner_node2"/>
    <edge source="inner_node1" target="inner_node2"/>
  </graph>
</node>
```

This is useful for:
- Compound graphs (nodes containing subgraphs)
- Cluster visualization
- Hierarchical network representation

## Schema Validation

All GraphML documents should include:

```xml
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns
                    http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd"
```

This enables XML schema validation against the official XSD.

## Best Practices

1. **Always include namespace declaration** - Required for valid GraphML
2. **Use meaningful IDs** - Make node/edge IDs descriptive when possible
3. **Define keys before use** - All `<key>` elements should come before graphs
4. **Specify edge direction** - Explicitly set `edgedefault` for clarity
5. **Validate against XSD** - Use XML validators to catch errors early
6. **Use appropriate data types** - Choose the right type for each attribute
7. **Add descriptions** - Include `<desc>` elements for complex structures
8. **Default values** - Set sensible defaults in `<key>` definitions

## Limitations and Considerations

- GraphML doesn't enforce uniqueness across graphs (only within a graph)
- Edge IDs must be unique within a graph
- No built-in support for parallel edges (multiple edges between same nodes)
- Nested graphs may not be supported by all visualization tools
- Large graphs can create large XML files (consider compression)

## File Size Optimization

For large graphs:
- Use gzip compression (`.graphml.gz`)
- Consider specialized graph formats (GraphSON, edge list)
- Remove unnecessary attributes
- Omit edge IDs if not required

## Tools and Libraries

See the Ecosystem & Tools section for parsers, validators, and visualization software supporting GraphML.
"""
    return reference

def main():
    """Download and process GraphML documentation"""
    documents = {
        "01-introduction.md": create_introduction(),
        "02-quick-reference.md": create_quick_reference(),
    }

    # Fetch official documents
    fetch_sources = [
        ("http://graphml.graphdrawing.org/primer/graphml-primer.html", "03-primer.md"),
        ("http://graphml.graphdrawing.org/specification/dtd.html", "04-dtd-specification.md"),
        ("http://graphml.graphdrawing.org/specification/xsd.html", "05-xsd-specification.md"),
    ]

    for url, filename in fetch_sources:
        markdown = fetch_and_convert(url, filename)
        if markdown:
            documents[filename] = markdown

    # Write all documents
    for filename, content in documents.items():
        if content:
            filepath = OUTPUT_DIR / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Created {filepath}")

    # Create index
    index_content = """# GraphML Documentation Index

This directory contains comprehensive documentation for GraphML (Graph Markup Language).

## Contents

- **01-introduction.md** - Overview of GraphML and its use cases
- **02-quick-reference.md** - Element definitions and practical examples
- **03-primer.md** - Official GraphML primer and tutorial
- **04-dtd-specification.md** - DTD (Document Type Definition) specification
- **05-xsd-specification.md** - XSD (XML Schema Definition) specification

## Getting Started

1. Start with **01-introduction.md** for an overview
2. Review **02-quick-reference.md** for common patterns
3. Consult **03-primer.md** for detailed examples and concepts
4. Reference **04-dtd-specification.md** and **05-xsd-specification.md** for complete element/attribute definitions

## Official Resources

- Official GraphML website: http://graphml.graphdrawing.org/
- Specification: http://graphml.graphdrawing.org/specification/
- FAQ: http://graphml.graphdrawing.org/faq/

## Key Concepts

- **Graphs**: Directed, undirected, or mixed edge types
- **Nodes**: Vertices in the graph with optional custom attributes
- **Edges**: Connections between nodes
- **Custom Data**: Extensible attributes via `<key>` elements
- **Nested Graphs**: Hierarchical/compound graphs with subgraphs

## Common Patterns

- Simple directed/undirected graphs
- Weighted graphs (node and edge weights)
- Labeled graphs (node and edge labels)
- Colored graphs (for visualization)
- Hierarchical/compound graphs
- Graphs with custom metadata

## Tools Support

GraphML is supported by many tools:
- **Visualization**: yEd, Gephi, Cytoscape, Graphviz (via plugins)
- **Parsing**: Python (networkx), Java (JGraphT), C# (.NET)
- **Analysis**: Community detection, centrality measures, pathfinding

## File Format

- Extension: `.graphml`
- MIME type: `application/graphml+xml`
- Encoding: UTF-8 (recommended)
- Compression: gzip (`.graphml.gz`) for large files
"""

    with open(OUTPUT_DIR / "README.md", 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"Created {OUTPUT_DIR / 'README.md'}")

    print(f"\nDocumentation complete: {OUTPUT_DIR}")
    print(f"Files created: {len(documents) + 1}")

if __name__ == "__main__":
    main()
