rapid
# Macro debug 
Source 

```
macro_rules! debug {
    (target: $target:expr, $($arg:tt)*) => { ... };
    ($($arg:tt)*) => { ... };
}
```