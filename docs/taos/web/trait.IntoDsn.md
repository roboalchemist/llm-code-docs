taos
# Trait IntoDsn 
Source 

```
pub trait IntoDsn {
    // Required method
    fn into_dsn(self) -> Result<Dsn, DsnError>;
}
```

## Required Methods§
Source
#### fn into_dsn(self) -> Result<Dsn, DsnError>