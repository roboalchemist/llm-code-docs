rome::graph
# Trait Triple 
Source 

```
pub trait Triple<'g, B, I, L>where
    B: BlankNodePtr<'g>,
    I: IRIPtr<'g>,
    L: LiteralPtr<'g>,{
    // Required methods
    fn subject(&self) -> BlankNodeOrIRI<'g, B, I>;
    fn predicate(&self) -> I;
    fn object(&self) -> Resource<'g, B, I, L>;
}
```

## Required Methods§