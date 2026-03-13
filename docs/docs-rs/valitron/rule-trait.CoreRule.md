valitron::rule

# Trait CoreRule

Source

```
pub trait CoreRule<I, T>:
    'static
    + Sized
    + Clone {
    type Message;

    const THE_NAME: &'static str;

    // Required method
    fn call(&mut self, data: &mut I) -> Result<(), Self::Message>;
}
```

## Required Associated Constants§
