argon2
# Type Alias Result 
Source 

```
pub type Result<T> = Result<T, Error>;
```

## Aliased Type§

```
pub enum Result<T> {
    Ok(T),
    Err(Error),
}
```

## Variants§
§1.0.0
### Ok(T)