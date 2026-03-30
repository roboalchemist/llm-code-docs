iocraft
# Enum Context 
Source 

```
pub enum Context<'a> {
    Mut(&'a mut (dyn Any + Send + Sync)),
    Ref(&'a (dyn Any + Send + Sync)),
    Owned(Box<dyn Any + Send + Sync>),
}
```

## Variants§
§
### Mut(&'a mut (dyn Any + Send + Sync))