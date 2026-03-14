iced
# Trait Executor 
Source 

```
pub trait Executor: Sized {
    // Required methods
    fn new() -> Result<Self, Error>
       where Self: Sized;
    fn spawn(&self, future: impl Future<Output = ()> + MaybeSend + 'static);
    fn block_on<T>(&self, future: impl Future<Output = T>) -> T;

    // Provided method
    fn enter<R>(&self, f: impl FnOnce() -> R) -> R { ... }
}
```

## Required Methods§