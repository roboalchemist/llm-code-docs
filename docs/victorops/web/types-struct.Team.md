victorops::types
# Struct Team 
Source 

```
pub struct Team {
    pub name: Option<String>,
    pub slug: Option<String>,
    pub member_count: Option<i32>,
    pub version: Option<i32>,
    pub is_default_team: Option<bool>,
}
```

## Fields§
§`name: Option<String>`

The name of the team.
§`slug: Option<String>`

The unique slug identifier for the team.
§`member_count: Option<i32>`

The number of members in the team.
§`version: Option<i32>`

The version of the team configuration.
§`is_default_team: Option<bool>`

Whether this is the default team for the organization.

## Trait Implementations§