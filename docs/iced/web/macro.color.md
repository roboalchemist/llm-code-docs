iced
# Macro color 
Source 

```
macro_rules! color {
    ($r:expr, $g:expr, $b:expr) => { ... };
    ($r:expr, $g:expr, $b:expr, $a:expr) => { ... };
    ($hex:literal) => { ... };
    ($hex:literal, $a:expr) => { ... };
}
```