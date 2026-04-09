typebox::error
# Enum RegistryError 
Source 

```
pub enum RegistryError {
    SchemaNotFound(String),
    CircularRef(String),
}
```

## Variants§
§
### SchemaNotFound(String)