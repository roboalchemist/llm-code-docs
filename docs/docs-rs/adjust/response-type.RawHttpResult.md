adjust::response
# Type Alias RawHttpResult 
Source 

```
pub type RawHttpResult<T> = Result<T, HttpError>;
```

## Aliased Type§

```
pub enum RawHttpResult<T> {
    Ok(T),
    Err(HttpError),
}
```

## Variants§
§1.0.0
### Ok(T)