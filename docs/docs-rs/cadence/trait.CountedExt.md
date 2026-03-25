cadence
# Trait CountedExt 
Source 

```
pub trait CountedExt: Counted<i64> {
    // Provided methods
    fn incr(&self, key: &str) -> MetricResult<Counter> { ... }
    fn incr_with_tags<'a>(
        &'a self,
        key: &'a str,
    ) -> MetricBuilder<'a, 'a, Counter> { ... }
    fn decr(&self, key: &str) -> MetricResult<Counter> { ... }
    fn decr_with_tags<'a>(
        &'a self,
        key: &'a str,
    ) -> MetricBuilder<'a, 'a, Counter> { ... }
}
```

## Provided Methods§