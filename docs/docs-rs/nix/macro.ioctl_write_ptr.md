nix

# Macro ioctl_write_ptr

Source

```
macro_rules! ioctl_write_ptr {
    ($(#[$attr:meta])* $name:ident, $ioty:expr, $nr:expr, $ty:ty) => { ... };
}
```

Available on **Unix** only.
