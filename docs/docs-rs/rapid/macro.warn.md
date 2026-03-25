rapid
# Macro warn 
Source 

```
macro_rules! warn {
    (target: $target:expr, $($arg:tt)*) => { ... };
    ($($arg:tt)*) => { ... };
}
```