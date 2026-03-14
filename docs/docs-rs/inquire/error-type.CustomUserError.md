inquire::error
# Type Alias CustomUserError 
Source 

```
pub type CustomUserError = Box<dyn Error + Send + Sync + 'static>;
```

## Aliased Type§

```
pub struct CustomUserError(/* private fields */);
```