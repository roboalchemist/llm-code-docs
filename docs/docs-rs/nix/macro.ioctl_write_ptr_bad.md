nix

# Macro ioctl_write_ptr_bad

Source

```
macro_rules! ioctl_write_ptr_bad {
    ($(#[$attr:meta])* $name:ident, $nr:expr, $ty:ty) => { ... };
}
```

Available on **Unix** only.
