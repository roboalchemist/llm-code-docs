wundergraph::query_builder::selection::fields
# Trait FieldListExtractor 
Source 

```
pub trait FieldListExtractor {
    type Out;

    const FIELD_COUNT: usize;

    // Required method
    fn map<F: Fn(usize) -> R, R>(local_index: usize, callback: F) -> Option<R>;
}
```

## Required Associated Constants§