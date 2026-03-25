statiq::sproc
# Struct SprocResult 
Source 

```
pub struct SprocResult<T = ()> {
    pub success: bool,
    pub error_code: Option<String>,
    pub error_message: Option<String>,
    pub data: Option<T>,
}
```

## Fields§
§`success: bool`§`error_code: Option<String>`§`error_message: Option<String>`§`data: Option<T>`
## Implementations§