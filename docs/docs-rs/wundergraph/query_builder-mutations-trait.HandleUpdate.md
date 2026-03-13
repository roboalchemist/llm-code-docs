wundergraph::query_builder::mutations
# Trait HandleUpdate 
Source 

```
pub trait HandleUpdate<L, U, DB, Ctx> {
    // Required method
    fn handle_update(
        selection: Option<&[Selection<'_, WundergraphScalarValue>]>,
        executor: &Executor<'_, Ctx, WundergraphScalarValue>,
        update: &U,
    ) -> ExecutionResult<WundergraphScalarValue>;
}
```

## Required Methods§