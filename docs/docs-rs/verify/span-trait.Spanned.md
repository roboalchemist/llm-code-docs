verify::span
# Trait Spanned 
Source 

```
pub trait Spanned {
    type Span: Span;

    // Required method
    fn span(&self) -> Option<Self::Span>;
}
```

## Required Associated Types§