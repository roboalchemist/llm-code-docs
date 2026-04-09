perf::ffi
# Struct perf_event_attr 
Source 

```
#[repr(C)]pub struct perf_event_attr {}
```

## Fields§
§`type_: u32`§`size: u32`§`config: u64`§`sample: perf_event_sample_arg`§`sample_type: u64`§`read_format: u64`§`_bitfield_1: u64`§`wakeup: perf_event_wakeup_arg`§`bp_type: u32`§`config1: perf_event_config1_arg`§`config2: perf_event_config2_arg`§`branch_sample_type: u64`§`sample_regs_user: u64`§`sample_stack_user: u32`§`clockid: i32`§`sample_regs_intr: u64`§`aux_watermark: u32`§`sample_max_stack: u16`§`__reserved_2: u16`
## Trait Implementations§