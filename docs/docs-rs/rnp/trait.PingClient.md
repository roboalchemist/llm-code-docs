rnp
# Trait PingClient
Source 

```
pub trait PingClient {
    // Required methods
    fn protocol(&self) -> &'static str;
    fn prepare_ping<'life0, 'life1, 'async_trait>(
        &'life0 mut self,
        source: &'life1 SocketAddr,
    ) -> Pin<Box<dyn Future<Output = Result<(), PingClientError>> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait;
    fn ping<'life0, 'life1, 'life2, 'async_trait>(
        &'life0 self,
        source: &'life1 SocketAddr,
        target: &'life2 SocketAddr,
    ) -> Pin<Box<dyn Future<Output = PingClientResult<PingClientPingResultDetails>> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait,
             'life2: 'async_trait;
}
```

## Required Methods§
Source
#### fn protocol(&self) -> &'static str