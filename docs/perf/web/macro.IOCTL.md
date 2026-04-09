perf
# Macro IOCTL 
Source 

```
macro_rules! IOCTL {
    ($name:ident, $ty:expr, $nr:expr) => { ... };
    ($name:ident, $ty:expr, $nr:expr, $arg:ty) => { ... };
}
```