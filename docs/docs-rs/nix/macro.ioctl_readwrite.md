nix

# Macro ioctl_readwrite

Source

```
macro_rules! ioctl_readwrite {
    ($(#[$attr:meta])* $name:ident, $ioty:expr, $nr:expr, $ty:ty) => { ... };
}
```

Available on **Unix** only.
