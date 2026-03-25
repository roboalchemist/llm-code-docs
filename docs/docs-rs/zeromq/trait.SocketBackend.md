zeromq
# Trait SocketBackend 
Source 

```
pub trait SocketBackend: Send + Sync {
    // Required methods
    fn socket_type(&self) -> SocketType;
    fn socket_options(&self) -> &SocketOptions;
    fn shutdown(&self);
    fn monitor(&self) -> &Mutex<Option<Sender<SocketEvent>>>;
}
```

## Required Methods§
Source
#### fn socket_type(&self) -> SocketType