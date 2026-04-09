bellman::gadgets::boolean
# Function field_into_boolean_vec_le 
Source 

```
pub fn field_into_boolean_vec_le<Scalar: PrimeField, CS: ConstraintSystem<Scalar>, F: PrimeFieldBits>(
    cs: CS,
    value: Option<F>,
) -> Result<Vec<Boolean>, SynthesisError>
```