verify
# Trait Verifier 
Source 

```
pub trait Verifier<S: Span> {
    type Error: Error;

    // Required method
    fn verify_value<V: ?Sized + Validate<Span = S>>(
        &self,
        value: &V,
    ) -> Result<(), Self::Error>;

    // Provided method
    fn verify_value_with_span<V: ?Sized + Validate<Span = S>>(
        &self,
        value: &V,
        _span: Option<V::Span>,
    ) -> Result<(), Self::Error> { ... }
}
```

## Required Associated Types§