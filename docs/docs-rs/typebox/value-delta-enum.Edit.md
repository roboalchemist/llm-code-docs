typebox::value::delta
# Enum Edit 
Source 

```
pub enum Edit {
    Insert {
        path: String,
        value: Value,
    },
    Update {
        path: String,
        value: Value,
    },
    Delete {
        path: String,
    },
}
```

## Variants§
§
### Insert