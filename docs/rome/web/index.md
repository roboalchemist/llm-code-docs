# Crate rome 
Source 
## Re-exports§
`pub use error::Result;`
## Modules§
errorThe error and result types for this crate.graphThe main module of this crate. It has traits for RDF graphs.graphsA number of Graph implementations.ioFunctions for reading and writing RDF files.iterA number of iterators used in Rome.namespacesCode for dealing with namespaces in RDF files.ontologyOntology mapping for rdf: and rdfs:ontology_adapter`OntologyAdapter` allows accessing of a graph via an ontology.resourceHelper traits used in generated ontology code.
## Macros§
classgraph_collectionCreate a module for a collection of graphs.impl_triple_cmp_wrapGraphs that are used in GraphCollection must implement TripleCmpWrap.
This macro does that.propertyspo_ops