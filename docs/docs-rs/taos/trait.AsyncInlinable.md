taos
# Trait AsyncInlinable 
Source 

```
pub trait AsyncInlinable {
    // Required methods
    fn read_inlined<'life0, 'async_trait, R>(
        reader: &'life0 mut R,
    ) -> Pin<Box<dyn Future<Output = Result<Self, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: Sized + 'async_trait,
             R: 'async_trait + AsyncRead + Send + Unpin;
    fn write_inlined<'life0, 'life1, 'async_trait, W>(
        &'life0 self,
        wtr: &'life1 mut W,
    ) -> Pin<Box<dyn Future<Output = Result<usize, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             'life1: 'async_trait,
             W: 'async_trait + AsyncWrite + Send + Unpin,
             Self: 'async_trait;

    // Provided methods
    fn read_optional_inlined<'life0, 'async_trait, R>(
        reader: &'life0 mut R,
    ) -> Pin<Box<dyn Future<Output = Result<Option<Self>, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: Sized + Send + 'async_trait,
             R: 'async_trait + AsyncRead + Send + Unpin { ... }
    fn write_inlined_with<'life0, 'life1, 'async_trait, W>(
        &'life0 self,
        wtr: &'life1 mut W,
        _opts: InlineOpts,
    ) -> Pin<Box<dyn Future<Output = Result<usize, Error>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             'life1: 'async_trait,
             W: 'async_trait + AsyncWrite + Send + Unpin,
             Self: Sync + 'async_trait { ... }
    fn inlined<'life0, 'async_trait>(
        &'life0 self,
    ) -> Pin<Box<dyn Future<Output = Vec<u8>> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: Sync + 'async_trait { ... }
    fn printable_inlined<'life0, 'async_trait>(
        &'life0 self,
    ) -> Pin<Box<dyn Future<Output = String> + Send + 'async_trait>>
       where 'life0: 'async_trait,
             Self: Sync + 'async_trait { ... }
}
```

## Required Methods§