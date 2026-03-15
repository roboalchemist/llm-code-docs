wolfssl
# Enum IOCallbackResult 
Source 

```
pub enum IOCallbackResult<T> {
    Ok(T),
    WouldBlock,
    Err(Error),
}
```

## Variants§
§
### Ok(T)