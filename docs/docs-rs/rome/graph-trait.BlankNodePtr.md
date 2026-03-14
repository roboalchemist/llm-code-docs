rome::graph
# Trait BlankNodePtr 
Source 

```
pub trait BlankNodePtr<'g> {
    // Provided methods
    fn to_blank_node_or_iri<I>(&self) -> BlankNodeOrIRI<'g, Self, I>
       where Self: Clone,
             I: IRIPtr<'g> { ... }
    fn to_resource<I, L>(&self) -> Resource<'g, Self, I, L>
       where Self: Clone,
             I: IRIPtr<'g>,
             L: LiteralPtr<'g> { ... }
}
```

## Provided Methods§