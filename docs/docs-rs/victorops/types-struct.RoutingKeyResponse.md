victorops::types
# Struct RoutingKeyResponse 
Source 

```
pub struct RoutingKeyResponse {
    pub routing_key: Option<String>,
    pub targets: Vec<RoutingKeyResponseTargets>,
}
```

## Fields§
§`routing_key: Option<String>`

The routing key value.
§`targets: Vec<RoutingKeyResponseTargets>`

The targets that this routing key routes to.

## Trait Implementations§