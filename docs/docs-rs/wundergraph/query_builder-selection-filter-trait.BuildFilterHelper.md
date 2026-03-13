wundergraph::query_builder::selection::filter
# Trait BuildFilterHelper 
Source 

```
pub trait BuildFilterHelper<DB, F, Ctx>where
    DB: Backend,{
    type Ret: Expression<SqlType = Bool> + NonAggregate + QueryFragment<DB>;

    const FIELD_COUNT: usize;

    // Required methods
    fn into_filter(f: F) -> Option<Self::Ret>;
    fn from_inner_look_ahead(
        objs: &[(&str, LookAheadValue<'_, WundergraphScalarValue>)],
    ) -> F;
    fn from_inner_input_value(
        obj: IndexMap<&str, &InputValue<WundergraphScalarValue>>,
    ) -> Option<F>;
    fn to_inner_input_value(
        f: &F,
        _v: &mut IndexMap<&str, InputValue<WundergraphScalarValue>>,
    );
    fn register_fields<'r>(
        _info: &NameBuilder<()>,
        registry: &mut Registry<'r, WundergraphScalarValue>,
    ) -> Vec<Argument<'r, WundergraphScalarValue>>;
}
```

## Required Associated Constants§