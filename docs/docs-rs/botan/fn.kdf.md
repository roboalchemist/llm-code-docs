botan
# Function kdf 
Source 

```
pub fn kdf(
    algo: &str,
    output_len: usize,
    secret: &[u8],
    salt: &[u8],
    label: &[u8],
) -> Result<Vec<u8>>
```