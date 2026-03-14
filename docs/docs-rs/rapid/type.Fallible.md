rapid
# Type Alias Fallible 
Source 

```
pub type Fallible<T> = Result<T, Error>;
```

## Aliased Type§

```
pub enum Fallible<T> {
    Ok(T),
    Err(Error),
}
```

## Variants§
§1.0.0
### Ok(T)