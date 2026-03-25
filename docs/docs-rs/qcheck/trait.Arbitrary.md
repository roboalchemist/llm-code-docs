qcheck
# Trait Arbitrary 
Source 

```
pub trait Arbitrary: Clone + 'static {
    // Required method
    fn arbitrary(g: &mut Gen) -> Self;

    // Provided method
    fn shrink(&self) -> Box<dyn Iterator<Item = Self>> { ... }
}
```

## Required Methods§