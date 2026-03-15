bellman::groth16
# Function create_proof 
Source 

```
pub fn create_proof<E, C, P: ParameterSource<E>>(
    circuit: C,
    params: P,
    r: E::Fr,
    s: E::Fr,
) -> Result<Proof<E>, SynthesisError>where
    E: Engine,
    E::Fr: PrimeFieldBits,
    C: Circuit<E::Fr>,
```