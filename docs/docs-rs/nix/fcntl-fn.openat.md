nix::fcntl

# Function openat

Source

```
pub fn openat<P: ?Sized + NixPath, Fd: AsFd>(
    dirfd: Fd,
    path: &P,
    oflag: OFlag,
    mode: Mode,
) -> Result<OwnedFd>
```

Available on **crate feature `fs`** only.
