webrtc::mux::mux_func
# Type Alias MatchFunc 
Source 

```
pub type MatchFunc = Box<dyn Fn(&[u8]) -> bool + Send + Sync>;
```

## Aliased Type§

```
pub struct MatchFunc(/* private fields */);
```