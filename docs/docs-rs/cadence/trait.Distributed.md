cadence
# Trait Distributed 
Source 

```
pub trait Distributed<T>where
    T: ToDistributionValue,{
    // Required method
    fn distribution_with_tags<'a>(
        &'a self,
        key: &'a str,
        value: T,
    ) -> MetricBuilder<'a, 'a, Distribution>;

    // Provided method
    fn distribution(&self, key: &str, value: T) -> MetricResult<Distribution> { ... }
}
```

## Required Methods§