verify
# Trait ValidateMap 
Source 

```
pub trait ValidateMap<S: Span> {
    type Error: Error;

    // Required methods
    fn with_span(&mut self, span: Option<S>) -> &mut Self;
    fn validate_key<V>(&mut self, key: &V) -> Result<(), Self::Error>
       where V: ?Sized + Validate<Span = S>;
    fn validate_string_key<V>(&mut self, key: &V) -> Result<(), Self::Error>
       where V: ?Sized + Validate<Span = S> + ToString;
    fn validate_value<V>(&mut self, value: &V) -> Result<(), Self::Error>
       where V: Validate<Span = S> + ?Sized;
    fn end(self) -> Result<(), Self::Error>;

    // Provided methods
    fn validate_entry<K, V>(
        &mut self,
        key: &K,
        value: &V,
    ) -> Result<(), Self::Error>
       where K: Validate<Span = S> + ?Sized,
             V: Validate<Span = S> + ?Sized { ... }
    fn validate_string_entry<K, V>(
        &mut self,
        key: &K,
        value: &V,
    ) -> Result<(), Self::Error>
       where K: ?Sized + Validate<Span = S> + ToString,
             V: ?Sized + Validate<Span = S> { ... }
    fn string_key_required(&self) -> bool { ... }
}
```

## Required Associated Types§