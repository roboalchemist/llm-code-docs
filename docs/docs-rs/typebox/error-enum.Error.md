typebox::error
# Enum Error 
Source 

```
pub enum Error {
    Validation(ValidationError),
    Parse(ParseError),
    Json(Error),
    Io(Error),
    SchemaNotFound(String),
}
```

## Variants§
§
### Validation(ValidationError)