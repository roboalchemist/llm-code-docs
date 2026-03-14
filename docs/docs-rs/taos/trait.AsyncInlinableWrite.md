taos
# Trait AsyncInlinableWrite 
Source 

```
pub trait AsyncInlinableWrite:
    AsyncWrite
    + Send
    + Unpin {
    // Provided methods
    fn write_len_with_width<'life0, 'async_trait, const N: usize>(
        &'life0 mut self,
        len: usize,
    ) -> Pin<Box<dyn Future<Output = Result<usize, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: 'async_trait { ... }
    fn write_inlined_bytes<'life0, 'life1, 'async_trait, const N: usize>(
        &'life0 mut self,
        bytes: &'life1 [u8],
    ) -> Pin<Box<dyn Future<Output = Result<usize, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             'life1: 'async_trait,
             Self: 'async_trait { ... }
    fn write_inlined_str<'life0, 'life1, 'async_trait, const N: usize>(
        &'life0 mut self,
        s: &'life1 str,
    ) -> Pin<Box<dyn Future<Output = Result<usize, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             'life1: 'async_trait,
             Self: 'async_trait { ... }
    fn write_inlinable<'life0, 'life1, 'async_trait, T>(
        &'life0 mut self,
        value: &'life1 T,
    ) -> Pin<Box<dyn Future<Output = Result<usize, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             'life1: 'async_trait,
             Self: Sized + 'async_trait,
             T: 'async_trait + AsyncInlinable + Sync { ... }
}
```

## Provided Methods§