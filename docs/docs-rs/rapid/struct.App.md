rapid
# Struct App 
Source 

```
pub struct App<TStdout, TStderr>where
    TStdout: Write + Send + 'static,
    TStderr: Write + Send + 'static,{ /* private fields */ }
```

## Implementations§