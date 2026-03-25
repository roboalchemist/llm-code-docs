wundergraph::helper
# Trait PrimaryKeyInputObject 
Source 

```
pub trait PrimaryKeyInputObject<V, I> {
    // Required methods
    fn register<'r>(
        registry: &mut Registry<'r, WundergraphScalarValue>,
        info: &I,
    ) -> Vec<Argument<'r, WundergraphScalarValue>>;
    fn from_input_value(value: &InputValue<WundergraphScalarValue>) -> Option<V>;
    fn from_look_ahead(
        look_ahead: &LookAheadValue<'_, WundergraphScalarValue>,
    ) -> Option<V>;
    fn to_input_value(values: &V) -> InputValue<WundergraphScalarValue>;
}
```

## Required Methods§
Source
#### fn register<'r>(
    registry: &mut Registry<'r, WundergraphScalarValue>,
    info: &I,
) -> Vec<Argument<'r, WundergraphScalarValue>>