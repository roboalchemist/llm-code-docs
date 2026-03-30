wundergraph::helper
# Trait UnRefClone 
Source 

```
pub trait UnRefClone {
    type UnRefed;

    // Required method
    fn make_owned(self) -> Self::UnRefed;
}
```

## Required Associated Types§