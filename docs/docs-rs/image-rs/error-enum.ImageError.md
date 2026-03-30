image::error
# Enum ImageError 
Source 

```
pub enum ImageError {
    Decoding(DecodingError),
    Encoding(EncodingError),
    Parameter(ParameterError),
    Limits(LimitError),
    Unsupported(UnsupportedError),
    IoError(Error),
}
```

## Variants§
§
### Decoding(DecodingError)