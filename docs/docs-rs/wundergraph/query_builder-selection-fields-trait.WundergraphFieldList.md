wundergraph::query_builder::selection::fields
# Trait WundergraphFieldList 
Source 

```
pub trait WundergraphFieldList<DB: Backend, Key, Table, Ctx> {
    type PlaceHolder: Queryable<Self::SqlType, DB> + 'static;
    type SqlType: 'static;

    const TABLE_FIELD_COUNT: usize;
    const NON_TABLE_FIELD_COUNT: usize;

    // Required method
    fn resolve(
        placeholder: Vec<Self::PlaceHolder>,
        global_args: &[LookAheadArgument<'_, WundergraphScalarValue>],
        select: &LookAheadSelection<'_, WundergraphScalarValue>,
        selection: Option<&[Selection<'_, WundergraphScalarValue>]>,
        name_list: &'static [&'static str],
        executor: &Executor<'_, Ctx, WundergraphScalarValue>,
    ) -> Result<Vec<Value<WundergraphScalarValue>>>;
}
```

## Required Associated Constants§