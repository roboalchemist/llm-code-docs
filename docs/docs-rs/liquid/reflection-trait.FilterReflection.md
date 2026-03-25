liquid::reflection
# Trait FilterReflection
Source 

```
pub trait FilterReflection {
    // Required methods
    fn name(&self) -> &str;
    fn description(&self) -> &str;
    fn positional_parameters(&self) -> &'static [ParameterReflection];
    fn keyword_parameters(&self) -> &'static [ParameterReflection];
}
```

## Required Methods§
Source
#### fn name(&self) -> &str