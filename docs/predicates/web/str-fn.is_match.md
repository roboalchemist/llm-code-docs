predicates::str

# Function is_match

Source

```
pub fn is_match<S>(pattern: S) -> Result<RegexPredicate, RegexError>where
    S: AsRef<str>,
```

Available on **crate feature `regex`** only.
