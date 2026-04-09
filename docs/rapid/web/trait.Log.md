rapid
# Trait Log 
Source 

```
pub trait Log: Sync + Send {
    // Required methods
    fn enabled(&self, metadata: &LogMetadata<'_>) -> bool;
    fn log(&self, record: &LogRecord<'_>);
}
```

## Required Methods§