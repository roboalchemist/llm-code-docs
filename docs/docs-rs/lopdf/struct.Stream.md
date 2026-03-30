lopdf
# Struct Stream 
Source 

```
pub struct Stream {
    pub dict: Dictionary,
    pub content: Vec<u8>,
    pub allows_compression: bool,
    pub start_position: Option<usize>,
}
```

## Fields§
§`dict: Dictionary`

Associated stream dictionary
§`content: Vec<u8>`

Contents of the stream in bytes
§`allows_compression: bool`

Can the stream be compressed by the `Document::compress()` function?
Font streams may not be compressed, for example
§`start_position: Option<usize>`

Stream data’s position in PDF file.

## Implementations§