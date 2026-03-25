pgp::composed
# Enum PublicOrSecret 
Source 

```
pub enum PublicOrSecret {
    Public(SignedPublicKey),
    Secret(SignedSecretKey),
}
```

## Variants§
§
### Public(SignedPublicKey)