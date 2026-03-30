bellman::gadgets::sha256
# Function sha256_block_no_padding 
Source 

```
pub fn sha256_block_no_padding<Scalar, CS>(
    cs: CS,
    input: &[Boolean],
) -> Result<Vec<Boolean>, SynthesisError>where
    Scalar: PrimeField,
    CS: ConstraintSystem<Scalar>,
```