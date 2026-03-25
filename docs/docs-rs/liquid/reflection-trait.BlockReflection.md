liquid::reflection
# Trait BlockReflection
Source 

```
pub trait BlockReflection {
    // Required methods
    fn start_tag(&self) -> &str;
    fn end_tag(&self) -> &str;
    fn description(&self) -> &str;

    // Provided methods
    fn example(&self) -> Option<&str> { ... }
    fn spec(&self) -> Option<&str> { ... }
}
```

## Required Methods§
Source
#### fn start_tag(&self) -> &str