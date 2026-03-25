perf::map
# Enum Event 
Source 

```
pub enum Event<'e, T> {
    Event(&'e T),
    Lost(&'e perf_record_lost),
    Comm(&'e perf_record_comm),
    Other(&'e perf_record_sample),
}
```

## Variants§
§
### Event(&'e T)