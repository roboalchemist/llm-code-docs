liquid::model
# Function to_object
Source 

```
pub fn to_object<T>(value: &T) -> Result<Object, Error>where
    T: Serialize,
```