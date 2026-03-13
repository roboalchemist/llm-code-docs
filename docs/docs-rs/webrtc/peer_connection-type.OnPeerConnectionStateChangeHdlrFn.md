webrtc::peer_connection
# Type Alias OnPeerConnectionStateChangeHdlrFn 
Source 

```
pub type OnPeerConnectionStateChangeHdlrFn = Box<dyn FnMut(RTCPeerConnectionState) -> Pin<Box<dyn Future<Output = ()> + Send + 'static>> + Send + Sync>;
```

## Aliased Type§

```
pub struct OnPeerConnectionStateChangeHdlrFn(/* private fields */);
```