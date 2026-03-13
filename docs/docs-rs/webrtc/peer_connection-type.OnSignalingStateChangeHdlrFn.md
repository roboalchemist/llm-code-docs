webrtc::peer_connection
# Type Alias OnSignalingStateChangeHdlrFn 
Source 

```
pub type OnSignalingStateChangeHdlrFn = Box<dyn FnMut(RTCSignalingState) -> Pin<Box<dyn Future<Output = ()> + Send + 'static>> + Send + Sync>;
```

## Aliased Type§

```
pub struct OnSignalingStateChangeHdlrFn(/* private fields */);
```