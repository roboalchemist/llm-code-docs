webrtc::peer_connection
# Type Alias OnNegotiationNeededHdlrFn 
Source 

```
pub type OnNegotiationNeededHdlrFn = Box<dyn FnMut() -> Pin<Box<dyn Future<Output = ()> + Send + 'static>> + Send + Sync>;
```

## Aliased Type§

```
pub struct OnNegotiationNeededHdlrFn(/* private fields */);
```