cross::docker::custom
# Enum Dockerfile 
Source 

```
pub enum Dockerfile<'a> {
    File {
        path: &'a str,
        context: Option<&'a str>,
        name: Option<&'a str>,
    },
    Custom {
        content: String,
    },
}
```

## Variants§
§
### File