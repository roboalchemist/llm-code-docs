nettle::ecc
# Trait Curve 
Source 

```
pub trait Curve {
    // Required method
    unsafe fn get_curve() -> *const ecc_curve;

    // Provided method
    unsafe fn bit_size() -> u32 { ... }
}
```

## Required Methods§