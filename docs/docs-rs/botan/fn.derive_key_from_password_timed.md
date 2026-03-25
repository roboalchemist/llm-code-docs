botan
# Function derive_key_from_password_timed 
Source 

```
pub fn derive_key_from_password_timed(
    algo: &str,
    out_len: usize,
    passphrase: &str,
    salt: &[u8],
    msec: u32,
) -> Result<(Vec<u8>, usize, usize, usize)>
```