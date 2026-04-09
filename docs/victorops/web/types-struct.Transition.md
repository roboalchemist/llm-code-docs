victorops::types
# Struct Transition 
Source 

```
pub struct Transition {
    pub name: Option<String>,
    pub at: Option<DateTime<Utc>>,
    pub message: Option<String>,
    pub by: Option<String>,
    pub manually: Option<bool>,
    pub alert_id: Option<String>,
    pub alert_url: Option<String>,
}
```

## Fields§
§`name: Option<String>`

The name of the transition.
§`at: Option<DateTime<Utc>>`

When the transition occurred.
§`message: Option<String>`

Message associated with the transition.
§`by: Option<String>`

Who performed the transition.
§`manually: Option<bool>`

Whether the transition was performed manually.
§`alert_id: Option<String>`

The ID of the alert that triggered this transition.
§`alert_url: Option<String>`

The URL of the alert that triggered this transition.

## Trait Implementations§