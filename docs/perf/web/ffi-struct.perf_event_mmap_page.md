perf::ffi
# Struct perf_event_mmap_page 
Source 

```
#[repr(C)]pub struct perf_event_mmap_page {}
```

## Fields§
§`version: u32`§`compat_version: u32`§`lock: u32`§`index: u32`§`offset: i64`§`time_enabled: u64`§`time_running: u64`§`capabilities: perf_event_mmap_capabilities`§`pmc_width: u16`§`time_shift: u16`§`time_mult: u32`§`time_offset: u64`§`time_zero: u64`§`size: u32`§`__reserved: [u8; 948]`§`data_head: u64`§`data_tail: u64`§`data_offset: u64`§`data_size: u64`§`aux_head: u64`§`aux_tail: u64`§`aux_offset: u64`§`aux_size: u64`
## Trait Implementations§