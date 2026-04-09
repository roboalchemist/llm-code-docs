httptest::responders
# Function json_encoded 
Source 

```
pub fn json_encoded<T>(data: T) -> ResponseBuilder<String>where
    T: Serialize,
```