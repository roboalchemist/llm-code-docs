victorops::types
# Struct RoutingKey 
Source 

```
pub struct RoutingKey {
    pub routing_key: Option<String>,
    pub targets: Vec<String>,
}
```

## Fields§
§`routing_key: Option<String>`

The routing key value used to route alerts.
§`targets: Vec<String>`

The list of targets that this routing key routes to.

## Trait Implementations§