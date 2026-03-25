wolfssl
# Enum NewSessionError 
Source 

```
pub enum NewSessionError {
    CreateFailed,
    SetupFailed(&'static str, Error),
}
```

## Variants§
§
### CreateFailed