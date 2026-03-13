wundergraph::query_builder::selection::fields
# Trait WundergraphBelongsTo 
Source 

```
pub trait WundergraphBelongsTo<Other, DB, Ctx, FK>: LoadingHandler<DB, Ctx>where
    DB: Backend + ApplyOffset + 'static,
    Self::Table: 'static,
    <Self::Table as QuerySource>::FromClause: QueryFragment<DB>,
    DB::QueryBuilder: Default,
    FK: Default + NonAggregate + SelectableExpression<Self::Table> + QueryFragment<DB>,{
    type Key: Eq + Hash;

    // Required method
    fn resolve(
        global_args: &[LookAheadArgument<'_, WundergraphScalarValue>],
        look_ahead: &LookAheadSelection<'_, WundergraphScalarValue>,
        selection: Option<&[Selection<'_, WundergraphScalarValue>]>,
        keys: &[Option<Self::Key>],
        executor: &Executor<'_, Ctx, WundergraphScalarValue>,
    ) -> Result<HashMap<Option<Self::Key>, Vec<Value<WundergraphScalarValue>>>>;

    // Provided method
    fn build_response(
        res: Vec<(Option<Self::Key>, <Self::FieldList as WundergraphFieldList<DB, Self::PrimaryKeyIndex, Self::Table, Ctx>>::PlaceHolder)>,
        global_args: &[LookAheadArgument<'_, WundergraphScalarValue>],
        look_ahead: &LookAheadSelection<'_, WundergraphScalarValue>,
        selection: Option<&[Selection<'_, WundergraphScalarValue>]>,
        executor: &Executor<'_, Ctx, WundergraphScalarValue>,
    ) -> Result<HashMap<Option<Self::Key>, Vec<Value<WundergraphScalarValue>>>> { ... }
}
```

## Required Associated Types§