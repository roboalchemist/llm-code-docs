taos
# Type Alias RawResult 
Source 

```
pub type RawResult<T> = Result<T, Error>;
```

## Aliased Type§

```
pub enum RawResult<T> {
    Ok(T),
    Err(Error),
}
```

## Variants§
§1.0.0
### Ok(T)