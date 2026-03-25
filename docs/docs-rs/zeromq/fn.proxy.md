zeromq
# Function proxy 
Source 

```
pub async fn proxy<Frontend: SocketSend + SocketRecv, Backend: SocketSend + SocketRecv>(
    frontend: Frontend,
    backend: Backend,
    capture: Option<Box<dyn CaptureSocket>>,
) -> ZmqResult<()>
```