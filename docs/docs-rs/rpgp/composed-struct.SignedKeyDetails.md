pgp::composed
# Struct SignedKeyDetails 
Source 

```
pub struct SignedKeyDetails {
    pub revocation_signatures: Vec<Signature>,
    pub direct_signatures: Vec<Signature>,
    pub users: Vec<SignedUser>,
    pub user_attributes: Vec<SignedUserAttribute>,
}
```

## Fields§
§`revocation_signatures: Vec<Signature>`§`direct_signatures: Vec<Signature>`§`users: Vec<SignedUser>`§`user_attributes: Vec<SignedUserAttribute>`
## Implementations§