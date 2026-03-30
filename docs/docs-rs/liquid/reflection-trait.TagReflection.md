liquid::reflection
# Trait TagReflection
Source 

```
pub trait TagReflection {
    // Required methods
    fn tag(&self) -> &str;
    fn description(&self) -> &str;

    // Provided methods
    fn example(&self) -> Option<&str> { ... }
    fn spec(&self) -> Option<&str> { ... }
}
```

## Required Methods§
Source
#### fn tag(&self) -> &str