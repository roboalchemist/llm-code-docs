validator
# Trait ValidateUrl 
Source 

```
pub trait ValidateUrl {
    // Required method
    fn as_url_string(&self) -> Option<Cow<'_, str>>;

    // Provided method
    fn validate_url(&self) -> bool { ... }
}
```

## Required Methods§
Source
#### fn as_url_string(&self) -> Option<Cow<'_, str>>