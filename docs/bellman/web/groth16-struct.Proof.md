bellman::groth16
# Struct Proof 
Source 

```
pub struct Proof<E: Engine> {
    pub a: E::G1Affine,
    pub b: E::G2Affine,
    pub c: E::G1Affine,
}
```

## Fields§
§`a: E::G1Affine`§`b: E::G2Affine`§`c: E::G1Affine`
## Implementations§