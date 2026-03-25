botan
# Function nist_kw_dec 
Source 

```
pub fn nist_kw_dec(
    cipher_algo: &str,
    padding: bool,
    kek: &[u8],
    wrapped: &[u8],
) -> Result<Vec<u8>>
```