pgp::composed
# Enum MessageReader 
Source 

```
pub enum MessageReader<'a> {
    Compressed(Box<CompressedDataReader<MessageReader<'a>>>),
    Edata(Box<Edata<'a>>),
    Reader(Box<dyn DebugBufRead + 'a>),
}
```

## Variants§
§
### Compressed(Box<CompressedDataReader<MessageReader<'a>>>)