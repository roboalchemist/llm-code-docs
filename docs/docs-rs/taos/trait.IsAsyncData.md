taos
# Trait IsAsyncData 
Source 

```
pub trait IsAsyncData {
    // Required methods
    fn as_raw_data<'life0, 'async_trait>(
        &'life0 self,
    ) -> Pin<Box<dyn Future<Output = Result<RawData, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait;
    fn fetch_raw_block<'life0, 'async_trait>(
        &'life0 self,
    ) -> Pin<Box<dyn Future<Output = Result<Option<RawBlock>, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait;
}
```

## Required Methods§
Source
#### fn as_raw_data<'life0, 'async_trait>(
    &'life0 self,
) -> Pin<Box<dyn Future<Output = Result<RawData, Error>> + Send + 'async_trait>>where
    'life0: 'async_trait,
    Self: 'async_trait,