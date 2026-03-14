rapid
# Function set_logger 
Source 

```
pub fn set_logger<M>(make_logger: M) -> Result<(), SetLoggerError>where
    M: FnOnce(MaxLogLevelFilter) -> Box<dyn Log>,
```