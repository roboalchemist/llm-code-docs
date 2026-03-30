bellman::gadgets::blake2s
# Function blake2s 
Source 

```
pub fn blake2s<Scalar: PrimeField, CS: ConstraintSystem<Scalar>>(
    cs: CS,
    input: &[Boolean],
    personalization: &[u8],
) -> Result<Vec<Boolean>, SynthesisError>
```