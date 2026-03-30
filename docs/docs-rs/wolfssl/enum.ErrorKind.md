wolfssl
# Enum ErrorKind 
Source 

```
pub enum ErrorKind {
    CaCertNotAvailable,
    DomainNameMismatch,
    DuplicateMessage,
    PeerClosed,
    Other {
        what: String,
        code: c_int,
    },
}
```

## Variants§
§
### CaCertNotAvailable