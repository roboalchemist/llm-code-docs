rapid
# Trait OptionMethods 
Source 

```
pub trait OptionMethods {
    type TOk;

    // Required methods
    fn ok_or_error<D>(self, context: D) -> Result<Self::TOk, Error>
       where D: Into<Error>;
    fn ok_or_else_error<F, D>(self, f: F) -> Result<Self::TOk, Error>
       where F: FnOnce() -> D,
             D: Into<Error>;
    fn ok_or_error_msg<D>(self, msg: D) -> Result<Self::TOk, Error>
       where D: Display + Debug + Send + Sync + 'static;
    fn ok_or_else_error_msg<F, D>(self, f: F) -> Result<Self::TOk, Error>
       where F: FnOnce() -> D,
             D: Display + Debug + Send + Sync + 'static;
}
```

## Required Associated Types§
Source
#### type TOk