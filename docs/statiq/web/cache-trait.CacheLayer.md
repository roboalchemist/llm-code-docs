statiq::cache
# Trait CacheLayer 
Source 

```
pub trait CacheLayer:
    Send
    + Sync
    + 'static {
    // Required methods
    fn default_ttl(&self) -> Duration;
    fn count_ttl(&self) -> Duration;
    fn get<'life0, 'life1, 'async_trait, T>(
        &'life0 self,
        key: &'life1 str,
    ) -> Pin<Box<dyn Future<Output = Result<Option<T>, SqlError>> + Send + 'async_trait>>
       where T: 'async_trait + DeserializeOwned + Send,
             Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait;
    fn set<'life0, 'life1, 'life2, 'async_trait, T>(
        &'life0 self,
        key: &'life1 str,
        value: &'life2 T,
        ttl: Duration,
    ) -> Pin<Box<dyn Future<Output = Result<(), SqlError>> + Send + 'async_trait>>
       where T: 'async_trait + Serialize + Send + Sync,
             Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait,
             'life2: 'async_trait;
    fn get_vec<'life0, 'life1, 'async_trait, T>(
        &'life0 self,
        key: &'life1 str,
    ) -> Pin<Box<dyn Future<Output = Result<Option<Vec<T>>, SqlError>> + Send + 'async_trait>>
       where T: 'async_trait + DeserializeOwned + Send,
             Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait;
    fn set_vec<'life0, 'life1, 'life2, 'async_trait, T>(
        &'life0 self,
        key: &'life1 str,
        values: &'life2 [T],
        ttl: Duration,
    ) -> Pin<Box<dyn Future<Output = Result<(), SqlError>> + Send + 'async_trait>>
       where T: 'async_trait + Serialize + Send + Sync,
             Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait,
             'life2: 'async_trait;
    fn get_scalar<'life0, 'life1, 'async_trait, T>(
        &'life0 self,
        key: &'life1 str,
    ) -> Pin<Box<dyn Future<Output = Result<Option<T>, SqlError>> + Send + 'async_trait>>
       where T: 'async_trait + DeserializeOwned + Send,
             Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait;
    fn set_scalar<'life0, 'life1, 'async_trait, T>(
        &'life0 self,
        key: &'life1 str,
        value: T,
        ttl: Duration,
    ) -> Pin<Box<dyn Future<Output = Result<(), SqlError>> + Send + 'async_trait>>
       where T: 'async_trait + Serialize + Send + Sync,
             Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait;
    fn invalidate_entry<'life0, 'life1, 'life2, 'async_trait>(
        &'life0 self,
        prefix: &'life1 str,
        id: &'life2 str,
    ) -> Pin<Box<dyn Future<Output = Result<(), SqlError>> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait,
             'life2: 'async_trait;
    fn invalidate_table<'life0, 'life1, 'async_trait>(
        &'life0 self,
        prefix: &'life1 str,
    ) -> Pin<Box<dyn Future<Output = Result<(), SqlError>> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait,
             'life1: 'async_trait;
}
```

## Required Methods§
Source
#### fn default_ttl(&self) -> Duration