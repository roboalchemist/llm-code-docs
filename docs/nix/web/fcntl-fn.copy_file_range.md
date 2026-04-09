nix::fcntl

# Function copy_file_range

Source

```
pub fn copy_file_range<Fd1: AsFd, Fd2: AsFd>(
    fd_in: Fd1,
    off_in: Option<&mut i64>,
    fd_out: Fd2,
    off_out: Option<&mut i64>,
    len: usize,
) -> Result<usize>
```

Available on **crate feature `zerocopy`** only.
