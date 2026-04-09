rome
# Module graph 
Source 
## Enums§
BlankNodeOrIRIAn enum that contains a blank node or an IRIResourceA Resource is a blank node, an IRI or a literal.WriterBlankNodeOrIRI`WriterBlankNodeOrIRI` is like `BlankNodeOrIRI` but for writing graphs.WriterResource`WriterResource` is like `Resource` but for writing graphs.
## Traits§
BlankNodePtrInstances of this trait point to a blank node in a graph.DatatypePtrA trait for a pointers to datatypes of literals in graphs.GraphAn RDF graph.GraphWriterTrait for writing into a graph.IRIPtrA trait for a pointers to IRI in graphs.LiteralPtrA trait for a pointers to literals in graphs.ResourceTranslatortranslate from one graph to another
useful for inferencing
there can be a general implemenation as wel as an optimized one that’s
used when extending a graph by inferencing from its own contentTripleTriples are fundamental to RDF.