liquid::model
# Enum DisplayCow
Source 

```
pub enum DisplayCow<'a> {
    Owned(Box<dyn Display + 'a>),
    Borrowed(&'a dyn Display),
}
```

## Variants§
§
### Owned(Box<dyn Display + 'a>)