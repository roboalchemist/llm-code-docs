tenable::types
# Struct Source 
Source 

```
pub struct Source {
    pub name: Option<String>,
    pub first_seen: Option<String>,
    pub last_seen: Option<String>,
}
```

## Fields§
§`name: Option<String>`

The name of the entity that reported the asset details. Sources can include sensors, connectors, and API imports. Source names can be customized by your organization (for example, you specify a name when you import asset records). If your organization does not customize source names, system-generated names include:\n - AWS—You obtained the asset data from an Amazon Web Services connector.\n - NESSUS_AGENT—You obtained the asset data obtained from a Nessus agent scan.\n - PVS—You obtained the asset data from a Nessus Network Monitor (NNM) scan.\n - NESSUS_SCAN—You obtained the asset data from a Nessus scan.\n - WAS—You obtained the asset data from a  Web Application Scanning scan.
§`first_seen: Option<String>`

The ISO timestamp when the source first reported the asset.
§`last_seen: Option<String>`

The ISO timestamp when the source last reported the asset.

## Trait Implementations§