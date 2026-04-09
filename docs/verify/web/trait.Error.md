verify
# Trait Error 
Source 

```
pub trait Error:
    Sized
    + Error
    + AddAssign {
    // Required method
    fn custom<T: Display>(error: T) -> Self;
}
```

## Required Methods§