tap::tap

# Trait TapFallible

Source

```
pub trait TapFalliblewhere
    Self: Sized,{
    type Ok: ?Sized;
    type Err: ?Sized;

    // Required methods
    fn tap_ok(self, func: impl FnOnce(&Self::Ok)) -> Self;
    fn tap_ok_mut(self, func: impl FnOnce(&mut Self::Ok)) -> Self;
    fn tap_err(self, func: impl FnOnce(&Self::Err)) -> Self;
    fn tap_err_mut(self, func: impl FnOnce(&mut Self::Err)) -> Self;

    // Provided methods
    fn tap_ok_dbg(self, func: impl FnOnce(&Self::Ok)) -> Self { ... }
    fn tap_ok_mut_dbg(self, func: impl FnOnce(&mut Self::Ok)) -> Self { ... }
    fn tap_err_dbg(self, func: impl FnOnce(&Self::Err)) -> Self { ... }
    fn tap_err_mut_dbg(self, func: impl FnOnce(&mut Self::Err)) -> Self { ... }
}
```

## Required Associated Types§
