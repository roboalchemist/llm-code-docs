tenable
# Enum Error 
Source 

```
pub enum Error<RE: Debug> {
    InvalidAuth(InvalidHeaderValue),
    Http(Error),
    InsufficientPermission,
    RateLimitReached,
    MaximumWaitTimeReached,
    UnexpectedStatusCode(StatusCode),
    Request(RE),
    Deserialization(Error),
}
```

## Variants§
§
### InvalidAuth(InvalidHeaderValue)