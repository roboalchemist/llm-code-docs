perf::ffi
# Struct perf_record_comm 
Source 

```
#[repr(C)]pub struct perf_record_comm {
    pub header: perf_event_header,
    pub pid: u32,
    pub tid: u32,
    pub comm: [u8; 16],
}
```

## Fields§
§`header: perf_event_header`§`pid: u32`§`tid: u32`§`comm: [u8; 16]`
## Trait Implementations§