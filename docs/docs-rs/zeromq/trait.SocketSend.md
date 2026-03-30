zeromq
# Trait SocketSend 
Source 

```
pub trait SocketSend {
    // Required method
    fn send<'life0, 'async_trait>(
        &'life0 mut self,
        message: ZmqMessage,
    ) -> Pin<Box<dyn Future<Output = ZmqResult<()>> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait;
}
```

## Required Methods§
Source
#### fn send<'life0, 'async_trait>(
    &'life0 mut self,
    message: ZmqMessage,
) -> Pin<Box<dyn Future<Output = ZmqResult<()>> + Send + 'async_trait>>where
    Self: 'async_trait,
    'life0: 'async_trait,