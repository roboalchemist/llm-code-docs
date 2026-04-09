nettle::aead
# Struct Ocb 
Source 

```
pub struct Ocb<C, T>where
    C: Cipher + BlockSizeIs16,
    T: Unsigned + IsLessOrEqual<U16, Output = True>,{ /* private fields */ }
```

## Implementations§