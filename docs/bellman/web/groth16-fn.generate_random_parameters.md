bellman::groth16
# Function generate_random_parameters 
Source 

```
pub fn generate_random_parameters<E, C, R>(
    circuit: C,
    rng: &mut R,
) -> Result<Parameters<E>, SynthesisError>where
    E: Engine,
    E::G1: WnafGroup,
    E::G2: WnafGroup,
    C: Circuit<E::Fr>,
    R: RngCore,
```