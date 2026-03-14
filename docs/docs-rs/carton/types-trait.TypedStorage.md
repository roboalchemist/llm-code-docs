carton::types
# Trait TypedStorage 
Source 

```
pub trait TypedStorage<T> {
    // Required methods
    fn view(&self) -> ArrayViewD<'_, T>;
    fn view_mut(&mut self) -> ArrayViewMutD<'_, T>;
}
```

## Required Methods§
Source
#### fn view(&self) -> ArrayViewD<'_, T>