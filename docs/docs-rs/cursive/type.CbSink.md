cursive
# Type Alias CbSink 
Source 

```
pub type CbSink = Sender<Box<dyn FnOnce(&mut Cursive) + Send>>;
```

## Aliased Type§

```
pub struct CbSink { /* private fields */ }
```