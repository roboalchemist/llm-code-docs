nix

# Type Alias Result

Source

```
pub type Result<T> = Result<T, Errno>;
```

Available on **Unix** only.

## Aliased Type§

```
pub enum Result<T> {
    Ok(T),
    Err(Errno),
}
```

## Variants§

§1.0.0

### Ok(T)
