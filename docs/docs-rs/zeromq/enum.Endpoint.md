zeromq
# Enum Endpoint 
Source 

```
#[non_exhaustive]pub enum Endpoint {
    Tcp(Host, u16),
    Ipc(Option<PathBuf>),
}
```

## Variants (Non-exhaustive)§
§
### Tcp(Host, u16)