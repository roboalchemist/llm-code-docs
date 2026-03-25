cadence::ext
# Trait ToSetValue 
Source 

```
pub trait ToSetValue {
    // Required method
    fn try_to_value(self) -> MetricResult<MetricValue>;
}
```

## Required Methods§
Source
#### fn try_to_value(self) -> MetricResult<MetricValue>