liquid::model
# Function from_value
Source 

```
pub fn from_value<'a, T>(v: &'a dyn ValueView) -> Result<T, Error>where
    T: Deserialize<'a>,
```