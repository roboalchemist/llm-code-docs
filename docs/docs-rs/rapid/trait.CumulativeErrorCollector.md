rapid
# Trait CumulativeErrorCollector 
Source 

```
pub trait CumulativeErrorCollector<R, E> {
    // Required method
    fn collect_if_no_errors(self) -> Result<Vec<R>, CumulativeError<E>>;
}
```

## Required Methods§
Source
#### fn collect_if_no_errors(self) -> Result<Vec<R>, CumulativeError<E>>