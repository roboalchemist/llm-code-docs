pacman::ini
# Enum Error 
Source 

```
pub enum Error {
    Io(Error),
    Parse(ParseError),
}
```

## Variants§
§
### Io(Error)