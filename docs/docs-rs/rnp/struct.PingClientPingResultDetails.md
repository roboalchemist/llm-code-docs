rnp
# Struct PingClientPingResultDetails
Source 

```
pub struct PingClientPingResultDetails {
    pub actual_local_addr: Option<SocketAddr>,
    pub round_trip_time: Duration,
    pub is_timeout: bool,
    pub warning: Option<PingClientWarning>,
}
```

## Fields§
§`actual_local_addr: Option<SocketAddr>`§`round_trip_time: Duration`§`is_timeout: bool`§`warning: Option<PingClientWarning>`
## Implementations§