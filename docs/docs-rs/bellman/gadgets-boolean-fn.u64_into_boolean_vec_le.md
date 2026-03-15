bellman::gadgets::boolean
# Function u64_into_boolean_vec_le 
Source 

```
pub fn u64_into_boolean_vec_le<Scalar: PrimeField, CS: ConstraintSystem<Scalar>>(
    cs: CS,
    value: Option<u64>,
) -> Result<Vec<Boolean>, SynthesisError>
```