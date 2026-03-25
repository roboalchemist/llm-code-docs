cadence::ext
# Trait MetricBackend 
Source 

```
pub trait MetricBackend: Sealed {
    // Required methods
    fn send_metric<M>(&self, metric: &M) -> MetricResult<()>
       where M: Metric;
    fn consume_error(&self, err: MetricError);
}
```

## Required Methods§