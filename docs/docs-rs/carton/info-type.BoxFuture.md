carton::info
# Type Alias BoxFuture 
Source 

```
pub type BoxFuture<'a, T> = Pin<Box<dyn Future<Output = T> + Send + 'a>>;
```

## Aliased Type§

```
pub struct BoxFuture<'a, T> { /* private fields */ }
```