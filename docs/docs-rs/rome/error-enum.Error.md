rome::error
# Enum Error 
Source 

```
pub enum Error {
    IOError(Error),
    NomError(String),
    Custom(&'static str),
    String(String),
}
```

## Variants§
§
### IOError(Error)