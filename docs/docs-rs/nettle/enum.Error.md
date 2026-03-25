nettle
# Enum Error 
Source 

```
pub enum Error {
    InvalidArgument {
        argument_name: &'static str,
    },
    SigningFailed,
    EncryptionFailed,
    DecryptionFailed,
    KeyGenerationFailed,
    InvalidBitSizes,
    InconsistentCurves,
}
```

## Variants§
§
### InvalidArgument