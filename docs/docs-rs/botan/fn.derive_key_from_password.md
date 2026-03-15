botan
# Function derive_key_from_password 
Source 

```
pub fn derive_key_from_password(
    algo: &str,
    out_len: usize,
    passphrase: &str,
    salt: &[u8],
    param1: usize,
    param2: usize,
    param3: usize,
) -> Result<Vec<u8>>
```