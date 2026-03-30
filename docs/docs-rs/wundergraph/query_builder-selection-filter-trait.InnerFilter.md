wundergraph::query_builder::selection::filter
# Trait InnerFilter 
Source 

```
pub trait InnerFilter: Sized + Nameable {
    type Context;

    const FIELD_COUNT: usize;

    // Required methods
    fn from_inner_input_value(
        v: IndexMap<&str, &InputValue<WundergraphScalarValue>>,
    ) -> Option<Self>;
    fn from_inner_look_ahead(
        v: &[(&str, LookAheadValue<'_, WundergraphScalarValue>)],
    ) -> Self;
    fn to_inner_input_value(
        &self,
        v: &mut IndexMap<&str, InputValue<WundergraphScalarValue>>,
    );
    fn register_fields<'r>(
        info: &NameBuilder<Self>,
        registry: &mut Registry<'r, WundergraphScalarValue>,
    ) -> Vec<Argument<'r, WundergraphScalarValue>>;
}
```

## Required Associated Constants§