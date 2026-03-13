faktory
# Struct ServerSnapshot 
Source 

```
pub struct ServerSnapshot {
    pub description: String,
    pub version: Version,
    pub uptime: Duration,
    pub connections: u64,
    pub command_count: u64,
    pub used_memory_mb: u64,
}
```

## Fields§
§`description: String`

Description of the server process (e.g. “Faktory”).
§`version: Version`

Faktory’s version as semver.
§`uptime: Duration`

Faktory server process uptime in seconds.
§`connections: u64`

Number of clients connected to the server.
§`command_count: u64`

Number of executed commands.
§`used_memory_mb: u64`

Faktory server process memory usage.

## Trait Implementations§