taos
# Trait AsyncInlinableRead 
Source 

```
pub trait AsyncInlinableRead:
    AsyncRead
    + Unpin
    + Send {
    // Provided methods
    fn read_len_with_width<'life0, 'async_trait, const N: usize>(
        &'life0 mut self,
    ) -> Pin<Box<dyn Future<Output = Result<usize, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait { ... }
    fn read_len_with_data<'life0, 'async_trait, const N: usize>(
        &'life0 mut self,
    ) -> Pin<Box<dyn Future<Output = Result<Vec<u8>, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait { ... }
    fn read_inlined_bytes<'life0, 'async_trait, const N: usize>(
        &'life0 mut self,
    ) -> Pin<Box<dyn Future<Output = Result<Vec<u8>, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait { ... }
    fn read_inlined_str<'life0, 'async_trait, const N: usize>(
        &'life0 mut self,
    ) -> Pin<Box<dyn Future<Output = Result<String, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait { ... }
    fn read_inlinable<'life0, 'async_trait, T>(
        &'life0 mut self,
    ) -> Pin<Box<dyn Future<Output = Result<T, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             T: 'async_trait + AsyncInlinable,
             Self: 'async_trait { ... }
}
```

## Provided Methods§