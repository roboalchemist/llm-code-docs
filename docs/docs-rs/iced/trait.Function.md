iced
# Trait Function 
Source 

```
pub trait Function<A, B, O> {
    // Required method
    fn with(self, prefix: A) -> impl Fn(B);
}
```

## Required Methods§