rod::actor
# Struct ActorContext 
Source 

```
pub struct ActorContext {
    pub peer_id: Arc<RwLock<String>>,
    pub router: Addr,
    pub addr: Addr,
    pub is_stopped: Arc<RwLock<bool>>,
    pub node: Option<Node>,
    /* private fields */
}
```

## Fields§
§`peer_id: Arc<RwLock<String>>`§`router: Addr`§`addr: Addr`§`is_stopped: Arc<RwLock<bool>>`§`node: Option<Node>`
## Implementations§