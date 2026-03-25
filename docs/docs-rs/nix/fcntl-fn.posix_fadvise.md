nix::fcntl

# Function posix_fadvise

Source

```
pub fn posix_fadvise<Fd: AsFd>(
    fd: Fd,
    offset: off_t,
    len: off_t,
    advice: PosixFadviseAdvice,
) -> Result<()>
```

Available on **Unix and (`linux_android` or Emscripten or Fuchsia or WASI or uClibc or FreeBSD) and crate feature `fs`** only.
