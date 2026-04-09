tap::prelude

# Trait TryConv

Source

```
pub trait TryConvwhere
    Self: Sized,{
    // Provided method
    fn try_conv<T>(self) -> Result<T, Self::Error>
       where Self: TryInto<T>,
             T: Sized { ... }
}
```

## Provided Methods§
