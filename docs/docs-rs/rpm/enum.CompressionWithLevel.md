rpm
# Enum CompressionWithLevel 
Source 

```
pub enum CompressionWithLevel {
    None,
    Zstd(i32),
    Gzip(u32),
    Xz(u32),
    Bzip2(u32),
}
```

## Variants§
§
### None