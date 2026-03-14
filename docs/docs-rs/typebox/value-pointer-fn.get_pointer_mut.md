typebox::value::pointer
# Function get_pointer_mut 
Source 

```
pub fn get_pointer_mut<'a>(
    value: &'a mut Value,
    pointer: &str,
) -> Option<&'a mut Value>
```