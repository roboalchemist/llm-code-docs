perf::ffi
# Struct perf_record_lost 
Source 

```
#[repr(C)]pub struct perf_record_lost {
    pub header: perf_event_header,
    pub id: u64,
    pub lost: u64,
}
```

## Fields§
§`header: perf_event_header`§`id: u64`§`lost: u64`
## Trait Implementations§