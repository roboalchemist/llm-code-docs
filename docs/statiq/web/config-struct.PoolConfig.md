statiq::config
# Struct PoolConfig 
Source 

```
pub struct PoolConfig {
    pub max_size: u32,
    pub min_size: u32,
    pub idle_timeout_secs: u64,
    pub max_lifetime_secs: u64,
    pub checkout_timeout_ms: u64,
    pub validation_interval_secs: u64,
    pub max_deadlock_retries: u8,
    pub reset_connection_on_reuse: bool,
}
```

## Fields§
§`max_size: u32`§`min_size: u32`§`idle_timeout_secs: u64`

Close idle connections that have been unused longer than this (seconds).
§`max_lifetime_secs: u64`

Maximum lifetime of any connection regardless of activity (seconds).
Connections older than this are recycled at the next validation pass.
0 = no limit.
§`checkout_timeout_ms: u64`§`validation_interval_secs: u64`§`max_deadlock_retries: u8`§`reset_connection_on_reuse: bool`

When `true`, runs `EXEC sp_reset_connection` before reusing a pooled
connection to clear leftover session state (SET options, etc.).
This mirrors ADO.NET connection pooling behaviour but requires that the
SQL Server login has EXECUTE permission on the internal proc.
Defaults to `false` — safe for all environments.

## Trait Implementations§