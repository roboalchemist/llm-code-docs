# GraphML Documentation Index

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
