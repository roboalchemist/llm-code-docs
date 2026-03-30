inquire::list_option
# Struct ListOption 
Source 

```
pub struct ListOption<T> {
    pub index: usize,
    pub value: T,
}
```

## Fields§
§`index: usize`

Index of the selected option relative to the original (full) list passed to the prompt.
§`value: T`

Value of the selected option.

## Implementations§