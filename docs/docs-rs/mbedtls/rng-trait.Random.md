mbedtls::rng
# Trait Random 
Source 

```
pub trait Random: RngCallback {
    // Provided method
    fn random(&mut self, data: &mut [u8]) -> Result<()>
       where Self: Sized { ... }
}
```

## Provided Methods§
Source
#### fn random(&mut self, data: &mut [u8]) -> Result<()>where
    Self: Sized,