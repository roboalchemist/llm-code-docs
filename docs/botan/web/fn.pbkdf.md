botan
# Function pbkdf 
Source 

```
pub fn pbkdf(
    algo: &str,
    out_len: usize,
    passphrase: &str,
    salt: &[u8],
    iterations: usize,
) -> Result<Vec<u8>>
```