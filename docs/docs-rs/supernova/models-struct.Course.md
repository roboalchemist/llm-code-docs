supernova::models
# Struct Course 
Source 

```
pub struct Course {
    pub id: u32,
    pub name: String,
    pub abbreviation: String,
    pub degree: Degree,
    pub description: Option<String>,
    pub active: bool,
    pub url: String,
    pub external_url: Option<String>,
    /* private fields */
}
```

## Fields§
§`id: u32`§`name: String`§`abbreviation: String`§`degree: Degree`§`description: Option<String>`§`active: bool`§`url: String`§`external_url: Option<String>`
## Implementations§