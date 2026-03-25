pgp::composed
# Trait DebugBufRead 
Source 

```
pub trait DebugBufRead:
    BufRead
    + Debug
    + Send { }
```

## Implementors§
Source§
### impl<T: BufRead + Debug + Send> DebugBufRead for T