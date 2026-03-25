rapid
# Trait ResultMethods 
Source 

```
pub trait ResultMethods {
    type TOk;
    type TError;

    // Required methods
    fn if_error_log_error(&self) -> &Self;
    fn if_error_log_warning(&self) -> &Self;
    fn context_error<D>(self, context: D) -> Result<Self::TOk, Error>
       where D: Display + Send + Sync + 'static;
    fn with_context_error<F, D>(self, f: F) -> Result<Self::TOk, Error>
       where F: FnOnce(&Self::TError) -> D,
             D: Display + Send + Sync + 'static;
    fn context_error_msg<D>(self, msg: D) -> Result<Self::TOk, Error>
       where D: Display + Debug + Send + Sync + 'static;
    fn with_context_error_msg<F, D>(self, f: F) -> Result<Self::TOk, Error>
       where F: FnOnce() -> D,
             D: Display + Debug + Send + Sync + 'static;

    // Provided methods
    fn if_error_log_error_and_ignore(&self) { ... }
    fn if_error_log_warning_and_ignore(&self) { ... }
}
```

## Required Associated Types§
Source
#### type TOk