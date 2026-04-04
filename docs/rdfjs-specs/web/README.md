# RDF/JS (JavaScript) Specifications

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
