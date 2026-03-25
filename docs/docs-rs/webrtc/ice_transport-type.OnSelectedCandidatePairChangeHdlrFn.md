webrtc::ice_transport
# Type Alias OnSelectedCandidatePairChangeHdlrFn 
Source 

```
pub type OnSelectedCandidatePairChangeHdlrFn = Box<dyn FnMut(RTCIceCandidatePair) -> Pin<Box<dyn Future<Output = ()> + Send + 'static>> + Send + Sync>;
```

## Aliased Type§

```
pub struct OnSelectedCandidatePairChangeHdlrFn(/* private fields */);
```