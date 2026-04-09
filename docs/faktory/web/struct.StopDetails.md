faktory
# Struct StopDetails 
Source 

```
#[non_exhaustive]pub struct StopDetails {
    pub reason: StopReason,
    pub workers_still_running: usize,
}
```

## Fields (Non-exhaustive)§
§`reason: StopReason`

The reason why the worker’s run has discontinued.
§`workers_still_running: usize`

The number of workers that might still be processing jobs.

## Trait Implementations§