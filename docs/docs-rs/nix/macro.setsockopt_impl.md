nix

# Macro setsockopt_impl

Source

```
macro_rules! setsockopt_impl {
    ($name:ident, $level:expr, $flag:path, $ty:ty, $setter:ty) => { ... };
}
```

Available on **Unix** only.
