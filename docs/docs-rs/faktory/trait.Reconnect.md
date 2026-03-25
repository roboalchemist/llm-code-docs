faktory
# Trait Reconnect 
Source 

```
pub trait Reconnect {
    // Required method
    fn reconnect<'life0, 'async_trait>(
        &'life0 mut self,
    ) -> Pin<Box<dyn Future<Output = Result<Box<dyn Connection>>> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait;
}
```

## Required Methods§