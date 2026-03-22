adjust::database
# Trait PoolBuilder 
Source 

```
pub trait PoolBuilder<T: ManageConnection> {
    // Required method
    fn create_pool() -> Result<Pool<T>>;
}
```

## Required Methods§
Source
#### fn create_pool() -> Result<Pool<T>>