webrtc::error
# Type Alias OnErrorHdlrFn 
Source 

```
pub type OnErrorHdlrFn = Box<dyn FnMut(Error) -> Pin<Box<dyn Future<Output = ()> + Send + 'static>> + Send + Sync>;
```

## Aliased Type§

```
pub struct OnErrorHdlrFn(/* private fields */);
```