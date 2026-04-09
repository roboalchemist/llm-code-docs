pgp::composed
# Enum KeyType 
Source 

```
pub enum KeyType {
    Rsa(u32),
    ECDH(ECCCurve),
    Ed25519Legacy,
    ECDSA(ECCCurve),
    Dsa(DsaKeySize),
    Ed25519,
    Ed448,
    X25519,
    X448,
}
```

## Variants§
§
### Rsa(u32)