adjust::controller
# Trait ControllerInitialization 
Source 

```
pub trait ControllerInitialization<S>where
    S: Clone + Send + Sync + 'static,{
    // Required method
    fn new() -> impl Future<Output = Result<Box<Self>>>
       where Self: Sized;
}
```

## Required Methods§
Source
#### fn new() -> impl Future<Output = Result<Box<Self>>>where
    Self: Sized,