fastwebsockets::handshake

# Function client

Source

```
pub async fn client<S, E, B>(
    executor: &E,
    request: Request<B>,
    socket: S,
) -> Result<(WebSocket<TokioIo<Upgraded>>, Response<Incoming>), WebSocketError>where
    S: AsyncRead + AsyncWrite + Send + Unpin + 'static,
    E: Executor<Pin<Box<dyn Future<Output = ()> + Send>>>,
    B: Body + 'static + Send,
    B::Data: Send,
    B::Error: Into<Box<dyn Error + Send + Sync>>,
```

Available on **crate feature `upgrade`** only.
