valitron::value

# Trait FromValue

Source

```
pub trait FromValue {
    // Required method
    fn from_value(value: &mut ValueMap) -> Option<&mut Self>;
}
```

## Required Methods§

Source

#### fn from_value(value: &mut ValueMap) -> Option<&mut Self>
