rapid
# Macro error 
Source 

```
macro_rules! error {
    (target: $target:expr, $($arg:tt)*) => { ... };
    ($($arg:tt)*) => { ... };
}
```