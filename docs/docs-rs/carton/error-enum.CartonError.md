carton::error
# Enum CartonError 
Source 

```
#[non_exhaustive]pub enum CartonError {
    UnsupportedFileSystem(&'static str),
    InvalidDeviceFormat(String),
    UnknownDataType(String),
    UnexpectedInternalError(&'static str),
    FetchError(Error),
    IOError(Error),
    ConfigParsingError(Error),
    ErrorFromRunner(String),
    SemverParseError(Error),
    Other(&'static str),
}
```

## Variants (Non-exhaustive)§
§
### UnsupportedFileSystem(&'static str)