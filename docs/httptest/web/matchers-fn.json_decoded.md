httptest::matchers
# Function json_decoded 
Source 

```
pub fn json_decoded<T, M>(inner: M) -> JsonDecoded<T, M>where
    M: Matcher<T>,
```