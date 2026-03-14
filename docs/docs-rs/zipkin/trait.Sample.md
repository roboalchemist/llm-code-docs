zipkin
# Trait Sample 
Source 

```
pub trait Sample {
    // Required method
    fn sample(&self, trace_id: TraceId) -> bool;
}
```

## Required Methods§