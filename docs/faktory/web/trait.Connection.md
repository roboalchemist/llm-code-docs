faktory
# Trait Connection 
Source 

```
pub trait Connection:
    AsyncWrite
    + AsyncBufRead
    + Unpin
    + Send
    + Reconnect { }
```

## Implementors§
Source§
### impl<T> Connection for Twhere
    T: AsyncWrite + AsyncBufRead + Unpin + Send + Reconnect,