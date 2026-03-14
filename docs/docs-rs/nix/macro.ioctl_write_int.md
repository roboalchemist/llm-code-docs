nix

# Macro ioctl_write_int

Source

```
macro_rules! ioctl_write_int {
    ($(#[$attr:meta])* $name:ident, $ioty:expr, $nr:expr) => { ... };
}
```

Available on **Unix** only.
