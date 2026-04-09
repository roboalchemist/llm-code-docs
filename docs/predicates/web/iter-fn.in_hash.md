predicates::iter

# Function in_hash

Source

```
pub fn in_hash<I, T>(iter: I) -> HashableInPredicate<T>where
    T: Hash + Eq + Debug,
    I: IntoIterator<Item = T>,
```
