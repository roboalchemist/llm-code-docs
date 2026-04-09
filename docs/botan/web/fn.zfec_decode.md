botan
# Function zfec_decode 
Source 

```
pub fn zfec_decode(
    k: usize,
    n: usize,
    shares: &[(usize, &[u8])],
    share_size: usize,
) -> Result<Vec<u8>>
```