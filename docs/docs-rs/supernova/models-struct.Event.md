supernova::models
# Struct Event 
Source 

```
pub struct Event {
    pub id: EventKey,
    pub title: String,
    pub description: String,
    pub start_date: NaiveDate,
    pub duration: Option<u16>,
    pub capacity: Option<u32>,
    pub cost: Option<u32>,
    pub event_type: GroupEventType,
    /* private fields */
}
```

## Fields§
§`id: EventKey`§`title: String`§`description: String`§`start_date: NaiveDate`§`duration: Option<u16>`§`capacity: Option<u32>`§`cost: Option<u32>`§`event_type: GroupEventType`
## Implementations§