lopdf
# Enum Encoding 
Source 

```
pub enum Encoding<'a> {
    OneByteEncoding(&'a [Option<u16>; 256]),
    SimpleEncoding(&'a [u8]),
    UnicodeMapEncoding(ToUnicodeCMap),
}
```

## Variants§
§
### OneByteEncoding(&'a [Option<u16>; 256])