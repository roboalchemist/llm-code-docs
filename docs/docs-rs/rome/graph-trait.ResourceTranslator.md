rome::graph
# Trait ResourceTranslator 
Source 

```
pub trait ResourceTranslator<'g> {
    type Graph: Graph<'g>;
    type GraphWriter: GraphWriter<'g>;

    // Required method
    fn translate_blank_node(
        &mut self,
        w: &mut Self::GraphWriter,
        blank_node: &<Self::Graph as Graph<'g>>::BlankNodePtr,
    ) -> <Self::GraphWriter as GraphWriter<'g>>::BlankNode;

    // Provided methods
    fn translate_blank_node_or_iri(
        &mut self,
        w: &mut Self::GraphWriter,
        blank_node_or_iri: &BlankNodeOrIRI<'g, <Self::Graph as Graph<'g>>::BlankNodePtr, <Self::Graph as Graph<'g>>::IRIPtr>,
    ) -> WriterBlankNodeOrIRI<'g, Self::GraphWriter>
       where Self: 'g { ... }
    fn translate_resource(
        &mut self,
        w: &mut Self::GraphWriter,
        resource: &Resource<'g, <Self::Graph as Graph<'g>>::BlankNodePtr, <Self::Graph as Graph<'g>>::IRIPtr, <Self::Graph as Graph<'g>>::LiteralPtr>,
    ) -> WriterResource<'g, Self::GraphWriter>
       where Self: 'g { ... }
}
```

## Required Associated Types§