eventsource::reqwest
# Trait ResultExt 
Source 

```
pub trait ResultExt<T> {
    // Required method
    fn chain_err<F, EK>(self, callback: F) -> Result<T, Error>
       where F: FnOnce() -> EK,
             EK: Into<ErrorKind>;
}
```

## Required Methods§