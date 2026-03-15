bellman::groth16
# Struct VerifyingKey 
Source 

```
pub struct VerifyingKey<E: Engine> {
    pub alpha_g1: E::G1Affine,
    pub beta_g1: E::G1Affine,
    pub beta_g2: E::G2Affine,
    pub gamma_g2: E::G2Affine,
    pub delta_g1: E::G1Affine,
    pub delta_g2: E::G2Affine,
    pub ic: Vec<E::G1Affine>,
}
```

## Fields§
§`alpha_g1: E::G1Affine`§`beta_g1: E::G1Affine`§`beta_g2: E::G2Affine`§`gamma_g2: E::G2Affine`§`delta_g1: E::G1Affine`§`delta_g2: E::G2Affine`§`ic: Vec<E::G1Affine>`
## Implementations§