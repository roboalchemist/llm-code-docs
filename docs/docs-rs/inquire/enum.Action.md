inquire
# Enum Action 
Source 

```
pub enum Action<I>where
    I: Copy + Clone + PartialEq + Eq,{
    Submit,
    Cancel,
    Interrupt,
    Inner(I),
}
```

## Variants§
§
### Submit