cross::docker::custom
# Enum PreBuild 
Source 

```
pub enum PreBuild {
    Single {
        line: String,
        env: bool,
    },
    Lines(Vec<String>),
}
```

## Variants§
§
### Single