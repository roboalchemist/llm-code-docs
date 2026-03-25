rapid
# Macro log_enabled 
Source 

```
macro_rules! log_enabled {
    (target: $target:expr, $lvl:expr) => { ... };
    ($lvl:expr) => { ... };
}
```