cadence::prelude
# Trait Setted 
Source 

```
pub trait Setted<T>where
    T: ToSetValue,{
    // Required method
    fn set_with_tags<'a>(
        &'a self,
        key: &'a str,
        value: T,
    ) -> MetricBuilder<'a, 'a, Set>;

    // Provided method
    fn set(&self, key: &str, value: T) -> MetricResult<Set> { ... }
}
```

## Required Methods§