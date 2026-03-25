supernova::errors
# Enum Error 
Source 

```
pub enum Error {
    Generic,
    Server,
    Decode,
    Serialization(Error),
    Deserialization(Error),
    Parsing(Error, String),
    ResourceMissing,
    MissingAuthentication,
    Authentication,
    Client,
    Network,
    Request,
}
```

## Variants§
§
### Generic