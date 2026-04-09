pgp::composed
# Enum PlainSessionKey 
Source 

```
pub enum PlainSessionKey {
    V3_4 {
        sym_alg: SymmetricKeyAlgorithm,
        key: RawSessionKey,
    },
    V5 {
        key: RawSessionKey,
    },
    V6 {
        key: RawSessionKey,
    },
}
```

## Variants§
§
### V3_4