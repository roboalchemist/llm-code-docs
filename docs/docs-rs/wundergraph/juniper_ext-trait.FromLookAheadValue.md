wundergraph::juniper_ext
# Trait FromLookAheadValue 
Source 

```
pub trait FromLookAheadValue: Sized {
    // Required method
    fn from_look_ahead(
        v: &LookAheadValue<'_, WundergraphScalarValue>,
    ) -> Option<Self>;
}
```

## Required Methods§