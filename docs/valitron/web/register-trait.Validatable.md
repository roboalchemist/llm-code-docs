valitron::register

# Trait Validatable

Source

```
pub trait Validatable<V, E> {
    // Required methods
    fn validate(&self, validator: V) -> Result<(), E>;
    fn validate_mut<'de>(self, validator: V) -> Result<Self, E>
       where Self: Deserialize<'de>;
}
```

## Required Methods§
