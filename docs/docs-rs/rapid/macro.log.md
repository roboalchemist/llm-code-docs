rapid
# Macro log 
Source 

```
macro_rules! log {
    (target: $target:expr, $lvl:expr, $($arg:tt)+) => { ... };
    ($lvl:expr, $($arg:tt)+) => { ... };
}
```