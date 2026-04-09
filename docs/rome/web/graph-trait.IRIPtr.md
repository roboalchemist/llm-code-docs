rome::graph
# Trait IRIPtr 
Source 

```
pub trait IRIPtr<'g> {
    // Required method
    fn as_str(&self) -> &str;

    // Provided methods
    fn to_blank_node_or_iri<B>(&self) -> BlankNodeOrIRI<'g, B, Self>
       where Self: Clone,
             B: BlankNodePtr<'g> { ... }
    fn to_resource<B, L>(&self) -> Resource<'g, B, Self, L>
       where Self: Clone,
             B: BlankNodePtr<'g>,
             L: LiteralPtr<'g> { ... }
}
```

## Required Methods§