apk::res

# Struct ResChunkHeader

Source

```
pub struct ResChunkHeader {
    pub ty: u16,
    pub header_size: u16,
    pub size: u32,
}
```

## Fields§

§`ty: u16`

Type identifier for this chunk. The meaning of this value depends
on the containing chunk.
§`header_size: u16`

Size of the chunk header (in bytes). Adding this value to the address
of the chunk allows you to find its associated data (if any).
§`size: u32`

Total size of this chunk (in bytes). This is the header_size plus the
size of any data associated with the chunk. Adding this value to the
chunk allows you to completely skip its contents (including any child
chunks). If this value is the same as header_size, there is no data
associated with the chunk.

## Implementations§
