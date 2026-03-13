valitron::rule::string

# Function custom

Source

```
pub fn custom<F, M>(f: F) -> RuleList<String, M>where
    F: FnOnce(&mut String) -> Result<(), M> + Clone + 'static,
    M: 'static,
```
