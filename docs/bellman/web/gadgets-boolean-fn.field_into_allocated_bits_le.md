bellman::gadgets::boolean
# Function field_into_allocated_bits_le 
Source 

```
pub fn field_into_allocated_bits_le<Scalar: PrimeField, CS: ConstraintSystem<Scalar>, F: PrimeFieldBits>(
    cs: CS,
    value: Option<F>,
) -> Result<Vec<AllocatedBit>, SynthesisError>
```