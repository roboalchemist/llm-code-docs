perf::sys
# Function perf_event_open 
Source 

```
pub fn perf_event_open(
    attr: *const perf_event_attr,
    pid: pid_t,
    cpu: c_int,
    group_fd: c_int,
    flags: u64,
) -> Result<c_int, Error>
```