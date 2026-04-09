inquire::formatter
# Type Alias OptionFormatter 
Source 

```
pub type OptionFormatter<'a, T> = &'a dyn Fn(ListOption<&T>) -> String;
```