liquid::model
# Enum ValueCow
Source 

```
pub enum ValueCow<'s> {
    Owned(Value),
    Borrowed(&'s dyn ValueView),
}
```

## Variants§
§
### Owned(Value)