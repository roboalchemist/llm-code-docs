carton::info
# Trait MiscFileLoader 
Source 

```
pub trait MiscFileLoader {
    // Required method
    fn get<'life0, 'async_trait>(
        &'life0 self,
    ) -> Pin<Box<dyn Future<Output = MiscFile> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait;
}
```

## Required Methods§
Source
#### fn get<'life0, 'async_trait>(
    &'life0 self,
) -> Pin<Box<dyn Future<Output = MiscFile> + Send + 'async_trait>>where
    Self: 'async_trait,
    'life0: 'async_trait,