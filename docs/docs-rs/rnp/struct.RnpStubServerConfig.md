rnp
# Struct RnpStubServerConfig
Source 

```
pub struct RnpStubServerConfig {
    pub protocol: RnpSupportedProtocol,
    pub server_address: SocketAddr,
    pub report_interval: Duration,
    pub close_on_accept: bool,
    pub write_chunk_size: usize,
    pub write_count_limit: u32,
    pub sleep_before_write: Duration,
    pub wait_before_disconnect: Duration,
}
```

## Fields§
§`protocol: RnpSupportedProtocol`§`server_address: SocketAddr`§`report_interval: Duration`§`close_on_accept: bool`§`write_chunk_size: usize`§`write_count_limit: u32`§`sleep_before_write: Duration`§`wait_before_disconnect: Duration`
## Trait Implementations§