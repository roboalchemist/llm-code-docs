supernova::models
# Struct Group 
Source 

```
pub struct Group {
    pub id: GroupKey,
    pub name: String,
    pub abbreviation: String,
    pub url: String,
    pub thumb: Option<String>,
    pub group_type: GroupType,
    pub outsiders_openness: GroupVisibility,
    pub official: bool,
    /* private fields */
}
```

## Fields§
§`id: GroupKey`§`name: String`§`abbreviation: String`§`url: String`§`thumb: Option<String>`§`group_type: GroupType`§`outsiders_openness: GroupVisibility`§`official: bool`
## Implementations§