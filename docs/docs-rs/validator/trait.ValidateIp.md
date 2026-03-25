validator
# Trait ValidateIp 
Source 

```
pub trait ValidateIp {
    // Required methods
    fn validate_ipv4(&self) -> bool;
    fn validate_ipv6(&self) -> bool;
    fn validate_ip(&self) -> bool;
}
```

## Required Methods§