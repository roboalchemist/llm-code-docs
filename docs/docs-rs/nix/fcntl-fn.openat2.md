nix::fcntl

# Function openat2

Source

```
pub fn openat2<P: ?Sized + NixPath, Fd: AsFd>(
    dirfd: Fd,
    path: &P,
    how: OpenHow,
) -> Result<OwnedFd>
```

Available on **Unix** only.
