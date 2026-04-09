rome::graph
# Enum WriterResource 
Source 

```
pub enum WriterResource<'g, W>where
    W: GraphWriter<'g>,{
    BlankNode(W::BlankNode, PhantomData<&'g u8>),
    IRI(W::IRI),
    Literal(W::Literal),
}
```

## Variants§
§
### BlankNode(W::BlankNode, PhantomData<&'g u8>)