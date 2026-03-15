bellman::groth16
# Struct PreparedVerifyingKey 
Source 

```
pub struct PreparedVerifyingKey<E: MultiMillerLoop> { /* private fields */ }
```

## Auto Trait Implementations§
§
### impl<E> Freeze for PreparedVerifyingKey<E>where
    <E as Engine>::Gt: Freeze,
    <E as MultiMillerLoop>::G2Prepared: Freeze,