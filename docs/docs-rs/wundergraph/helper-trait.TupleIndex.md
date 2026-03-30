wundergraph::helper
# Trait TupleIndex 
Source 

```
pub trait TupleIndex<N> {
    type Value;

    // Required method
    fn get(&self) -> Self::Value;
}
```

## Required Associated Types§