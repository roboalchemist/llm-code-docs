wundergraph::error
# Enum WundergraphError 
Source 

```
pub enum WundergraphError {
    CouldNotBuildFilterArgument,
    UnknownDatabaseField {
        name: String,
    },
    NoPrimaryKeyArgumentFound,
    JuniperError {
        inner: FieldError<WundergraphScalarValue>,
    },
    DieselError {
        inner: Error,
    },
}
```

## Variants§
§
### CouldNotBuildFilterArgument