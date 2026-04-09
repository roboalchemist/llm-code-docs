botan
# Function bcrypt_hash 
Source 

```
pub fn bcrypt_hash(
    pass: &str,
    rng: &mut RandomNumberGenerator,
    workfactor: usize,
) -> Result<String>
```