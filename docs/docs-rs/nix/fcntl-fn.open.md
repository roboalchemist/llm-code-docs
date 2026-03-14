nix::fcntl

# Function open

Source

```
pub fn open<P: ?Sized + NixPath>(
    path: &P,
    oflag: OFlag,
    mode: Mode,
) -> Result<OwnedFd>
```

Available on **crate feature `fs`** only.
