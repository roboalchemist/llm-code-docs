proptest
# Macro prop_assume 
Source 

```
macro_rules! prop_assume {
    ($expr:expr) => { ... };
    ($expr:expr, $fmt:tt $(, $fmt_arg:expr),* $(,)?) => { ... };
}
```