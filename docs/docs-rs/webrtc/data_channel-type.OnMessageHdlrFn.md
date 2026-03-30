webrtc::data_channel
# Type Alias OnMessageHdlrFn 
Source 

```
pub type OnMessageHdlrFn = Box<dyn FnMut(DataChannelMessage) -> Pin<Box<dyn Future<Output = ()> + Send + 'static>> + Send + Sync>;
```

## Aliased Type§

```
pub struct OnMessageHdlrFn(/* private fields */);
```