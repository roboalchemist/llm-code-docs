pgp::composed
# Enum Any 
Source 

```
pub enum Any<'a> {
    Cleartext(CleartextSignedMessage),
    PublicKey(SignedPublicKey),
    SecretKey(SignedSecretKey),
    Message(Message<'a>),
    Signature(DetachedSignature),
}
```

## Variants§
§
### Cleartext(CleartextSignedMessage)