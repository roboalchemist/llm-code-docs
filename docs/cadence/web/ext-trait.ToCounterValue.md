cadence::ext
# Trait ToCounterValue 
Source 

```
pub trait ToCounterValue {
    // Required method
    fn try_to_value(self) -> MetricResult<MetricValue>;
}
```

## Required Methods§
Source
#### fn try_to_value(self) -> MetricResult<MetricValue>