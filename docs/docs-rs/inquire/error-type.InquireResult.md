inquire::error
# Type Alias InquireResult 
Source 

```
pub type InquireResult<T> = Result<T, InquireError>;
```

## Aliased Type§

```
pub enum InquireResult<T> {
    Ok(T),
    Err(InquireError),
}
```

## Variants§
§1.0.0
### Ok(T)