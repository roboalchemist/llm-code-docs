zeromq
# Enum SocketEvent 
Source 

```
pub enum SocketEvent {
    Connected(Endpoint, PeerIdentity),
    ConnectDelayed,
    ConnectRetried,
    Listening(Endpoint),
    Accepted(Endpoint, PeerIdentity),
    AcceptFailed(ZmqError),
    Closed,
    CloseFailed,
    Disconnected(PeerIdentity),
}
```

## Variants§
§
### Connected(Endpoint, PeerIdentity)