mbedtls::hash
# Function pbkdf_pkcs12 
Source 

```
pub fn pbkdf_pkcs12(
    md: Type,
    password: &[u8],
    salt: &[u8],
    id: u8,
    iterations: u32,
    key: &mut [u8],
) -> Result<()>
```