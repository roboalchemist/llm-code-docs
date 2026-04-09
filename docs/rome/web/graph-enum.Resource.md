rome::graph
# Enum Resource 
Source 

```
pub enum Resource<'g, B, I, L>where
    B: BlankNodePtr<'g> + 'g,
    I: IRIPtr<'g> + 'g,
    L: LiteralPtr<'g> + 'g,{
    BlankNode(B, PhantomData<&'g u8>),
    IRI(I),
    Literal(L),
}
```

## Variants§
§
### BlankNode(B, PhantomData<&'g u8>)