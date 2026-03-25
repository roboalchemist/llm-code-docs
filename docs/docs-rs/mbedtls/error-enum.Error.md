mbedtls::error
# Enum Error 
Source 

```
pub enum Error {
    HighLevel(HiError),
    LowLevel(LoError),
    HighAndLowLevel(HiError, LoError),
    Other(c_int),
    Utf8Error(Option<Utf8Error>),
}
```

## Variants§
§
### HighLevel(HiError)