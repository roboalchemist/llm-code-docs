wundergraph::query_builder::mutations
# Trait HandleBatchInsert 
Source 

```
pub trait HandleBatchInsert<L, I, DB, Ctx> {
    // Required method
    fn handle_batch_insert(
        selection: Option<&[Selection<'_, WundergraphScalarValue>]>,
        executor: &Executor<'_, Ctx, WundergraphScalarValue>,
        insertable: Vec<I>,
    ) -> ExecutionResult<WundergraphScalarValue>;
}
```

## Required Methods§