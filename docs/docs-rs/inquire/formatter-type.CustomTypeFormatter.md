inquire::formatter
# Type Alias CustomTypeFormatter 
Source 

```
pub type CustomTypeFormatter<'a, T> = &'a dyn Fn(T) -> String;
```