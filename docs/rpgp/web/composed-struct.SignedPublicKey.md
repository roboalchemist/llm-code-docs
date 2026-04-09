pgp::composed
# Struct SignedPublicKey 
Source 

```
pub struct SignedPublicKey {
    pub primary_key: PublicKey,
    pub details: SignedKeyDetails,
    pub public_subkeys: Vec<SignedPublicSubKey>,
}
```

## Fields§
§`primary_key: PublicKey`§`details: SignedKeyDetails`§`public_subkeys: Vec<SignedPublicSubKey>`
## Implementations§