nix

# Macro ioctl_read_buf

Source

```
macro_rules! ioctl_read_buf {
    ($(#[$attr:meta])* $name:ident, $ioty:expr, $nr:expr, $ty:ty) => { ... };
}
```

Available on **Unix** only.
