cadence::ext
# Trait ToGaugeValue 
Source 

```
pub trait ToGaugeValue {
    // Required method
    fn try_to_value(self) -> MetricResult<MetricValue>;
}
```

## Required Methods§
Source
#### fn try_to_value(self) -> MetricResult<MetricValue>