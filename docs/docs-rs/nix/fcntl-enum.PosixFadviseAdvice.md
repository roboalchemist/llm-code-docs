nix::fcntl

# Enum PosixFadviseAdvice

Source

```
#[non_exhaustive]#[repr(i32)]pub enum PosixFadviseAdvice {
    POSIX_FADV_NORMAL = 0,
    POSIX_FADV_SEQUENTIAL = 2,
    POSIX_FADV_RANDOM = 1,
    POSIX_FADV_NOREUSE = 5,
    POSIX_FADV_WILLNEED = 3,
    POSIX_FADV_DONTNEED = 4,
}
```

Available on **Unix and (`linux_android` or Emscripten or Fuchsia or WASI or uClibc or FreeBSD) and crate feature `fs`** only.

## Variants (Non-exhaustive)§

§

### POSIX_FADV_NORMAL = 0
