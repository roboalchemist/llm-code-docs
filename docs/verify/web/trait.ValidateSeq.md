verify
# Trait ValidateSeq 
Source 

```
pub trait ValidateSeq<S: Span> {
    type Error: Error;

    // Required methods
    fn with_span(&mut self, span: Option<S>) -> &mut Self;
    fn validate_element<V>(&mut self, value: &V) -> Result<(), Self::Error>
       where V: ?Sized + Validate<Span = S> + Hash;
    fn end(self) -> Result<(), Self::Error>;
}
```

## Required Associated Types§