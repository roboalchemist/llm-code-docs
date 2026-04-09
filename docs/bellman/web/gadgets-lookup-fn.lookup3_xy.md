bellman::gadgets::lookup
# Function lookup3_xy 
Source 

```
pub fn lookup3_xy<Scalar: PrimeField, CS>(
    cs: CS,
    bits: &[Boolean],
    coords: &[(Scalar, Scalar)],
) -> Result<(AllocatedNum<Scalar>, AllocatedNum<Scalar>), SynthesisError>where
    CS: ConstraintSystem<Scalar>,
```