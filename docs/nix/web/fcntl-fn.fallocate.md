nix::fcntl

# Function fallocate

Source

```
pub fn fallocate<Fd: AsFd>(
    fd: Fd,
    mode: FallocateFlags,
    offset: off_t,
    len: off_t,
) -> Result<()>
```

Available on **crate feature `fs`** only.
