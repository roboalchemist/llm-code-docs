cross::errors
# Trait Section 
Source 

```
pub trait Section: Sealed {
    type Return;

    // Required methods
    fn section<D>(self, section: D) -> Self::Return
       where D: Display + Send + Sync + 'static;
    fn with_section<D, F>(self, section: F) -> Self::Return
       where D: Display + Send + Sync + 'static,
             F: FnOnce() -> D;
    fn error<E>(self, error: E) -> Self::Return
       where E: Error + Send + Sync + 'static;
    fn with_error<E, F>(self, error: F) -> Self::Return
       where F: FnOnce() -> E,
             E: Error + Send + Sync + 'static;
    fn note<D>(self, note: D) -> Self::Return
       where D: Display + Send + Sync + 'static;
    fn with_note<D, F>(self, f: F) -> Self::Return
       where D: Display + Send + Sync + 'static,
             F: FnOnce() -> D;
    fn warning<D>(self, warning: D) -> Self::Return
       where D: Display + Send + Sync + 'static;
    fn with_warning<D, F>(self, f: F) -> Self::Return
       where D: Display + Send + Sync + 'static,
             F: FnOnce() -> D;
    fn suggestion<D>(self, suggestion: D) -> Self::Return
       where D: Display + Send + Sync + 'static;
    fn with_suggestion<D, F>(self, f: F) -> Self::Return
       where D: Display + Send + Sync + 'static,
             F: FnOnce() -> D;
    fn suppress_backtrace(self, suppress: bool) -> Self::Return;
}
```

## Required Associated Types§