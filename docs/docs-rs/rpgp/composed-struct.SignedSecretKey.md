pgp::composed
# Struct SignedSecretKey 
Source 

```
pub struct SignedSecretKey {
    pub primary_key: SecretKey,
    pub details: SignedKeyDetails,
    pub public_subkeys: Vec<SignedPublicSubKey>,
    pub secret_subkeys: Vec<SignedSecretSubKey>,
}
```

## Fields§
§`primary_key: SecretKey`§`details: SignedKeyDetails`§`public_subkeys: Vec<SignedPublicSubKey>`§`secret_subkeys: Vec<SignedSecretSubKey>`
## Implementations§