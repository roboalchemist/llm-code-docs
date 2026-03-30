cadence
# Trait Timed 
Source 

```
pub trait Timed<T>where
    T: ToTimerValue,{
    // Required method
    fn time_with_tags<'a>(
        &'a self,
        key: &'a str,
        time: T,
    ) -> MetricBuilder<'a, 'a, Timer>;

    // Provided method
    fn time(&self, key: &str, time: T) -> MetricResult<Timer> { ... }
}
```

## Required Methods§