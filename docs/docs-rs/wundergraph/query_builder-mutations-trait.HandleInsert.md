wundergraph::query_builder::mutations
# Trait HandleInsert 
Source 

```
pub trait HandleInsert<L, I, DB, Ctx> {
    // Required method
    fn handle_insert(
        selection: Option<&[Selection<'_, WundergraphScalarValue>]>,
        executor: &Executor<'_, Ctx, WundergraphScalarValue>,
        insertable: I,
    ) -> ExecutionResult<WundergraphScalarValue>;
}
```

## Required Methods§