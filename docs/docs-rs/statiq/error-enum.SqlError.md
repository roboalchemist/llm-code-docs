statiq::error
# Enum SqlError 
Source 

```
pub enum SqlError {
    Odbc {
        code: i32,
        message: String,
    },
    PoolExhausted {
        timeout_ms: u64,
    },
    QueryTimeout {
        elapsed_ms: u64,
    },
    Cancelled,
    Cache(RedisError),
    Serialize(Error),
    DeadlockRetryExhausted {
        attempts: u8,
    },
    InvalidTransactionState,
    Config(String),
    RowMapping {
        column: String,
        reason: String,
    },
    NotFound {
        table: &'static str,
        pk: String,
    },
    Io(Error),
}
```

## Variants§
§
### Odbc