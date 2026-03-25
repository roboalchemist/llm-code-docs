valitron::rule::string

# Trait StringRule

Source

```
pub trait StringRule: Clone {
    type Message;

    const NAME: &'static str;

    // Required methods
    fn message(&self) -> Self::Message;
    fn call(&mut self, data: &mut String) -> bool;
}
```

## Required Associated Constants§
