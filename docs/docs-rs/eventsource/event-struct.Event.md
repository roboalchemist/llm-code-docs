eventsource::event
# Struct Event 
Source 

```
pub struct Event {
    pub id: Option<String>,
    pub event_type: Option<String>,
    pub data: String,
}
```

## Fields§
§`id: Option<String>`

Corresponds to the `id` field.
§`event_type: Option<String>`

Corresponds to the `event` field.
§`data: String`

All `data` fields concatenated by newlines.

## Implementations§