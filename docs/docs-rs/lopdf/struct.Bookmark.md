lopdf
# Struct Bookmark 
Source 

```
pub struct Bookmark {
    pub children: Vec<u32>,
    pub title: String,
    pub format: u32,
    pub color: [f32; 3],
    pub page: ObjectId,
    pub id: u32,
}
```

## Fields§
§`children: Vec<u32>`

Children, Must be a Collection that allows for insertion of the same page ID.
§`title: String`§`format: u32`

0, 1 for italic, 2 for bold, 3 for italic bold
§`color: [f32; 3]`

R,G,B
§`page: ObjectId`§`id: u32`
## Implementations§