inquire::parser
# Type Alias CustomTypeParser 
Source 

```
pub type CustomTypeParser<'a, T> = &'a dyn Fn(&str) -> Result<T, ()>;
```