cross
# Trait OutputExt 
Source 

```
pub trait OutputExt {
    // Required methods
    fn stdout(&self) -> Result<String, CommandError>;
    fn stderr(&self) -> Result<String, CommandError>;
}
```

## Required Methods§
Source
#### fn stdout(&self) -> Result<String, CommandError>