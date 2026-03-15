pgp::composed
# Struct TheRing 
Source 

```
pub struct TheRing<'a> {
    pub secret_keys: Vec<&'a SignedSecretKey>,
    pub key_passwords: Vec<&'a Password>,
    pub message_password: Vec<&'a Password>,
    pub session_keys: Vec<PlainSessionKey>,
    pub decrypt_options: DecryptionOptions,
}
```

## Fields§
§`secret_keys: Vec<&'a SignedSecretKey>`§`key_passwords: Vec<&'a Password>`§`message_password: Vec<&'a Password>`§`session_keys: Vec<PlainSessionKey>`§`decrypt_options: DecryptionOptions`
## Trait Implementations§