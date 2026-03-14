webrtc::data_channel
# Type Alias OnOpenHdlrFn 
Source 

```
pub type OnOpenHdlrFn = Box<dyn FnOnce() -> Pin<Box<dyn Future<Output = ()> + Send + 'static>> + Send + Sync>;
```

## Aliased Type§

```
pub struct OnOpenHdlrFn(/* private fields */);
```