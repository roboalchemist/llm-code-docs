inquire::validator
# Trait CustomTypeValidator 
Source 

```
pub trait CustomTypeValidator<T: ?Sized>: DynClone {
    // Required method
    fn validate(&self, input: &T) -> Result<Validation, CustomUserError>;
}
```

## Required Methods§