carton::types
# Enum Device 
Source 

```
pub enum Device {
    CPU,
    GPU {
        uuid: Option<String>,
    },
}
```

## Variants§
§
### CPU