wundergraph::helper
# Trait UnRef 
Source 

```
pub trait UnRef<'a> {
    type UnRefed;

    // Required method
    fn as_ref(v: &'a Self::UnRefed) -> Self;
}
```

## Required Associated Types§