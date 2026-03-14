druid::lens

# Trait Lens

Source

```
pub trait Lens<T: ?Sized, U: ?Sized> {
    // Required methods
    fn with<V, F: FnOnce(&U) -> V>(&self, data: &T, f: F) -> V;
    fn with_mut<V, F: FnOnce(&mut U) -> V>(&self, data: &mut T, f: F) -> V;
}
```

## Required Methods§
