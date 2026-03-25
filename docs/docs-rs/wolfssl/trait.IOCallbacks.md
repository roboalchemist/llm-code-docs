wolfssl
# Trait IOCallbacks 
Source 

```
pub trait IOCallbacks {
    // Required methods
    fn recv(&mut self, buf: &mut [u8]) -> IOCallbackResult<usize>;
    fn send(&mut self, buf: &[u8]) -> IOCallbackResult<usize>;
}
```

## Required Methods§