mbedtls::cipher
# Trait Type 
Source 

```
pub trait Type {
    // Required method
    fn is_valid_mode(mode: CipherMode) -> bool;
}
```

## Required Methods§
Source
#### fn is_valid_mode(mode: CipherMode) -> bool