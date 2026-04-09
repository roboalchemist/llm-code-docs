bellman::gadgets::sha256
# Function sha256 
Source 

```
pub fn sha256<Scalar, CS>(
    cs: CS,
    input: &[Boolean],
) -> Result<Vec<Boolean>, SynthesisError>where
    Scalar: PrimeField,
    CS: ConstraintSystem<Scalar>,
```