pgp::composed
# Enum SubpacketConfig 
Source 

```
pub enum SubpacketConfig {
    Default,
    UserDefined {
        hashed: Vec<Subpacket>,
        unhashed: Vec<Subpacket>,
    },
}
```

## Variants§
§
### Default