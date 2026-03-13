rnp
# Struct PingClientConfig
Source 

```
pub struct PingClientConfig {
    pub wait_timeout: Duration,
    pub time_to_live: Option<u32>,
    pub check_disconnect: bool,
    pub wait_before_disconnect: Duration,
    pub disconnect_timeout: Duration,
    pub server_name: Option<String>,
    pub log_tls_key: bool,
    pub alpn_protocol: Option<String>,
    pub use_timer_rtt: bool,
}
```

## Fields§
§`wait_timeout: Duration`§`time_to_live: Option<u32>`§`check_disconnect: bool`§`wait_before_disconnect: Duration`§`disconnect_timeout: Duration`§`server_name: Option<String>`§`log_tls_key: bool`§`alpn_protocol: Option<String>`§`use_timer_rtt: bool`
## Trait Implementations§