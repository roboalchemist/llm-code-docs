liquid::model
# Trait ObjectIndex
Source 

```
pub trait ObjectIndex:
    Debug
    + Display
    + Ord
    + Hash
    + Eq
    + Borrow<str> {
    // Required method
    fn as_index(&self) -> &str;
}
```

## Required Methods§