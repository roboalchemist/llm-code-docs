typebox::error
# Enum PatchError 
Source 

```
pub enum PatchError {
    InvalidPath(String),
    TypeMismatch {
        path: String,
        message: String,
    },
}
```

## Variants§
§
### InvalidPath(String)