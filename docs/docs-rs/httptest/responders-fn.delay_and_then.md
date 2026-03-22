httptest::responders
# Function delay_and_then 
Source 

```
pub fn delay_and_then<R: Responder>(delay: Duration, and_then: R) -> Delay<R>
```