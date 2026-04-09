rome::resource
# Trait ResourceBase 
Source 

```
pub trait ResourceBase<'g>: Clone + Ord {
    type Graph: Graph<'g>;

    // Required methods
    fn new(
        this: Resource<'g, <<Self as ResourceBase<'g>>::Graph as Graph<'g>>::BlankNodePtr, <<Self as ResourceBase<'g>>::Graph as Graph<'g>>::IRIPtr, <<Self as ResourceBase<'g>>::Graph as Graph<'g>>::LiteralPtr>,
        graph: &'g OntologyAdapter<'g, Self::Graph>,
    ) -> Self;
    fn iter(graph: &'g OntologyAdapter<'g, Self::Graph>) -> Self::SubjectIter;
    fn this(
        &self,
    ) -> &Resource<'g, <<Self as ResourceBase<'g>>::Graph as Graph<'g>>::BlankNodePtr, <<Self as ResourceBase<'g>>::Graph as Graph<'g>>::IRIPtr, <<Self as ResourceBase<'g>>::Graph as Graph<'g>>::LiteralPtr>;
    fn adapter(&self) -> &'g OntologyAdapter<'g, Self::Graph>;

    // Provided methods
    fn iter_objects<O>(
        &self,
        predicate: Option<&<<Self as ResourceBase<'g>>::Graph as Graph<'g>>::IRIPtr>,
    ) -> ObjectIter<'g, O> ⓘ
       where O: ResourceBase<'g, Graph = Self::Graph>,
             Self: 'g { ... }
    fn iri(&self) -> Option<IRI<'g, Self>> { ... }
}
```

## Required Associated Types§