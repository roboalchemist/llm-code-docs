valitron::rule

# Trait Rule

Source

```
pub trait Rule: Clone {
    type Message;

    const NAME: &'static str;

    // Required methods
    fn message(&self) -> Self::Message;
    fn call(&mut self, data: &mut Value) -> bool;

    // Provided method
    fn call_with_relate(&mut self, data: &mut ValueMap) -> bool { ... }
}
```

## Required Associated Constants§
