clamav::engine
# Enum ScanResult 
Source 

```
pub enum ScanResult {
    Clean,
    Whitelisted,
    Virus(String),
}
```

## Variants§
§
### Clean