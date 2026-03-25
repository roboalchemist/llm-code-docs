zeromq
# Trait SocketRecv 
Source 

```
pub trait SocketRecv {
    // Required method
    fn recv<'life0, 'async_trait>(
        &'life0 mut self,
    ) -> Pin<Box<dyn Future<Output = ZmqResult<ZmqMessage>> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait;
}
```

## Required Methods§
Source
#### fn recv<'life0, 'async_trait>(
    &'life0 mut self,
) -> Pin<Box<dyn Future<Output = ZmqResult<ZmqMessage>> + Send + 'async_trait>>where
    Self: 'async_trait,
    'life0: 'async_trait,