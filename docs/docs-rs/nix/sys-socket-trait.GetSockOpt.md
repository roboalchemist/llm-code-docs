nix::sys::socket

# Trait GetSockOpt

Source

```
pub trait GetSockOpt: Copy {
    type Val;

    // Required method
    fn get<F: AsFd>(&self, fd: &F) -> Result<Self::Val>;
}
```

Available on **crate feature `socket`** only.

## Required Associated Types§

Source

#### type Val
