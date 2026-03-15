env_logger::fmt
# Enum Target 
Source 

```
#[non_exhaustive]pub enum Target {
    Stdout,
    Stderr,
    Pipe(Box<dyn Write + Send + 'static>),
}
```

## Variants (Non-exhaustive)§
§
### Stdout