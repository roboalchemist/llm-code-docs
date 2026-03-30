wundergraph::query_builder::selection::filter
# Trait BuildFilter 
Source 

```
pub trait BuildFilter<DB>where
    DB: Backend,{
    type Ret: Expression<SqlType = Bool> + NonAggregate + QueryFragment<DB>;

    // Required method
    fn into_filter(self) -> Option<Self::Ret>;
}
```

## Required Associated Types§