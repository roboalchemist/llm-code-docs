rapid
# Function set_logger_raw 
Source 

```
pub unsafe fn set_logger_raw<M>(make_logger: M) -> Result<(), SetLoggerError>where
    M: FnOnce(MaxLogLevelFilter) -> *const dyn Log,
```