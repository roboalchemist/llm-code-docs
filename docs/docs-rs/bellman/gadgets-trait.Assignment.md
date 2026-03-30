bellman::gadgets
# Trait Assignment 
Source 

```
pub trait Assignment<T> {
    // Required method
    fn get(&self) -> Result<&T, SynthesisError>;
}
```

## Required Methods§
Source
#### fn get(&self) -> Result<&T, SynthesisError>