mbedtls::hash
# Function pbkdf2_hmac 
Source 

```
pub fn pbkdf2_hmac(
    md: Type,
    password: &[u8],
    salt: &[u8],
    iterations: u32,
    key: &mut [u8],
) -> Result<()>
```