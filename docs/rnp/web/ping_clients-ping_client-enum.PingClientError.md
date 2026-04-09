rnp::ping_clients::ping_client
# Enum PingClientError
Source 

```
pub enum PingClientError {
    PreparationFailed(Box<dyn Error + Send>),
    PingFailed(Box<dyn Error + Send>),
}
```

## Variants§
§
### PreparationFailed(Box<dyn Error + Send>)