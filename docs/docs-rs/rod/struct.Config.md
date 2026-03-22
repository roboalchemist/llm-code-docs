rod
# Struct Config 
Source 

```
pub struct Config {
    pub allow_public_space: bool,
    pub my_pub: Option<String>,
    pub stats: bool,
}
```

## Fields§
§`allow_public_space: bool`§`my_pub: Option<String>`

Prioritize data storage for this public key. Format: x.y where x and y are base64 encoded ECDSA public key coordinates.
Example: hyECQHwSo7fgr2MVfPyakvayPeixxsaAWVtZ-vbaiSc.TXIp8MnCtrnW6n2MrYquWPcc-DTmZzMBmc2yaGv9gIU
§`stats: bool`

Show node stats at /stats?

## Trait Implementations§