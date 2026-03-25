nix::sys::socket

# Trait SetSockOpt

Source

```
pub trait SetSockOpt: Clone {
    type Val: ?Sized;

    // Required method
    fn set<F: AsFd>(&self, fd: &F, val: &Self::Val) -> Result<()>;
}
```

Available on **crate feature `socket`** only.

## Required Associated Types§

Source

#### type Val: ?Sized
