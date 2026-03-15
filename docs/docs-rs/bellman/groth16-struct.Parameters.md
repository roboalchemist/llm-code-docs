bellman::groth16
# Struct Parameters 
Source 

```
pub struct Parameters<E: Engine> {
    pub vk: VerifyingKey<E>,
    pub h: Arc<Vec<E::G1Affine>>,
    pub l: Arc<Vec<E::G1Affine>>,
    pub a: Arc<Vec<E::G1Affine>>,
    pub b_g1: Arc<Vec<E::G1Affine>>,
    pub b_g2: Arc<Vec<E::G2Affine>>,
}
```

## Fields§
§`vk: VerifyingKey<E>`§`h: Arc<Vec<E::G1Affine>>`§`l: Arc<Vec<E::G1Affine>>`§`a: Arc<Vec<E::G1Affine>>`§`b_g1: Arc<Vec<E::G1Affine>>`§`b_g2: Arc<Vec<E::G2Affine>>`
## Implementations§