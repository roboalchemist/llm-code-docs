carton::error
# Type Alias Result 
Source 

```
pub type Result<T> = Result<T, CartonError>;
```

## Aliased Type§

```
pub enum Result<T> {
    Ok(T),
    Err(CartonError),
}
```

## Variants§
§1.0.0
### Ok(T)