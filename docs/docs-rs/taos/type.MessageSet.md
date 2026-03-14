taos
# Type Alias MessageSet 
Source 

```
pub type MessageSet<Meta, Data> = MessageSet<Meta, Data>;
```

## Aliased Type§

```
pub enum MessageSet<Meta, Data> {
    Meta(Meta),
    Data(Data),
    MetaData(Meta, Data),
}
```

## Variants§
§
### Meta(Meta)