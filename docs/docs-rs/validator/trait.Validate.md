validator
# Trait Validate 
Source 

```
pub trait Validate {
    // Required method
    fn validate(&self) -> Result<(), ValidationErrors>;
}
```

## Required Methods§
Source
#### fn validate(&self) -> Result<(), ValidationErrors>