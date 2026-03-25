cadence::prelude
# Trait Histogrammed 
Source 

```
pub trait Histogrammed<T>where
    T: ToHistogramValue,{
    // Required method
    fn histogram_with_tags<'a>(
        &'a self,
        key: &'a str,
        value: T,
    ) -> MetricBuilder<'a, 'a, Histogram>;

    // Provided method
    fn histogram(&self, key: &str, value: T) -> MetricResult<Histogram> { ... }
}
```

## Required Methods§