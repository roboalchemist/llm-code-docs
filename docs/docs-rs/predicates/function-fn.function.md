predicates::function

# Function function

Source

```
pub fn function<F, T>(function: F) -> FnPredicate<F, T>where
    F: Fn(&T) -> bool,
    T: ?Sized,
```
