nix

# Macro ioctl_readwrite_buf

Source

```
macro_rules! ioctl_readwrite_buf {
    ($(#[$attr:meta])* $name:ident, $ioty:expr, $nr:expr, $ty:ty) => { ... };
}
```

Available on **Unix** only.
