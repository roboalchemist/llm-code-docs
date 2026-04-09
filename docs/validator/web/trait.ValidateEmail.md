validator
# Trait ValidateEmail 
Source 

```
pub trait ValidateEmail {
    // Required method
    fn as_email_string(&self) -> Option<Cow<'_, str>>;

    // Provided method
    fn validate_email(&self) -> bool { ... }
}
```

## Required Methods§
Source
#### fn as_email_string(&self) -> Option<Cow<'_, str>>