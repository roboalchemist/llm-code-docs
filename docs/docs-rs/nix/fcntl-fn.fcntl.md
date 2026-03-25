nix::fcntl

# Function fcntl

Source

```
pub fn fcntl<Fd: AsFd>(fd: Fd, arg: FcntlArg<'_>) -> Result<c_int>
```

Available on **crate feature `fs`** only.
