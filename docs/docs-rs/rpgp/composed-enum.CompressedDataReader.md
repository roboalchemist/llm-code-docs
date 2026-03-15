pgp::composed
# Enum CompressedDataReader 
Source 

```
pub enum CompressedDataReader<R: DebugBufRead> {
    Body {
        source: MaybeDecompress<PacketBodyReader<R>>,
        buffer: BytesMut,
    },
    Done {
        source: PacketBodyReader<R>,
    },
    Error,
}
```

## Variants§
§
### Body