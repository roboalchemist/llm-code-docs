tap

# Trait Conv

Source

```
pub trait Convwhere
    Self: Sized,{
    // Provided method
    fn conv<T>(self) -> T
       where Self: Into<T>,
             T: Sized { ... }
}
```

## Provided Methods§
