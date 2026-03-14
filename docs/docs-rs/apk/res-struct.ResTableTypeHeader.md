apk::res

# Struct ResTableTypeHeader

Source

```
pub struct ResTableTypeHeader {
    pub id: u8,
    pub res0: u8,
    pub res1: u16,
    pub entry_count: u32,
    pub entries_start: u32,
    pub config: ResTableConfig,
}
```

## Fields§

§`id: u8`

The type identifier this chunk is holding. Type IDs start
at 1 (corresponding to the value of the type bits in a
resource identifier). 0 is invalid.
§`res0: u8`

Must be 0.
§`res1: u16`

Must be 0.
§`entry_count: u32`

Number of u32 entry indices that follow.
§`entries_start: u32`

Offset from header where ResTableEntry data starts.
§`config: ResTableConfig`

Configuration this collection of entries is designed for.

## Implementations§
