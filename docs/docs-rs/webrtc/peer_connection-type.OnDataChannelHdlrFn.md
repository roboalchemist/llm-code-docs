webrtc::peer_connection
# Type Alias OnDataChannelHdlrFn 
Source 

```
pub type OnDataChannelHdlrFn = Box<dyn FnMut(Arc<RTCDataChannel>) -> Pin<Box<dyn Future<Output = ()> + Send + 'static>> + Send + Sync>;
```

## Aliased Type§

```
pub struct OnDataChannelHdlrFn(/* private fields */);
```