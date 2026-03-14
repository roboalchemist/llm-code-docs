statiq::pool::metrics
# Struct MetricsSnapshot 
Source 

```
pub struct MetricsSnapshot {
    pub active: u64,
    pub idle: u64,
    pub total_created: u64,
    pub total_destroyed: u64,
    pub total_checkouts: u64,
    pub total_timeouts: u64,
    pub total_deadlocks: u64,
    pub waiters: u64,
}
```

## Fields§
§`active: u64`§`idle: u64`§`total_created: u64`§`total_destroyed: u64`§`total_checkouts: u64`§`total_timeouts: u64`§`total_deadlocks: u64`§`waiters: u64`
## Trait Implementations§