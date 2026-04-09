inquire::ui
# Struct Styled 
Source 

```
pub struct Styled<T>where
    T: Display,{
    pub content: T,
    pub style: StyleSheet,
}
```

## Fields§
§`content: T`

Content to be rendered.
§`style: StyleSheet`

Style sheet to be applied to content when rendered.

## Implementations§