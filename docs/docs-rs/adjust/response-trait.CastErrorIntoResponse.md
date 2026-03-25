adjust::response
# Trait CastErrorIntoResponse 
Source 

```
pub trait CastErrorIntoResponse<T> {
    // Required method
    fn err_into_response(self) -> Result<T, HttpError>;
}
```

## Required Methods§
Source
#### fn err_into_response(self) -> Result<T, HttpError>