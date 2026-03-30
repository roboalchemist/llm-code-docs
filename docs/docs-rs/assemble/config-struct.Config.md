assemble::config
# Struct Config 
Source 

```
pub struct Config {
    pub name: String,
    pub version: Option<String>,
    pub env: BTreeMap<String, String>,
    pub build: Option<Vec<Build>>,
    pub deploy: Option<Vec<Step>>,
    pub storage: Option<Vec<BTreeMap<String, String>>>,
}
```

## Fields§
§`name: String`§`version: Option<String>`§`env: BTreeMap<String, String>`§`build: Option<Vec<Build>>`§`deploy: Option<Vec<Step>>`§`storage: Option<Vec<BTreeMap<String, String>>>`
## Trait Implementations§