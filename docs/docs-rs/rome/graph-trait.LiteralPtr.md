rome::graph
# Trait LiteralPtr 
Source 

```
pub trait LiteralPtr<'g> {
    type DatatypePtr: DatatypePtr<'g> + PartialEq;

    // Required methods
    fn as_str(&self) -> &str;
    fn datatype(&self) -> Self::DatatypePtr;
    fn datatype_str(&self) -> &str;
    fn language(&self) -> Option<&str>;

    // Provided method
    fn to_resource<B, I>(&self) -> Resource<'g, B, I, Self>
       where Self: Clone,
             B: BlankNodePtr<'g>,
             I: IRIPtr<'g> { ... }
}
```

## Required Associated Types§