victorops::error
# Enum Error 
Source 

```
pub enum Error {
    Http(Error),
    Json(Error),
    UrlParse(ParseError),
    InvalidHeaderValue(InvalidHeaderValue),
    Api {
        status: u16,
        message: String,
    },
    Authentication,
    NotFound,
    InvalidInput(String),
}
```

## Variants§
§
### Http(Error)