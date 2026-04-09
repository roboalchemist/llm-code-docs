liquid::model
# Function find
Source 

```
pub fn find<'o>(
    value: &'o dyn ValueView,
    path: &[ScalarCow<'_>],
) -> Result<ValueCow<'o>, Error>
```