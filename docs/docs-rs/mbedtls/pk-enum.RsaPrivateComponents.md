mbedtls::pk
# Enum RsaPrivateComponents 
Source 

```
pub enum RsaPrivateComponents<'a> {
    WithPrimes {
        p: &'a Mpi,
        q: &'a Mpi,
        e: &'a Mpi,
    },
    WithPrivateExponent {
        n: &'a Mpi,
        d: &'a Mpi,
        e: &'a Mpi,
    },
}
```

## Variants§
§
### WithPrimes