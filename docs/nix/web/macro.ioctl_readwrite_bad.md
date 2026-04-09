nix

# Macro ioctl_readwrite_bad

Source

```
macro_rules! ioctl_readwrite_bad {
    ($(#[$attr:meta])* $name:ident, $nr:expr, $ty:ty) => { ... };
}
```

Available on **Unix** only.
