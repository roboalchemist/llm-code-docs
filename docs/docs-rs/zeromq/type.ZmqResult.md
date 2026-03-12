zeromq
# Type Alias ZmqResult 
Source 

```
pub type ZmqResult<T> = Result<T, ZmqError>;
```

## Aliased Type§

```
pub enum ZmqResult<T> {
    Ok(T),
    Err(ZmqError),
}
```

## Variants§
§1.0.0
### Ok(T)