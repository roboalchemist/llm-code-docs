rome
# Module resource 
Source 
## Structs§
IRIA wrapper around `ResourceBase` that guarantees that the resource
is an IRI and not a blank node or a literal.IRISubjectIterIterate over all subjects that are an IRI for the given object and predicate.
In other words: no blank nodes are returned.ObjectIterIterate over all objects for the given subject and predicate.SubjectIterIterate over all subjects for the given object and predicate.
## Traits§
ResourceBaseBase trait for all ontology traits.