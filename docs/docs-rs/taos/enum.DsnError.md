taos
# Enum DsnError 
Source 

```
pub enum DsnError {
    PortErr(ParseIntError),
    InvalidDriver(String),
    InvalidProtocol(String),
    InvalidPassword(String, FromUtf8Error),
    InvalidConnection(String),
    InvalidAddresses(String, String),
    RequireDatabase(String),
    RequireParam(String),
    InvalidParam(String, String),
    NonUtf8Character(FromUtf8Error),
}
```

## Variants§
§
### PortErr(ParseIntError)