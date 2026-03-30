cadence::ext
# Trait ToTimerValue 
Source 

```
pub trait ToTimerValue {
    // Required method
    fn try_to_value(self) -> MetricResult<MetricValue>;
}
```

## Required Methods§
Source
#### fn try_to_value(self) -> MetricResult<MetricValue>