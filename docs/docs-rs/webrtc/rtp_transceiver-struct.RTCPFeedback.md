webrtc::rtp_transceiver
# Struct RTCPFeedback 
Source 

```
pub struct RTCPFeedback {
    pub typ: String,
    pub parameter: String,
}
```

## Fields§
§`typ: String`

Type is the type of feedback.
see: https://draft.ortc.org/#dom-rtcrtcpfeedback
valid: ack, ccm, nack, goog-remb, transport-cc
§`parameter: String`

The parameter value depends on the type.
For example, type=“nack” parameter=“pli” will send Picture Loss Indicator packets.

## Trait Implementations§