eventsource::reqwest
# Enum ErrorKind 
Source 

```
pub enum ErrorKind {
    Reqwest(Error),
    Io(Error),
    Msg(String),
    Http(StatusCode),
    InvalidContentType(Mime),
    NoContentType,
    // some variants omitted
}
```

## Variants§
§
### Reqwest(Error)