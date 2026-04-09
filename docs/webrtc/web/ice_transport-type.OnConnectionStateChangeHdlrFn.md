webrtc::ice_transport
# Type Alias OnConnectionStateChangeHdlrFn 
Source 

```
pub type OnConnectionStateChangeHdlrFn = Box<dyn FnMut(RTCIceTransportState) -> Pin<Box<dyn Future<Output = ()> + Send + 'static>> + Send + Sync>;
```

## Aliased Type§

```
pub struct OnConnectionStateChangeHdlrFn(/* private fields */);
```