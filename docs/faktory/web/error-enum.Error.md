faktory::error
# Enum Error 
Source 

```
#[non_exhaustive]pub enum Error {
    Connect(Connect),
    IO(Error),
    Protocol(Protocol),
    Serialization(Error),
    Stream(Stream),
}
```

## Variants (Non-exhaustive)§
§
### Connect(Connect)