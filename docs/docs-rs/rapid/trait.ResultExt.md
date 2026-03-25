rapid
# Trait ResultExt 
Source 

```
pub trait ResultExt<T, E> {
    // Required methods
    fn compat(self) -> Result<T, Compat<E>>;
    fn context<D>(self, context: D) -> Result<T, Context<D>>
       where D: Display + Send + Sync + 'static;
    fn with_context<F, D>(self, f: F) -> Result<T, Context<D>>
       where F: FnOnce(&E) -> D,
             D: Display + Send + Sync + 'static;
}
```

## Required Methods§