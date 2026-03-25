victorops::types
# Struct ApiOnCallEntry 
Source 

```
pub struct ApiOnCallEntry {
    pub on_call_user: Option<ApiUser>,
    pub override_on_call_user: Option<ApiUser>,
    pub on_call_type: Option<String>,
    pub rotation_name: Option<String>,
    pub shift_name: Option<String>,
    pub shift_roll: Option<DateTime<Utc>>,
    pub rolls: Vec<ApiOnCallRoll>,
}
```

## Fields§
§`on_call_user: Option<ApiUser>`

The user who is scheduled to be on-call.
§`override_on_call_user: Option<ApiUser>`

The user who is overriding the scheduled on-call user.
§`on_call_type: Option<String>`

The type of on-call assignment.
§`rotation_name: Option<String>`

The name of the rotation this entry belongs to.
§`shift_name: Option<String>`

The name of the shift this entry belongs to.
§`shift_roll: Option<DateTime<Utc>>`

The timestamp when the shift roll occurs.
§`rolls: Vec<ApiOnCallRoll>`

The list of rolls/rotations for this entry.

## Trait Implementations§