wundergraph::query_builder::selection::filter
# Trait FilterValue 
Source 

```
pub trait FilterValue<C> {
    type RawValue: Clone + FromInputValue<WundergraphScalarValue> + FromLookAheadValue + ToInputValue<WundergraphScalarValue>;
    type AdditionalFilter;
}
```

## Required Associated Types§