rome::graph
# Enum BlankNodeOrIRI 
Source 

```
pub enum BlankNodeOrIRI<'g, B, I>where
    B: BlankNodePtr<'g> + 'g,
    I: IRIPtr<'g> + 'g,{
    BlankNode(B, PhantomData<&'g u8>),
    IRI(I),
}
```

## Variants§
§
### BlankNode(B, PhantomData<&'g u8>)