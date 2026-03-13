taos
# Trait AsyncTBuilder 
Source 

```
pub trait AsyncTBuilder:
    Sized
    + Send
    + Sync
    + 'static {
    type Target: Send + Sync + 'static;

    // Required methods
    fn from_dsn<D>(dsn: D) -> Result<Self, Error>
       where D: IntoDsn;
    fn client_version() -> &'static str;
    fn ping<'life0, 'life1, 'async_trait>(
        &'life0 self,
        _: &'life1 mut Self::Target,
    ) -> Pin<Box<dyn Future<Output = Result<(), Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             'life1: 'async_trait,
             Self: 'async_trait;
    fn ready<'life0, 'async_trait>(
        &'life0 self,
    ) -> Pin<Box<dyn Future<Output = bool> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait;
    fn build<'life0, 'async_trait>(
        &'life0 self,
    ) -> Pin<Box<dyn Future<Output = Result<Self::Target, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait;

    // Provided methods
    fn pool(self) -> Result<Pool<Manager<Self>>, Error> { ... }
    fn pool_builder(self) -> PoolBuilder<Manager<Self>> { ... }
    fn default_pool_config(&self) -> PoolConfig { ... }
    fn with_pool_config(
        self,
        config: PoolConfig,
    ) -> Result<Pool<Manager<Self>>, Error> { ... }
}
```

## Required Associated Types§
Source
#### type Target: Send + Sync + 'static