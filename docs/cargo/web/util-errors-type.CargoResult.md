cargo::util::errors

# Type Alias CargoResult

Source

```
pub type CargoResult<T> = Result<T>;
```

## Aliased Type§

```
pub enum CargoResult<T> {
    Ok(T),
    Err(Error),
}
```

## Variants§

§1.0.0

### Ok(T)
