webrtc::peer_connection
# Module configuration 
Source 
## Structs§
RTCConfigurationA Configuration defines how peer-to-peer communication via PeerConnection
is established or re-established.
Configurations may be set up once and reused across multiple connections.
Configurations are treated as readonly. As long as they are unmodified,
they are safe for concurrent use.