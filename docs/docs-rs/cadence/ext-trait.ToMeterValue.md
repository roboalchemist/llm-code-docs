cadence::ext
# Trait ToMeterValue 
Source 

```
pub trait ToMeterValue {
    // Required method
    fn try_to_value(self) -> MetricResult<MetricValue>;
}
```

## Required Methods§
Source
#### fn try_to_value(self) -> MetricResult<MetricValue>