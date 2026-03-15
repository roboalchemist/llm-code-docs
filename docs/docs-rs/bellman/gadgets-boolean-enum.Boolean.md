bellman::gadgets::boolean
# Enum Boolean 
Source 

```
pub enum Boolean {
    Is(AllocatedBit),
    Not(AllocatedBit),
    Constant(bool),
}
```

## Variants§
§
### Is(AllocatedBit)