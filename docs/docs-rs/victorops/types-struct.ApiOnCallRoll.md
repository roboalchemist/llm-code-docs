victorops::types
# Struct ApiOnCallRoll 
Source 

```
pub struct ApiOnCallRoll {
    pub start: Option<DateTime<Utc>>,
    pub end: Option<DateTime<Utc>>,
    pub on_call_user: Option<ApiUser>,
    pub is_roll: Option<bool>,
}
```

## Fields§
§`start: Option<DateTime<Utc>>`

The start time of the on-call period.
§`end: Option<DateTime<Utc>>`

The end time of the on-call period.
§`on_call_user: Option<ApiUser>`

The user who is on-call during this period.
§`is_roll: Option<bool>`

Whether this is a roll/rotation period.

## Trait Implementations§