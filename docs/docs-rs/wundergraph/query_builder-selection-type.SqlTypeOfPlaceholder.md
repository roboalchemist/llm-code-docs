wundergraph::query_builder::selection
# Type Alias SqlTypeOfPlaceholder 
Source 

```
pub type SqlTypeOfPlaceholder<T, DB, K, Table, Ctx> = <T as WundergraphFieldList<DB, K, Table, Ctx>>::SqlType;
```