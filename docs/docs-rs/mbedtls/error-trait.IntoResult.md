mbedtls::error
# Trait IntoResult 
Source 

```
pub trait IntoResult: Sized {
    // Required method
    fn into_result(self) -> Result<Self>;

    // Provided method
    fn into_result_discard(self) -> Result<()> { ... }
}
```

## Required Methods§
Source
#### fn into_result(self) -> Result<Self>