rnp
# Struct PingWorkerConfig
Source 

```
pub struct PingWorkerConfig {
    pub protocol: RnpSupportedProtocol,
    pub target: SocketAddr,
    pub source_ip: IpAddr,
    pub ping_interval: Duration,
    pub ping_client_config: PingClientConfig,
}
```

## Fields§
§`protocol: RnpSupportedProtocol`§`target: SocketAddr`§`source_ip: IpAddr`§`ping_interval: Duration`§`ping_client_config: PingClientConfig`
## Trait Implementations§