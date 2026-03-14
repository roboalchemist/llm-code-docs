webrtc::peer_connection
# Type Alias OnTrackHdlrFn 
Source 

```
pub type OnTrackHdlrFn = Box<dyn FnMut(Arc<TrackRemote>, Arc<RTCRtpReceiver>, Arc<RTCRtpTransceiver>) -> Pin<Box<dyn Future<Output = ()> + Send + 'static>> + Send + Sync>;
```

## Aliased Type§

```
pub struct OnTrackHdlrFn(/* private fields */);
```