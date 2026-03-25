bellman::gadgets::lookup
# Function lookup3_xy_with_conditional_negation 
Source 

```
pub fn lookup3_xy_with_conditional_negation<Scalar: PrimeField, CS>(
    cs: CS,
    bits: &[Boolean],
    coords: &[(Scalar, Scalar)],
) -> Result<(Num<Scalar>, Num<Scalar>), SynthesisError>where
    CS: ConstraintSystem<Scalar>,
```