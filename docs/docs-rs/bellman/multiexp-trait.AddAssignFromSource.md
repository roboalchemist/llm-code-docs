bellman::multiexp
# Trait AddAssignFromSource 
Source 

```
pub trait AddAssignFromSource: PrimeCurve {
    // Provided method
    fn add_assign_from_source<S: Source<<Self as PrimeCurve>::Affine>>(
        &mut self,
        source: &mut S,
    ) -> Result<(), SynthesisError> { ... }
}
```

## Provided Methods§