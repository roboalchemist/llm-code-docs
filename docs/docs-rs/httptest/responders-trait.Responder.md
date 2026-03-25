httptest::responders
# Trait Responder 
Source 

```
pub trait Responder: Send {
    // Required method
    fn respond<'a>(
        &mut self,
        req: &'a Request<Bytes>,
    ) -> Pin<Box<dyn Future<Output = Response<Bytes>> + Send + 'a>>;
}
```

## Required Methods§