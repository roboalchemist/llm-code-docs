rapid
# Trait Fail 
Source 

```
pub trait Fail:
    Display
    + Debug
    + Send
    + Sync
    + 'static {
    // Provided methods
    fn name(&self) -> Option<&str> { ... }
    fn cause(&self) -> Option<&(dyn Fail + 'static)> { ... }
    fn backtrace(&self) -> Option<&Backtrace> { ... }
    fn context<D>(self, context: D) -> Context<D>
       where D: Display + Send + Sync + 'static,
             Self: Sized { ... }
    fn compat(self) -> Compat<Self>
       where Self: Sized { ... }
}
```

## Provided Methods§