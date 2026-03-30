webrtc::dtls_transport
# Type Alias OnDTLSTransportStateChangeHdlrFn 
Source 

```
pub type OnDTLSTransportStateChangeHdlrFn = Box<dyn FnMut(RTCDtlsTransportState) -> Pin<Box<dyn Future<Output = ()> + Send + 'static>> + Send + Sync>;
```

## Aliased Type§

```
pub struct OnDTLSTransportStateChangeHdlrFn(/* private fields */);
```