pgp::composed
# Enum SymEncryptedDataReader 
Source 

```
pub enum SymEncryptedDataReader<R: BufRead> {
    Body {
        decryptor: MaybeDecryptor<PacketBodyReader<R>>,
    },
    Error,
}
```

## Variants§
§
### Body