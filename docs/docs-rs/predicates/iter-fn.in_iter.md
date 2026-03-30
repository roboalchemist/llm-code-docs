predicates::iter

# Function in_iter

Source

```
pub fn in_iter<I, T>(iter: I) -> InPredicate<T>where
    T: PartialEq + Debug,
    I: IntoIterator<Item = T>,
```
