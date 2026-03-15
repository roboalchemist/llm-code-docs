pgp::composed
# Enum LiteralDataReader 
Source 

```
pub enum LiteralDataReader<R: BufRead> {
    Body {
        header: LiteralDataHeader,
        source: PacketBodyReader<R>,
        buffer: BytesMut,
    },
    Done {
        header: LiteralDataHeader,
        source: PacketBodyReader<R>,
        buffer: BytesMut,
    },
    Error,
}
```

## Variants§
§
### Body