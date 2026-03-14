rnp
# Type Alias PingClientFactory
Source 

```
pub type PingClientFactory = fn(protocol: &RnpSupportedProtocol, config: &PingClientConfig) -> Option<Box<dyn PingClient + Send + Sync>>;
```