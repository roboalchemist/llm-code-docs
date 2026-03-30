httptest::matchers
# Function any_of 
Source 

```
pub fn any_of<IN>(inner: Vec<Box<dyn Matcher<IN>>>) -> AnyOf<IN>where
    IN: ?Sized,
```