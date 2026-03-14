taos
# Trait IsOffset 
Source 

```
pub trait IsOffset {
    // Required methods
    fn database(&self) -> &str;
    fn topic(&self) -> &str;
    fn vgroup_id(&self) -> i32;
}
```

## Required Methods§