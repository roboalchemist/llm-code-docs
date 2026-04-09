inquire::formatter
# Type Alias MultiOptionFormatter 
Source 

```
pub type MultiOptionFormatter<'a, T> = &'a dyn Fn(&[ListOption<&T>]) -> String;
```