perf::ffi
# Struct perf_record_sample 
Source 

```
#[repr(C)]pub struct perf_record_sample {
    pub header: perf_event_header,
    pub size: u32,
    pub data: [u8; 0],
}
```

## Fields§
§`header: perf_event_header`§`size: u32`§`data: [u8; 0]`
## Trait Implementations§