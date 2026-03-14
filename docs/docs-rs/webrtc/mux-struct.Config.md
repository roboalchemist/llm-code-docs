webrtc::mux
# Struct Config 
Source 

```
pub struct Config {
    pub conn: Arc<dyn Conn + Send + Sync>,
    pub buffer_size: usize,
}
```

## Fields§
§`conn: Arc<dyn Conn + Send + Sync>`§`buffer_size: usize`
## Auto Trait Implementations§
§
### impl Freeze for Config