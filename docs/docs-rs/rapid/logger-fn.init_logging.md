rapid::logger
# Function init_logging 
Source 

```
pub fn init_logging<O: Write + Send + 'static>(output: O) -> GlobalLoggerGuard
```