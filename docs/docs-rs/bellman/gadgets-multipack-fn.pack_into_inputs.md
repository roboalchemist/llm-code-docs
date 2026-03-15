bellman::gadgets::multipack
# Function pack_into_inputs 
Source 

```
pub fn pack_into_inputs<Scalar, CS>(
    cs: CS,
    bits: &[Boolean],
) -> Result<(), SynthesisError>where
    Scalar: PrimeField,
    CS: ConstraintSystem<Scalar>,
```