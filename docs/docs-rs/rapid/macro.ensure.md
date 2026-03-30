rapid
# Macro ensure 
Source 

```
macro_rules! ensure {
    ($cond:expr) => { ... };
    ($cond:expr, $e:expr) => { ... };
    ($cond:expr, $fmt:expr, $($arg:tt)*) => { ... };
}
```