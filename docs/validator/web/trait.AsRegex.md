validator
# Trait AsRegex 
Source 

```
pub trait AsRegex {
    // Required method
    fn as_regex(&self) -> Cow<'_, Regex>;
}
```

## Required Methods§
Source
#### fn as_regex(&self) -> Cow<'_, Regex>