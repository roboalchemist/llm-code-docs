mbedtls::cipher
# Trait Operation 
Source 

```
pub trait Operation: Sized {
    // Required method
    fn is_encrypt() -> bool;
}
```

## Required Methods§
Source
#### fn is_encrypt() -> bool