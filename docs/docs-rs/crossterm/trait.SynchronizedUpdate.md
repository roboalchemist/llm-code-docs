crossterm
# Trait SynchronizedUpdate 
Source 

```
pub trait SynchronizedUpdate {
    // Required method
    fn sync_update<T>(
        &mut self,
        operations: impl FnOnce(&mut Self) -> T,
    ) -> Result<T>;
}
```

## Required Methods§