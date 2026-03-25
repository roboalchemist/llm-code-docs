druid

# Trait Data

Source

```
pub trait Data: Clone + 'static {
    // Required method
    fn same(&self, other: &Self) -> bool;
}
```

## Required Methods§
