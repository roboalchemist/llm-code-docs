bellman::multiexp
# Trait QueryDensity 
Source 

```
pub trait QueryDensity {
    type Iter: Iterator<Item = bool>;

    // Required methods
    fn iter(self) -> Self::Iter;
    fn get_query_size(self) -> Option<usize>;
}
```

## Required Associated Types§