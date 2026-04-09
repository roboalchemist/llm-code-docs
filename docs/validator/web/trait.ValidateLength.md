validator
# Trait ValidateLength 
Source 

```
pub trait ValidateLength<T>where
    T: PartialEq + PartialOrd,{
    // Required method
    fn length(&self) -> Option<T>;

    // Provided method
    fn validate_length(
        &self,
        min: Option<T>,
        max: Option<T>,
        equal: Option<T>,
    ) -> bool { ... }
}
```

## Required Methods§
Source
#### fn length(&self) -> Option<T>