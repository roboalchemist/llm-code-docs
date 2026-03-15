bellman::groth16
# Function create_random_proof 
Source 

```
pub fn create_random_proof<E, C, R, P: ParameterSource<E>>(
    circuit: C,
    params: P,
    rng: &mut R,
) -> Result<Proof<E>, SynthesisError>where
    E: Engine,
    E::Fr: PrimeFieldBits,
    C: Circuit<E::Fr>,
    R: RngCore,
```