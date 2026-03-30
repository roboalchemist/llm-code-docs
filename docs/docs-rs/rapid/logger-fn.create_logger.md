rapid::logger
# Function create_logger 
Source 

```
pub fn create_logger<O: Write + Send + 'static>(output: O) -> Logger
```