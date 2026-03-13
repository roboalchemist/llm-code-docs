inquire::type_aliases
# Type Alias Scorer 
Source 

```
pub type Scorer<'a, T> = &'a dyn Fn(&str, &T, &str, usize) -> Option<i64>;
```