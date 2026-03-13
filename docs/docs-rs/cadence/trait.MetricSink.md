cadence
# Trait MetricSink 
Source 

```
pub trait MetricSink {
    // Required method
    fn emit(&self, metric: &str) -> Result<usize>;

    // Provided methods
    fn flush(&self) -> Result<()> { ... }
    fn stats(&self) -> SinkStats { ... }
}
```

## Required Methods§