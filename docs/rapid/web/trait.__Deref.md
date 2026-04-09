rapid
# Trait __Deref 
1.0.0 (const: unstable) · Source 

```
pub trait __Deref {
    type Target: ?Sized;

    // Required method
    fn deref(&self) -> &Self::Target;
}
```

## Required Associated Types§