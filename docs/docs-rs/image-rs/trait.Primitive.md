image
# Trait Primitive 
Source 

```
pub trait Primitive:
    Copy
    + NumCast
    + Num
    + PartialOrd<Self>
    + Clone
    + Bounded {
    const DEFAULT_MAX_VALUE: Self;
    const DEFAULT_MIN_VALUE: Self;
}
```

## Required Associated Constants§