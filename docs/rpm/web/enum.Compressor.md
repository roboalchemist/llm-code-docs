rpm
# Enum Compressor 
Source 

```
pub enum Compressor {
    None(Vec<u8>),
    Gzip(GzEncoder<Vec<u8>>),
    Zstd(Encoder<'static, Vec<u8>>),
    Xz(XzEncoder<Vec<u8>>),
}
```

## Variants§
§
### None(Vec<u8>)