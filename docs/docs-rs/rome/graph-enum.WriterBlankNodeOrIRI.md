rome::graph
# Enum WriterBlankNodeOrIRI 
Source 

```
pub enum WriterBlankNodeOrIRI<'g, W>where
    W: GraphWriter<'g>,{
    BlankNode(W::BlankNode, PhantomData<&'g u8>),
    IRI(W::IRI),
}
```

## Variants§
§
### BlankNode(W::BlankNode, PhantomData<&'g u8>)