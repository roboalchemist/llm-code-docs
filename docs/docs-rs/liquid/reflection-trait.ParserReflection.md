liquid::reflection
# Trait ParserReflection
Source 

```
pub trait ParserReflection {
    // Required methods
    fn blocks(&self) -> Box<dyn Iterator<Item = &dyn BlockReflection> + '_>;
    fn tags(&self) -> Box<dyn Iterator<Item = &dyn TagReflection> + '_>;
    fn filters(&self) -> Box<dyn Iterator<Item = &dyn FilterReflection> + '_>;
    fn partials(&self) -> Box<dyn Iterator<Item = &str> + '_>;
}
```

## Required Methods§
Source
#### fn blocks(&self) -> Box<dyn Iterator<Item = &dyn BlockReflection> + '_>