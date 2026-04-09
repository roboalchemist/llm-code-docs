nix::fcntl

# Function renameat2

Source

```
pub fn renameat2<P1: ?Sized + NixPath, P2: ?Sized + NixPath, Fd1: AsFd, Fd2: AsFd>(
    old_dirfd: Fd1,
    old_path: &P1,
    new_dirfd: Fd2,
    new_path: &P2,
    flags: RenameFlags,
) -> Result<()>
```

Available on **crate feature `fs`** only.
