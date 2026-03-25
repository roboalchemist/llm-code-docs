liquid::model
# Function try_find
Source 

```
pub fn try_find<'o>(
    value: &'o dyn ValueView,
    path: &[ScalarCow<'_>],
) -> Option<ValueCow<'o>>
```