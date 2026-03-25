wundergraph::error
# Type Alias Result 
Source 

```
pub type Result<T> = Result<T, WundergraphError>;
```

## Aliased Type§

```
pub enum Result<T> {
    Ok(T),
    Err(WundergraphError),
}
```

## Variants§
§1.0.0
### Ok(T)