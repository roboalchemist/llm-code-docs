webrtc::peer_connection
# Type Alias OnICEConnectionStateChangeHdlrFn 
Source 

```
pub type OnICEConnectionStateChangeHdlrFn = Box<dyn FnMut(RTCIceConnectionState) -> Pin<Box<dyn Future<Output = ()> + Send + 'static>> + Send + Sync>;
```

## Aliased Type§

```
pub struct OnICEConnectionStateChangeHdlrFn(/* private fields */);
```