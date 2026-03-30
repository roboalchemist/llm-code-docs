fastwebsockets::upgrade

# Function upgrade

Source

```
pub fn upgrade<B>(
    request: impl BorrowMut<Request<B>>,
) -> Result<(Response<Empty<Bytes>>, UpgradeFut), WebSocketError>
```

Available on **crate feature `upgrade`** only.
