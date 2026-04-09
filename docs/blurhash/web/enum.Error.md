blurhash
# Enum Error 
Source 

```
pub enum Error {
    HashTooShort,
    LengthMismatch {
        expected: usize,
        actual: usize,
    },
    InvalidAscii,
    InvalidBase83(u8),
    ComponentsOutOfRange,
}
```

## Variants§
§
### HashTooShort