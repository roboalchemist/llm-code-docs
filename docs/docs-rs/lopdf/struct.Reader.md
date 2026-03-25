lopdf
# Struct Reader 
Source 

```
pub struct Reader<'a> {
    pub buffer: &'a [u8],
    pub document: Document,
    pub encryption_state: Option<EncryptionState>,
    pub raw_objects: BTreeMap<ObjectId, Vec<u8>>,
    pub password: Option<String>,
}
```

## Fields§
§`buffer: &'a [u8]`§`document: Document`§`encryption_state: Option<EncryptionState>`§`raw_objects: BTreeMap<ObjectId, Vec<u8>>`§`password: Option<String>`
## Implementations§