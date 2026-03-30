rnp::ping_clients::ping_client
# Enum PingClientWarning
Source 

```
pub enum PingClientWarning {
    DisconnectFailed(Box<dyn Error + Send>),
    AppHandshakeFailed(Box<dyn Error + Send>),
}
```

## Variants§
§
### DisconnectFailed(Box<dyn Error + Send>)