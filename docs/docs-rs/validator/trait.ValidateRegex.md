validator
# Trait ValidateRegex 
Source 

```
pub trait ValidateRegex {
    // Required method
    fn validate_regex(&self, regex: impl AsRegex) -> bool;
}
```

## Required Methods§
Source
#### fn validate_regex(&self, regex: impl AsRegex) -> bool