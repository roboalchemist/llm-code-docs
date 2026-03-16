httptest::responders
# Macro cycle 
Source 

```
macro_rules! cycle {
    ($($x:expr),*) => { ... };
    ($($x:expr,)*) => { ... };
}
```