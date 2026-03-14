rnp::ping_clients::ping_client
# Type Alias PingClientResult
Source 

```
pub type PingClientResult<T, E = PingClientError> = Result<T, E>;
```

## Aliased Type§

```
enum PingClientResult<T, E = PingClientError> {
    Ok(T),
    Err(E),
}
```

## Variants§
§1.0.0
### Ok(T)