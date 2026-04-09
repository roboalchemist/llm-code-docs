lopdf
# Struct SaveOptions 
Source 

```
pub struct SaveOptions {
    pub use_object_streams: bool,
    pub use_xref_streams: bool,
    pub linearize: bool,
    pub object_stream_config: ObjectStreamConfig,
}
```

## Fields§
§`use_object_streams: bool`

Enable object streams for compressing non-stream objects
§`use_xref_streams: bool`

Enable cross-reference streams instead of traditional xref tables
§`linearize: bool`

Enable linearization (fast web view)
§`object_stream_config: ObjectStreamConfig`

Configuration for object streams

## Implementations§