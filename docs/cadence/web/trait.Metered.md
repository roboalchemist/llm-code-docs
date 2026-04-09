cadence
# Trait Metered 
Source 

```
pub trait Metered<T>where
    T: ToMeterValue,{
    // Required method
    fn meter_with_tags<'a>(
        &'a self,
        key: &'a str,
        value: T,
    ) -> MetricBuilder<'a, 'a, Meter>;

    // Provided method
    fn meter(&self, key: &str, value: T) -> MetricResult<Meter> { ... }
}
```

## Required Methods§