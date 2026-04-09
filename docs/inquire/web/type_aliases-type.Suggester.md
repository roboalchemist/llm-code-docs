inquire::type_aliases
# Type Alias Suggester 
Source 

```
pub type Suggester<'a> = &'a dyn Fn(&str) -> Result<Vec<String>, CustomUserError>;
```