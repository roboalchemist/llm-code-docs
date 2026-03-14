tap

# Trait TapOptional

Source

```
pub trait TapOptionalwhere
    Self: Sized,{
    type Val: ?Sized;

    // Required methods
    fn tap_some(self, func: impl FnOnce(&Self::Val)) -> Self;
    fn tap_some_mut(self, func: impl FnOnce(&mut Self::Val)) -> Self;
    fn tap_none(self, func: impl FnOnce()) -> Self;

    // Provided methods
    fn tap_some_dbg(self, func: impl FnOnce(&Self::Val)) -> Self { ... }
    fn tap_some_mut_dbg(self, func: impl FnOnce(&mut Self::Val)) -> Self { ... }
    fn tap_none_dbg(self, func: impl FnOnce()) -> Self { ... }
}
```

## Required Associated Types§
