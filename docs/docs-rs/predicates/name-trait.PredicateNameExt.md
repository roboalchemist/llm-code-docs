predicates::name

# Trait PredicateNameExt

Source

```
pub trait PredicateNameExt<Item: ?Sized>where
    Self: Predicate<Item>,{
    // Provided method
    fn name(self, name: &'static str) -> NamePredicate<Self, Item>
       where Self: Sized { ... }
}
```

## Provided Methods§
