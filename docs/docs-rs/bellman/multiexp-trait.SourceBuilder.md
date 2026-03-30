bellman::multiexp
# Trait SourceBuilder 
Source 

```
pub trait SourceBuilder<G: PrimeCurveAffine>:
    Send
    + Sync
    + 'static
    + Clone {
    type Source: Source<G>;

    // Required method
    fn build(self) -> Self::Source;
}
```

## Required Associated Types§
Source
#### type Source: Source<G>