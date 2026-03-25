valitron::rule::available

# Enum MessageKind

Source

```
#[non_exhaustive]pub enum MessageKind {
    Required,
    Confirm(String),
    Compare(String, String),
    Contains(String),
    EndsWith(String),
    StartWith(String),
    Length,
    Trim,
    Range,
    Email,
    Regex,
    Fallback(String),
}
```

Available on **crate feature `full`** only.

## Variants (Non-exhaustive)§

§

### Required
