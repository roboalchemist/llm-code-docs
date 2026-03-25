rnp::ping_clients::ping_client_factory
# Type Alias PingClientFactory
Source 

```
pub type PingClientFactory = fn(protocol: &RnpSupportedProtocol, config: &PingClientConfig) -> Option<Box<dyn PingClient + Send + Sync>>;
```