wundergraph::query_builder::mutations
# Trait HandleDelete 
Source 

```
pub trait HandleDelete<L, K, DB, Ctx> {
    // Required method
    fn handle_delete(
        executor: &Executor<'_, Ctx, WundergraphScalarValue>,
        to_delete: &K,
    ) -> ExecutionResult<WundergraphScalarValue>;
}
```

## Required Methods§