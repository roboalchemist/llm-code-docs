statiq::entity
# Trait SqlEntity 
Source 

```
pub trait SqlEntity:
    Sized
    + Send
    + Sync
    + 'static
    + Serialize
    + DeserializeOwned {
}
```

## Required Associated Constants§
Source
#### const TABLE_NAME: &'static str