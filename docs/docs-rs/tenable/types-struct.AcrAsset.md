tenable::types
# Struct AcrAsset 
Source 

```
pub struct AcrAsset {
    pub id: Option<String>,
    pub fqdn: Option<Vec<String>>,
    pub mac_address: Option<String>,
    pub netbios_name: Option<String>,
    pub ipv4: Option<Vec<String>>,
}
```

## Fields§
§`id: Option<String>`

The UUID for a specific asset. Use this value as the unique key for the asset.
§`fqdn: Option<Vec<String>>`

Fully-qualified domain names (FQDNs) associated with the asset or assets.
§`mac_address: Option<String>`

MAC addresses associated with the asset or assets.
§`netbios_name: Option<String>`

The NetBIOS name for the asset.
§`ipv4: Option<Vec<String>>`

IPv4 addresses associated with the asset or assets.

## Trait Implementations§