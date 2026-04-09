xmpp

# Type Alias Error

Source

```
pub type Error = Error;
```

## Aliased Type§

```
pub enum Error {
    Io(Error),
    JidParse(Error),
    Protocol(ProtocolError),
    Auth(AuthError),
    Disconnected,
    InvalidState,
    Fmt(Error),
    Utf8(Utf8Error),
    Connection(Box<dyn ServerConnectorError>),
}
```

## Variants§

§

### Io(Error)
