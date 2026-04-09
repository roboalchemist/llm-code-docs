webrtc::data_channel
# Type Alias OnCloseHdlrFn 
Source 

```
pub type OnCloseHdlrFn = Box<dyn FnMut() -> Pin<Box<dyn Future<Output = ()> + Send + 'static>> + Send + Sync>;
```

## Aliased Type§

```
pub struct OnCloseHdlrFn(/* private fields */);
```