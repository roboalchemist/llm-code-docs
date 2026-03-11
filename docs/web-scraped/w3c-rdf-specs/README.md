# W3C RDF (Resource Description Framework) Specifications

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
