wundergraph::diesel_ext
# Trait BoxableFilter 
Source 

```
pub trait BoxableFilter<QS, DB>where
    DB: Backend,
    Self: Expression + AppearsOnTable<QS> + NonAggregate + QueryFragment<DB>,{ }
```

## Trait Implementations§