rod::actor
# Trait Actor 
Source 

```
pub trait Actor:
    Send
    + Sync
    + 'static {
    // Required method
    fn handle<'life0, 'life1, 'async_trait>(
        &'life0 mut self,
        message: Message,
        context: &'life1 ActorContext,
    ) -> Pin<Box<dyn Future<Output = ()> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait;

    // Provided methods
    fn pre_start<'life0, 'life1, 'async_trait>(
        &'life0 mut self,
        _context: &'life1 ActorContext,
    ) -> Pin<Box<dyn Future<Output = ()> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait { ... }
    fn stopping<'life0, 'life1, 'async_trait>(
        &'life0 mut self,
        _context: &'life1 ActorContext,
    ) -> Pin<Box<dyn Future<Output = ()> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait { ... }
    fn subscribe_to_everything(&self) -> bool { ... }
}
```

## Required Methods§
Source
#### fn handle<'life0, 'life1, 'async_trait>(
    &'life0 mut self,
    message: Message,
    context: &'life1 ActorContext,
) -> Pin<Box<dyn Future<Output = ()> + Send + 'async_trait>>where
    Self: 'async_trait,
    'life0: 'async_trait,
    'life1: 'async_trait,