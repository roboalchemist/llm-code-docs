supernova::models
# Struct Room 
Source 

```
pub struct Room {
    pub title: String,
    pub description: Option<String>,
    pub door_number: Option<u16>,
    pub room_type: RoomType,
    pub extinguished: bool,
    pub capacity: Option<u16>,
    pub equipment: Option<String>,
    pub url: String,
    /* private fields */
}
```

## Fields§
§`title: String`§`description: Option<String>`§`door_number: Option<u16>`§`room_type: RoomType`§`extinguished: bool`§`capacity: Option<u16>`§`equipment: Option<String>`§`url: String`
## Implementations§