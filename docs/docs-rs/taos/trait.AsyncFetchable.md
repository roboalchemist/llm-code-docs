taos
# Trait AsyncFetchable 
Source 

```
pub trait AsyncFetchable:
    Sized
    + Send
    + Sync {
    // Required methods
    fn affected_rows(&self) -> i32;
    fn precision(&self) -> Precision;
    fn fields(&self) -> &[Field];
    fn summary(&self) -> (usize, usize);

    // Provided methods
    fn filed_names(&self) -> Vec<&str> { ... }
    fn num_of_fields(&self) -> usize { ... }
    fn blocks(&mut self) -> AsyncBlocks<'_, Self> { ... }
    fn rows(&mut self) -> AsyncRows<'_, Self> { ... }
    fn to_records<'life0, 'async_trait>(
        &'life0 mut self,
    ) -> Pin<Box<dyn Future<Output = Result<Vec<Vec<Value>>, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait { ... }
    fn deserialize<R>(&mut self) -> AsyncDeserialized<'_, Self, R>
       where R: DeserializeOwned { ... }
}
```

## Required Methods§
Source
#### fn affected_rows(&self) -> i32