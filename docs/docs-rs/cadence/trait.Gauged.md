cadence
# Trait Gauged 
Source 

```
pub trait Gauged<T>where
    T: ToGaugeValue,{
    // Required method
    fn gauge_with_tags<'a>(
        &'a self,
        key: &'a str,
        value: T,
    ) -> MetricBuilder<'a, 'a, Gauge>;

    // Provided method
    fn gauge(&self, key: &str, value: T) -> MetricResult<Gauge> { ... }
}
```

## Required Methods§