rnp::ping_clients::ping_client_factory
# Function new_ping_client
Source 

```
pub fn new_ping_client(
    protocol: &RnpSupportedProtocol,
    config: &PingClientConfig,
    external_ping_client_factory: Option<PingClientFactory>,
) -> Box<dyn PingClient + Send + Sync>
```