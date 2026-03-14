taos
# Struct Address 
Source 

```
pub struct Address {
    pub host: Option<String>,
    pub port: Option<u16>,
    pub path: Option<String>,
}
```

## Fields§
§`host: Option<String>`

Host or ip address of the server.
§`port: Option<u16>`

Port to connect to the server.
§`path: Option<String>`

Use unix socket path to connect.

## Implementations§