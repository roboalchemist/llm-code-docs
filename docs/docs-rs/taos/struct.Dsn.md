taos
# Struct Dsn 
Source 

```
pub struct Dsn {
    pub driver: String,
    pub protocol: Option<String>,
    pub username: Option<String>,
    pub password: Option<String>,
    pub addresses: Vec<Address>,
    pub path: Option<String>,
    pub subject: Option<String>,
    pub params: BTreeMap<String, String>,
}
```

## Fields§
§`driver: String`§`protocol: Option<String>`§`username: Option<String>`§`password: Option<String>`§`addresses: Vec<Address>`§`path: Option<String>`§`subject: Option<String>`§`params: BTreeMap<String, String>`
## Implementations§