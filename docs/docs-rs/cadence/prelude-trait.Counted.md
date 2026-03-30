cadence::prelude
# Trait Counted 
Source 

```
pub trait Counted<T>where
    T: ToCounterValue,{
    // Required method
    fn count_with_tags<'a>(
        &'a self,
        key: &'a str,
        count: T,
    ) -> MetricBuilder<'a, 'a, Counter>;

    // Provided method
    fn count(&self, key: &str, count: T) -> MetricResult<Counter> { ... }
}
```

## Required Methods§