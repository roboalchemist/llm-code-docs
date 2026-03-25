liquid::model
# Function to_scalar
Source 

```
pub fn to_scalar<T>(value: &T) -> Result<ScalarCow<'static>, Error>where
    T: Serialize,
```