nix

# Macro ioctl_write_buf

Source

```
macro_rules! ioctl_write_buf {
    ($(#[$attr:meta])* $name:ident, $ioty:expr, $nr:expr, $ty:ty) => { ... };
}
```

Available on **Unix** only.
