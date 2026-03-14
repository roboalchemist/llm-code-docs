predicates::path

# Trait PredicateFileContentExt

Source

```
pub trait PredicateFileContentExtwhere
    Self: Predicate<[u8]> + Sized,{
    // Provided method
    fn from_file_path(self) -> FileContentPredicate<Self> { ... }
}
```

## Provided Methods§
