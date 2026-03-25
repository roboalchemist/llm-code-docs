statiq::transaction
# Function with_retry 
Source 

```
pub async fn with_retry<F, Fut, T>(
    pool: &Pool,
    token: &CancellationToken,
    max_retries: u8,
    f: F,
) -> Result<T, SqlError>where
    F: FnMut(&mut Transaction<'_>) -> Fut,
    Fut: Future<Output = Result<T, SqlError>>,
```