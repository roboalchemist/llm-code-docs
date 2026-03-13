taos
# Trait IsAsyncMeta 
Source 

```
pub trait IsAsyncMeta {
    // Required methods
    fn as_raw_meta<'life0, 'async_trait>(
        &'life0 self,
    ) -> Pin<Box<dyn Future<Output = Result<RawMeta, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait;
    fn as_json_meta<'life0, 'async_trait>(
        &'life0 self,
    ) -> Pin<Box<dyn Future<Output = Result<JsonMeta, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait;
}
```

## Required Methods§
Source
#### fn as_raw_meta<'life0, 'async_trait>(
    &'life0 self,
) -> Pin<Box<dyn Future<Output = Result<RawMeta, Error>> + Send + 'async_trait>>where
    'life0: 'async_trait,
    Self: 'async_trait,