adjust::controller
# Trait Controller 
Source 

```
pub trait Controller<S>: ControllerInitialization<S>where
    S: Clone + Send + Sync + 'static,{
    // Required method
    fn register(&self, router: Router<S>) -> Router<S>;
}
```

## Required Methods§
Source
#### fn register(&self, router: Router<S>) -> Router<S>