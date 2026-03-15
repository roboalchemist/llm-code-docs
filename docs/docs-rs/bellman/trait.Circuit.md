bellman
# Trait Circuit 
Source 

```
pub trait Circuit<Scalar: PrimeField> {
    // Required method
    fn synthesize<CS: ConstraintSystem<Scalar>>(
        self,
        cs: &mut CS,
    ) -> Result<(), SynthesisError>;
}
```

## Required Methods§