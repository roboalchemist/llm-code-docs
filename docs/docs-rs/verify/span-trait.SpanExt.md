verify::span
# Trait SpanExt 
Source 

```
pub trait SpanExt: Sized + Clone {
    // Required method
    fn combine(&mut self, span: Self);

    // Provided method
    fn combined(&self, span: Self) -> Self { ... }
}
```

## Required Methods§