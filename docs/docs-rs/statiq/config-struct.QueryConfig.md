statiq::config
# Struct QueryConfig 
Source 

```
pub struct QueryConfig {
    pub default_command_timeout_secs: u64,
    pub slow_query_threshold_ms: u64,
    pub max_text_bytes: usize,
}
```

## Fields§
§`default_command_timeout_secs: u64`§`slow_query_threshold_ms: u64`§`max_text_bytes: usize`

Maximum byte size for a single text/binary cell in TextRowSet (scaffold mode).
Cells wider than this limit are silently truncated by the ODBC driver.
Default: 65536 (64 KiB). Increase for nvarchar(max)/xml/varbinary(max) columns.

## Trait Implementations§