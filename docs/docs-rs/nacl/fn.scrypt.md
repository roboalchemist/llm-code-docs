nacl
# Function scrypt 
Source 

```
pub fn scrypt(
    passwd: &[u8],
    salt: &[u8],
    logN: u8,
    r: usize,
    p: usize,
    dk_len: usize,
    progress_cb: &dyn Fn(u32),
) -> Result<Vec<u8>, Error>
```