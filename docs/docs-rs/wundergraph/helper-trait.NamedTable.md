wundergraph::helper
# Trait NamedTable 
Source 

```
pub trait NamedTable {
    // Required method
    fn name(&self) -> Cow<'static, str>;
}
```

## Required Methods§