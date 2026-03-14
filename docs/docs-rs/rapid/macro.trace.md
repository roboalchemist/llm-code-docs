rapid
# Macro trace 
Source 

```
macro_rules! trace {
    (target: $target:expr, $($arg:tt)*) => { ... };
    ($($arg:tt)*) => { ... };
}
```