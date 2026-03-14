zeromq
# Trait Socket 
Source 

```
pub trait Socket: Sized + Send {
    // Required methods
    fn with_options(options: SocketOptions) -> Self;
    fn backend(&self) -> Arc<dyn MultiPeerBackend>;
    fn binds(&mut self) -> &mut HashMap<Endpoint, AcceptStopHandle>;
    fn monitor(&mut self) -> Receiver<SocketEvent>;

    // Provided methods
    fn new() -> Self { ... }
    fn bind<'life0, 'life1, 'async_trait>(
        &'life0 mut self,
        endpoint: &'life1 str,
    ) -> Pin<Box<dyn Future<Output = ZmqResult<Endpoint>> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait { ... }
    fn unbind<'life0, 'async_trait>(
        &'life0 mut self,
        endpoint: Endpoint,
    ) -> Pin<Box<dyn Future<Output = ZmqResult<()>> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait { ... }
    fn unbind_all<'life0, 'async_trait>(
        &'life0 mut self,
    ) -> Pin<Box<dyn Future<Output = Vec<ZmqError>> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait { ... }
    fn connect<'life0, 'life1, 'async_trait>(
        &'life0 mut self,
        endpoint: &'life1 str,
    ) -> Pin<Box<dyn Future<Output = ZmqResult<()>> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait { ... }
    fn close<'async_trait>(
        self,
    ) -> Pin<Box<dyn Future<Output = Vec<ZmqError>> + Send + 'async_trait>>
       where Self: 'async_trait { ... }
}
```

## Required Methods§
Source
#### fn with_options(options: SocketOptions) -> Self