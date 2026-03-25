nix

# Macro ioctl_read

Source

```
macro_rules! ioctl_read {
    ($(#[$attr:meta])* $name:ident, $ioty:expr, $nr:expr, $ty:ty) => { ... };
}
```

Available on **Unix** only.
