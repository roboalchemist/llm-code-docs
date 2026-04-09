validator
# Trait ValidateRange 
Source 

```
pub trait ValidateRange<T> {
    // Required methods
    fn greater_than(&self, max: T) -> Option<bool>;
    fn less_than(&self, min: T) -> Option<bool>;

    // Provided method
    fn validate_range(
        &self,
        min: Option<T>,
        max: Option<T>,
        exclusive_min: Option<T>,
        exclusive_max: Option<T>,
    ) -> bool { ... }
}
```

## Required Methods§
Source
#### fn greater_than(&self, max: T) -> Option<bool>