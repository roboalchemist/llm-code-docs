cadence::ext
# Trait ToHistogramValue 
Source 

```
pub trait ToHistogramValue {
    // Required method
    fn try_to_value(self) -> MetricResult<MetricValue>;
}
```

## Required Methods§
Source
#### fn try_to_value(self) -> MetricResult<MetricValue>