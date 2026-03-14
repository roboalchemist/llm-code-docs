victorops::types
# Struct ApiOnCallOverride 
Source 

```
pub struct ApiOnCallOverride {
    pub orig_on_call_user: Option<ApiUser>,
    pub override_on_call_user: Option<ApiUser>,
    pub start: Option<DateTime<Utc>>,
    pub end: Option<DateTime<Utc>>,
    pub policy: Option<ApiEscalationPolicy>,
}
```

## Fields§
§`orig_on_call_user: Option<ApiUser>`

The original user who was scheduled to be on-call.
§`override_on_call_user: Option<ApiUser>`

The user who is overriding the original on-call assignment.
§`start: Option<DateTime<Utc>>`

The start time of the on-call override.
§`end: Option<DateTime<Utc>>`

The end time of the on-call override.
§`policy: Option<ApiEscalationPolicy>`

The escalation policy associated with this override.

## Trait Implementations§