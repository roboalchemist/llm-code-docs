pgp::composed
# Function decrypt_session_key_with_password 
Source 

```
pub fn decrypt_session_key_with_password(
    packet: &SymKeyEncryptedSessionKey,
    msg_pw: &Password,
) -> Result<PlainSessionKey>
```