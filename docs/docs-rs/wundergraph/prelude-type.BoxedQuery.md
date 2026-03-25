wundergraph::prelude
# Type Alias BoxedQuery 
Source 

```
pub type BoxedQuery<'a, L, DB, Ctx> = BoxedSelectStatement<'a, SqlTypeOfPlaceholder<<L as LoadingHandler<DB, Ctx>>::FieldList, DB, <L as LoadingHandler<DB, Ctx>>::PrimaryKeyIndex, <L as HasTable>::Table, Ctx>, <L as HasTable>::Table, DB>;
```

## Aliased Type§

```
pub struct BoxedQuery<'a, L, DB, Ctx> { /* private fields */ }
```