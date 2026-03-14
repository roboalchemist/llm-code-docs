nix::errno

# Trait ErrnoSentinel

Source

```
pub trait ErrnoSentinel: Sized {
    // Required method
    fn sentinel() -> Self;
}
```

Available on **Unix** only.

## Required Methods§

Source

#### fn sentinel() -> Self
