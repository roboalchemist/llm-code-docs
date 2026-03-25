statiq::sproc
# Trait FromResultSet 
Source 

```
pub trait FromResultSet: Sized {
    // Required method
    fn from_result_set(rows: Vec<OdbcRow>) -> Result<Self, SqlError>;
}
```

## Required Methods§
Source
#### fn from_result_set(rows: Vec<OdbcRow>) -> Result<Self, SqlError>