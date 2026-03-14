statiq::pool::metrics
# Struct PoolMetrics 
Source 

```
pub struct PoolMetrics {
    pub active_count: AtomicU64,
    pub idle_count: AtomicU64,
    pub total_created: AtomicU64,
    pub total_destroyed: AtomicU64,
    pub total_checkouts: AtomicU64,
    pub total_timeouts: AtomicU64,
    pub total_deadlocks: AtomicU64,
    pub waiters: AtomicU64,
}
```

## Fields§
§`active_count: AtomicU64`§`idle_count: AtomicU64`§`total_created: AtomicU64`§`total_destroyed: AtomicU64`§`total_checkouts: AtomicU64`§`total_timeouts: AtomicU64`§`total_deadlocks: AtomicU64`§`waiters: AtomicU64`
## Implementations§