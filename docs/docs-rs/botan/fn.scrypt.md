botan
# Function scrypt 
Source 

```
pub fn scrypt(
    out_len: usize,
    passphrase: &str,
    salt: &[u8],
    n: usize,
    r: usize,
    p: usize,
) -> Result<Vec<u8>>
```