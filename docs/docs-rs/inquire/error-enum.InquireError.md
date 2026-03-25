inquire::error
# Enum InquireError 
Source 

```
pub enum InquireError {
    NotTTY,
    InvalidConfiguration(String),
    IO(Error),
    OperationCanceled,
    OperationInterrupted,
    Custom(CustomUserError),
}
```

## Variants§
§
### NotTTY