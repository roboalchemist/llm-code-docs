taos
# Trait AsyncBindable 
Source 

```
pub trait AsyncBindable<Q>: Sizedwhere
    Q: AsyncQueryable,{
    // Required methods
    fn init<'life0, 'async_trait>(
        taos: &'life0 Q,
    ) -> Pin<Box<dyn Future<Output = Result<Self, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait;
    fn init_with_req_id<'life0, 'async_trait>(
        taos: &'life0 Q,
        req_id: u64,
    ) -> Pin<Box<dyn Future<Output = Result<Self, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait;
    fn prepare<'life0, 'life1, 'async_trait>(
        &'life0 mut self,
        sql: &'life1 str,
    ) -> Pin<Box<dyn Future<Output = Result<&'life0 mut Self, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             'life1: 'async_trait,
             Self: 'async_trait;
    fn set_tbname<'life0, 'life1, 'async_trait>(
        &'life0 mut self,
        name: &'life1 str,
    ) -> Pin<Box<dyn Future<Output = Result<&'life0 mut Self, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             'life1: 'async_trait,
             Self: 'async_trait;
    fn set_tags<'life0, 'life1, 'async_trait>(
        &'life0 mut self,
        tags: &'life1 [Value],
    ) -> Pin<Box<dyn Future<Output = Result<&'life0 mut Self, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             'life1: 'async_trait,
             Self: 'async_trait;
    fn bind<'life0, 'life1, 'async_trait>(
        &'life0 mut self,
        params: &'life1 [ColumnView],
    ) -> Pin<Box<dyn Future<Output = Result<&'life0 mut Self, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             'life1: 'async_trait,
             Self: 'async_trait;
    fn add_batch<'life0, 'async_trait>(
        &'life0 mut self,
    ) -> Pin<Box<dyn Future<Output = Result<&'life0 mut Self, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait;
    fn execute<'life0, 'async_trait>(
        &'life0 mut self,
    ) -> Pin<Box<dyn Future<Output = Result<usize, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait;
    fn affected_rows<'life0, 'async_trait>(
        &'life0 self,
    ) -> Pin<Box<dyn Future<Output = usize> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait;

    // Provided methods
    fn set_tbname_tags<'life0, 'life1, 'life2, 'async_trait>(
        &'life0 mut self,
        name: &'life1 str,
        tags: &'life2 [Value],
    ) -> Pin<Box<dyn Future<Output = Result<&'life0 mut Self, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             'life1: 'async_trait,
             'life2: 'async_trait,
             Self: Send + 'async_trait { ... }
    fn result_set<'life0, 'async_trait>(
        &'life0 mut self,
    ) -> Pin<Box<dyn Future<Output = Result<<Q as AsyncQueryable>::AsyncResultSet, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: Send + 'async_trait { ... }
}
```

## Required Methods§
Source
#### fn init<'life0, 'async_trait>(
    taos: &'life0 Q,
) -> Pin<Box<dyn Future<Output = Result<Self, Error>> + Send + 'async_trait>>where
    'life0: 'async_trait,
    Self: 'async_trait,