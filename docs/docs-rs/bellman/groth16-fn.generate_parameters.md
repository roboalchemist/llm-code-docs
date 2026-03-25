bellman::groth16
# Function generate_parameters 
Source 

```
pub fn generate_parameters<E, C>(
    circuit: C,
    g1: E::G1,
    g2: E::G2,
    alpha: E::Fr,
    beta: E::Fr,
    gamma: E::Fr,
    delta: E::Fr,
    tau: E::Fr,
) -> Result<Parameters<E>, SynthesisError>where
    E: Engine,
    E::G1: WnafGroup,
    E::G2: WnafGroup,
    C: Circuit<E::Fr>,
```