httptest
# Trait IntoTimes 
Source 

```
pub trait IntoTimes: Sealed {
    // Required method
    fn into_times(self) -> (Bound<usize>, Bound<usize>);
}
```

## Required Methods§