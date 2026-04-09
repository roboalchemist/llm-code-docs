cadence::ext
# Trait ToDistributionValue 
Source 

```
pub trait ToDistributionValue {
    // Required method
    fn try_to_value(self) -> MetricResult<MetricValue>;
}
```

## Required Methods§
Source
#### fn try_to_value(self) -> MetricResult<MetricValue>