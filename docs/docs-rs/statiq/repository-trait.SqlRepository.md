statiq::repository
# Trait SqlRepository 
Source 

```
pub trait SqlRepository<T: SqlEntity>: Send + Sync {
}
```

## Required Methods§
Source
#### fn get_by_id<'life0, 'life1, 'async_trait>(
    &'life0 self,
    id: impl 'async_trait + Into<PkValue> + Send,
    token: &'life1 CancellationToken,
) -> Pin<Box<dyn Future<Output = Result<Option<T>, SqlError>> + Send + 'async_trait>>where
    Self: 'async_trait,
    'life0: 'async_trait,
    'life1: 'async_trait,