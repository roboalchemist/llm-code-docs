verify::schemars::errors
# Enum InvalidSchema 
Source 

```
pub enum InvalidSchema {
    MissingDefinition(String),
    InvalidPattern {
        pattern: String,
        error: Error,
    },
    ExternalReference(String),
}
```
Available on **crate feature `schemars`** only.
## Variants§
§
### MissingDefinition(String)