zeromq
# Trait MultiPeerBackend 
Source 

```
pub trait MultiPeerBackend: SocketBackend {
    // Required methods
    fn peer_connected<'life0, 'async_trait>(
        self: Arc<Self>,
        peer_id: &'life0 PeerIdentity,
        io: FramedIo,
    ) -> Pin<Box<dyn Future<Output = ()> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait;
    fn peer_disconnected(&self, peer_id: &PeerIdentity);
}
```

## Required Methods§