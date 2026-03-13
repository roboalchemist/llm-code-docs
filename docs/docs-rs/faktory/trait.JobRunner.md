faktory
# Trait JobRunner 
Source 

```
pub trait JobRunner: Send + Sync {
    type Error;

    // Required method
    fn run<'life0, 'async_trait>(
        &'life0 self,
        job: Job,
    ) -> Pin<Box<dyn Future<Output = Result<(), Self::Error>> + Send + 'async_trait>>
       where Self: 'async_trait,
             'life0: 'async_trait;
}
```

## Required Associated Types§