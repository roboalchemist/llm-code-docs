httptest::responders
# Function url_encoded 
Source 

```
pub fn url_encoded<T>(data: T) -> ResponseBuilder<String>where
    T: Serialize,
```