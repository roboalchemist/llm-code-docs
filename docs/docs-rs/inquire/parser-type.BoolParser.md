inquire::parser
# Type Alias BoolParser 
Source 

```
pub type BoolParser<'a> = &'a dyn Fn(&str) -> Result<bool, ()>;
```