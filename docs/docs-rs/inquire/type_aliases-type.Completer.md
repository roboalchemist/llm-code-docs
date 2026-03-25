inquire::type_aliases
# Type Alias Completer 
Source 

```
pub type Completer<'a> = &'a dyn Fn(&str) -> Result<Option<String>, CustomUserError>;
```