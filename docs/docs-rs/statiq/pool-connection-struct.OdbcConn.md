statiq::pool::connection
# Struct OdbcConn 
Source 

```
pub struct OdbcConn {
    pub state: ConnState,
    pub created_at: Instant,
    pub last_used_at: Instant,
    pub needs_reset: bool,
    pub reset_on_reuse: bool,
    /* private fields */
}
```

## Fields§
§`state: ConnState`§`created_at: Instant`§`last_used_at: Instant`§`needs_reset: bool`

Set to `true` when the connection is returned to the pool.
The next execute call will run `EXEC sp_reset_connection` first to clear
any leftover session state (SET options, implicit transactions, etc.).
Only effective when `reset_on_reuse` is also `true`.
§`reset_on_reuse: bool`

Mirrors `PoolConfig::reset_connection_on_reuse`. When `false` (default),
`sp_reset_connection` is never executed regardless of `needs_reset`.

## Implementations§