botan
# Function nist_kw_enc 
Source 

```
pub fn nist_kw_enc(
    cipher_algo: &str,
    padding: bool,
    kek: &[u8],
    key: &[u8],
) -> Result<Vec<u8>>
```