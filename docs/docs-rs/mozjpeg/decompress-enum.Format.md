mozjpeg::decompress
# Enum Format 
Source 

```
pub enum Format<R> {
    RGB(DecompressStarted<R>),
    Gray(DecompressStarted<R>),
    CMYK(DecompressStarted<R>),
}
```

## Variants§
§
### RGB(DecompressStarted<R>)