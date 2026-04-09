cross
# Type Alias Result 
Source 

```
pub type Result<T, E = Report> = Result<T, E>;
```

## Aliased Type§

```
pub enum Result<T, E = Report> {
    Ok(T),
    Err(E),
}
```

## Variants§
§1.0.0
### Ok(T)