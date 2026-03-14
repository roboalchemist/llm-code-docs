validator
# Trait ValidateRequired 
Source 

```
pub trait ValidateRequired {
    // Required method
    fn is_some(&self) -> bool;

    // Provided method
    fn validate_required(&self) -> bool { ... }
}
```

## Required Methods§
Source
#### fn is_some(&self) -> bool