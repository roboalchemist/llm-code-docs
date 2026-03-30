bat::output
# Enum OutputHandle 
Source 

```
pub enum OutputHandle<'a> {
    IoWrite(&'a mut dyn Write),
    FmtWrite(&'a mut dyn Write),
}
```

## Variants§
§
### IoWrite(&'a mut dyn Write)