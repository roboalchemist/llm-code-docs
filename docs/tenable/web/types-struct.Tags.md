tenable::types
# Struct Tags 
Source 

```
pub struct Tags {
    pub tag_uuid: Option<String>,
    pub tag_key: Option<String>,
    pub tag_value: Option<String>,
    pub added_by: Option<String>,
    pub added_at: Option<String>,
}
```

## Fields§
§`tag_uuid: Option<String>`

The UUID of the tag.
§`tag_key: Option<String>`

The tag category (the first half of the category:value pair).
§`tag_value: Option<String>`

The tag value (the second half of the category:value pair).
§`added_by: Option<String>`

The UUID of the user who assigned the tag to the asset.
§`added_at: Option<String>`

The ISO timestamp when the tag was assigned to the asset.

## Trait Implementations§