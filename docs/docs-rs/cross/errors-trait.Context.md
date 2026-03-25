cross::errors
# Trait Context 
Source 

```
pub trait Context<T, E>: Sealed {
    // Required methods
    fn wrap_err<D>(self, msg: D) -> Result<T, Report>
       where D: Display + Send + Sync + 'static;
    fn wrap_err_with<D, F>(self, f: F) -> Result<T, Report>
       where D: Display + Send + Sync + 'static,
             F: FnOnce() -> D;
    fn context<D>(self, msg: D) -> Result<T, Report>
       where D: Display + Send + Sync + 'static;
    fn with_context<D, F>(self, f: F) -> Result<T, Report>
       where D: Display + Send + Sync + 'static,
             F: FnOnce() -> D;
}
```

## Required Methods§