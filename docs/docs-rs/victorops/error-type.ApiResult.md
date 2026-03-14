victorops::error
# Type Alias ApiResult 
Source 

```
pub type ApiResult<T> = Result<T, Error>;
```

## Aliased Type§

```
pub enum ApiResult<T> {
    Ok(T),
    Err(Error),
}
```

## Variants§
§1.0.0
### Ok(T)