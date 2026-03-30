bellman::multiexp
# Trait Source 
Source 

```
pub trait Source<G: PrimeCurveAffine> {
    // Required methods
    fn next(&mut self) -> Result<&G, SynthesisError>;
    fn skip(&mut self, amt: usize) -> Result<(), SynthesisError>;
}
```

## Required Methods§
Source
#### fn next(&mut self) -> Result<&G, SynthesisError>